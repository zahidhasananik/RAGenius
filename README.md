# Local RAG Assistant 

### 📋 Prerequisites
- Install **Ollama** (ollama.com)
- Run `ollama pull llama3`

### ⚙️ Setup
1. Extract the ZIP.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file based on `.env.example`.

### 🚀 How to Run
1. **Indexing:** Run `python main.py` to process the sample files.
2. **API:** Run `uvicorn api:app --reload`.


### 📡 API Endpoints
- `POST /upload`: Uploads .pdf, .docx, or .jpg.
- `POST /ask`: Takes a JSON `{"question": "..."}` and returns Answer + Context + Source.

- Project link- https://huggingface.co/spaces/Anik694/rag-genius
