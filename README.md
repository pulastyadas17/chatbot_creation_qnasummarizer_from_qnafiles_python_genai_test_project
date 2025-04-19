# chatbot_creation_qnasummarizer_from_qnafiles_python_genai_test_project

✅ Here’s how it works:
📌 File Upload & Text Extraction: Users can upload a variety of document formats (PDF, TXT, XLSX), and the system extracts the text using the pdfplumber library for PDFs and Pandas for Excel sheets.
📌 Q&A Extraction: The extracted text is processed to identify Q&A pairs, where each question is followed by an answer. This is crucial for training the system to understand the document structure.
📌 Question Matching with Sentence Transformers: When a user asks a question, the system uses the Sentence Transformers model to match the query with the most relevant answer from the document using semantic search. The model encodes both the document’s questions and the user query, comparing them to find the best match.

✅ Key Features:
📌 Supports PDF, TXT, and XLSX document formats.
📌 Uses semantic search to find the most relevant answers, ensuring a highly accurate response to user questions.
📌 Built with Streamlit, providing a simple, interactive interface for easy usage.

![image](https://github.com/user-attachments/assets/55c64d93-4d93-4d29-a4a0-257236b0fa3e)

![image](https://github.com/user-attachments/assets/15b4ae23-466c-4369-aa94-edd8c0cf7229)

