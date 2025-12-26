# RAGenius
Smart Multi-Modal RAG API
📌 Project Objective
This project is a smart Retrieval-Augmented Generation (RAG) API designed to answer complex questions based on information extracted from a wide variety of document types. The system utilizes a FastAPI backend to process unstructured text, images (via OCR), and structured data to provide context-aware responses.



🚀 Key Features

Universal Ingestion: Supports .pdf, .docx, .txt, .jpg, .png, .csv, and SQLite .db files.



Multi-Modal Support: Capable of handling both text-based and image-based questions using OCR and advanced LLM prompting.




Semantic Search: Uses OpenAI/HuggingFace embeddings and FAISS/ChromaDB for high-speed similarity searches.



Contextual Accuracy: Returns final answers along with the retrieved context and source metadata (e.g., page numbers and filenames).




🛠️ Tech Stack

Backend: Python, FastAPI, Async/Await 


Vector Database: FAISS / ChromaDB 


OCR Engine: Pytesseract / EasyOCR 


Parsers: pdfplumber, python-docx, Pandas, SQLite3 




LLM Integration: OpenAI API / Claude / Hugging Face Hub 

⚙️ Environment Setup
Clone the Repository:

Bash

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Create a Virtual Environment:

Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

Bash

pip install -r requirements.txt
Configure Environment Variables: Create a .env file in the root directory and add your keys:

Plaintext

OPENAI_API_KEY=your_openai_api_key_here
TESSERACT_PATH=/usr/bin/tesseract  # Path to your Tesseract OCR executable
📋 API Usage
1. Upload a Document
Endpoint: POST /upload Used to ingest files and add them to the vector store.


Payload: Multipart Form-data (file)

2. Ask a Question
Endpoint: POST /query Used to retrieve answers based on the uploaded documents.


Sample Request Body: 


JSON

{
  "question": "What are the payment terms mentioned in the invoice?",
  "image_base64": "optional_base64_string"
}

Sample Response: 


JSON

{
  "answer": "The payment terms are net 30 days.",
  "context": "Payment terms: net 30 days from date of invoice...",
  "source": "page 2 of invoice.pdf"
}
🐳 Bonus Features (Implemented)

Containerization: Full Docker support for easy deployment.



UI: A minimal web frontend built with Streamlit for interactive testing.


Orchestration: Chaining and logic handled via LangChain.
