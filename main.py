import os
from ingestion import DocumentProcessor
from vector_store import VectorManager

def run_pipeline(data_folder):
    # 1. Initialize our components
    processor = DocumentProcessor()
    v_db = VectorManager()
    
    print(f"🚀 Starting AI Ingestion Pipeline on: {data_folder}")

    # 2. Loop through all files in My H: drive folder
    for filename in os.listdir(data_folder):
        file_path = os.path.join(data_folder, filename)
        
        # Skip folders, only process files
        if os.path.isfile(file_path):
            print(f"📄 Processing: {filename}...")
            
            # Step A: Extract Text
            raw_text = processor.get_text_from_any(file_path)
            
            if "Error" in raw_text or "Unsupported" in raw_text:
                print(f"❌ {raw_text}")
                continue
                
            # Step B: Create Chunks
            chunks = processor.create_chunks(raw_text)
            
            # Step C: Save to Vector Database
            v_db.add_chunks_to_db(chunks)
            
    print("\n✅ All documents have been indexed! Your AI is now 'Smart'.")

if __name__ == "__main__":
    # Point this to the folder on My H: drive where your PDFs/images are
    MY_DATA = "./test_files" 
    
    # Create the folder if it doesn't exist
    if not os.path.exists(MY_DATA):
        os.makedirs(MY_DATA)
        print(f"⚠️ Created {MY_DATA} folder. Please put a PDF in there and run again!")
    else:
        run_pipeline(MY_DATA)