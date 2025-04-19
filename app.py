# app.py
import streamlit as st
import pdfplumber
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import os

# Load semantic model (CPU)
model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')

# Extract text from file
def extract_text(file):
    ext = file.name.split('.')[-1].lower()
    text = ""
    if ext == "pdf":
        with pdfplumber.open(file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif ext == "txt":
        text = file.read().decode("utf-8")
    elif ext in ["xls", "xlsx"]:
        df = pd.read_excel(file)
        text = df.astype(str).apply(lambda x: ' '.join(x), axis=1).str.cat(sep='\n')
    return text

# Find best answer using semantic similarity
def find_best_answer(user_question, document_text):
    if not document_text:
        return "Sorry, I couldn't extract any text from the document."

    document_sentences = document_text.split('\n')
    document_embeddings = model.encode(document_sentences, convert_to_tensor=True, device='cpu')
    query_embedding = model.encode(user_question, convert_to_tensor=True, device='cpu')
    scores = util.pytorch_cos_sim(query_embedding, document_embeddings)[0]

    best_match_idx = int(scores.argmax())
    best_score = float(scores[best_match_idx])

    if best_score > 0.5:
        return document_sentences[best_match_idx]
    else:
        save_unanswered_question(user_question)
        return "Sorry, I couldn't find a relevant answer."

# Save unanswered questions
def save_unanswered_question(question):
    with open('unanswered_questions.txt', 'a') as file:
        file.write(f"{question}\n")

# Load unanswered questions
def load_unanswered_questions():
    if os.path.exists('unanswered_questions.txt'):
        with open('unanswered_questions.txt', 'r') as file:
            return file.read()
    return "No unanswered questions yet."

# Streamlit UI
st.title("📄 Document Q&A Bot with Semantic Search")

uploaded_file = st.file_uploader("Upload a PDF, TXT, XLS, or XLSX file", type=["pdf", "txt", "xls", "xlsx"])

if uploaded_file:
    document_text = extract_text(uploaded_file)
    st.success("✅ File processed and ready!")
    question = st.text_input("💬 Ask a question about the document:")

    if st.button("Get Answer") and question:
        answer = find_best_answer(question, document_text)
        st.markdown(f"**Answer:** {answer}")

st.markdown("---")
st.subheader("📋 View Unanswered Questions")

if st.button("Show Unanswered Questions"):
    st.code(load_unanswered_questions())
