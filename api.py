import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from chatbot import LocalAIChatbot # My existing class
import shutil

app = FastAPI(title="RAG API")
bot = LocalAIChatbot()

# Folder for uploads
UPLOAD_DIR = "test_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class QuestionRequest(BaseModel):
    question: str

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Workflow Step 1: Upload a file (.pdf, .docx, .jpg)"""
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Trigger the indexing logic (Run My main.py logic here)
    # bot.v_db.index_new_file(file_path) 
    
    return {"message": f"Successfully uploaded {file.filename}. Ready for RAG."}

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """Workflow Step 2 & 3: Ask a question and get Context + Answer + Source"""
    try:
        #  modif ask function to return a dictionary instead of just a string
        result = bot.ask_with_metadata(request.question) 
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)