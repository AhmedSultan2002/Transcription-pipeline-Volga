from fastapi import FastAPI, UploadFile, HTTPException
import shutil
import os
from app.services.transcription import execute_transcription
from app.utils.formatting import format_transcription_segments

app = FastAPI()

@app.post("/upload/")
async def accept_audio_file(file: UploadFile):
    """
    Service endpoint strictly for receiving and validating audio files.
    """
    # 1. Basic Validation (Rejecting obvious bad files early)
    allowed_content_types = {"audio/mpeg", "audio/wav", "audio/x-m4a"}
    if file.content_type not in allowed_content_types:
        raise HTTPException(status_code=400, detail="Unsupported audio format")

    # 2. Storage (Saving to a temporary directory)
    storage_dir = "secure_audio_storage"
    os.makedirs(storage_dir, exist_ok=True)
    
    file_path = os.path.join(storage_dir, file.filename)
    
    with open(file_path, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 3. Return a reference ID so downstream services can find it
    return {
        "status": "success", 
        "message": "Audio accepted for processing.",
        "file_id": file.filename, 
        "path": file_path 
    }

@app.get("/transcription/{file_id}")
async def get_transcription_results(file_id: str):
    """
    Endpoint that chains the transcription and formatting services.
    """
    file_path = f"secure_audio_storage/{file_id}"
    
    try:
        # Step 2: Extract raw data
        raw_segments, _ = execute_transcription(file_path)
        
        # Step 3: Format with timestamps
        final_json_output = format_transcription_segments(raw_segments)
        
        return {
            "file_id": file_id,
            "data": final_json_output
        }
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")