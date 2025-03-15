from fastapi import APIRouter, UploadFile, File
import aiofiles
from app.services.whisper_service import transcribe_audio

# Create a new APIRouter instance
router = APIRouter()

@router.post("/")
async def transcribe(file: UploadFile = File(...)):
    """Receives an uploaded audio file, saves it, and transcribes it using Whisper."""
    file_path = f"uploads/{file.filename}"

    # Save the uploaded file correctly
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(await file.read())  # ✅ Fix applied: await file.read()

    # Transcribe the saved file
    text = transcribe_audio(file_path) 


    return {"transcription": text}
