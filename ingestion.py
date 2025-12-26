import os
import pdfplumber
import docx
import pandas as pd
import pytesseract
from PIL import Image

class DocumentProcessor:
    def __init__(self):
        # Update this path for actual Tesseract installation path
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def get_text_from_any(self, file_path):
        """Detects extension and routes to the correct parser."""
        ext = os.path.splitext(file_path)[1].lower()
        
        try:
            if ext == '.pdf':
                return self._parse_pdf(file_path)
            elif ext == '.docx':
                return self._parse_docx(file_path)
            elif ext in ['.jpg', '.png', '.jpeg']:
                return self._parse_image(file_path)
            elif ext == '.csv':
                return self._parse_csv(file_path)
            else:
                return f"Unsupported file type: {ext}"
        except Exception as e:
            return f"Error processing {file_path}: {str(e)}"

    def _parse_pdf(self, path):
        text = ""
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += f"[Page {i+1}] " + page_text + "\n"
        return text

    def _parse_docx(self, path):
        doc = docx.Document(path)
        return "\n".join([para.text for para in doc.paragraphs])

    def _parse_image(self, path):
        return pytesseract.image_to_string(Image.open(path))

    def _parse_csv(self, path):
        df = pd.read_csv(path)
        return df.to_string()

    def create_chunks(self, text, chunk_size=800, overlap_pct=0.15):
        """Creates chunks with a specific percentage of overlap."""
        chunks = []
        overlap_size = int(chunk_size * overlap_pct)
        step = chunk_size - overlap_size
        
        for i in range(0, len(text), step):
            chunk = text[i : i + chunk_size]
            chunks.append(chunk)
            # Stop if we've reached the end of the text
            if i + chunk_size >= len(text):
                break
        return chunks

# --- Execution Block ---
if __name__ == "__main__":
    processor = DocumentProcessor()
    
    # Place a file named 'test_data.pdf' or 'data.csv' My your H: folder to test
    filename = "My_file_here.pdf" 
    
    if os.path.exists(filename):
        raw_text = processor.get_text_from_any(filename)
        processed_chunks = processor.create_chunks(raw_text)
        
        print(f"✅ Successfully parsed: {filename}")
        print(f"✅ Created {len(processed_chunks)} chunks.")
        print(f"--- Preview of Chunk 1 ---\n{processed_chunks[0][:200]}...")
    else:
        print("Please place a sample file in the folder to test!")