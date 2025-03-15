import sys
from fastapi import APIRouter, UploadFile, File, HTTPException
import aiofiles
from app.services.whisper_service import transcribe_audio
from app.services.deepseek_service import summarise_text

router = APIRouter()

UPLOAD_DIR = "uploads/"

@router.post("/")
async def process_meeting(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}{file.filename}"

    # Step 1: Save the uploaded file
    async with aiofiles.open(file_path, "wb") as f:
        content = await file.read()
        await f.write(content)

    print("Hello, world")

    try:
        print(f"✅ File saved: {file_path}", file=sys.stderr)  # Force print to console

        # Step 2: Transcribe the audio file
        transcription = transcribe_audio(file_path)
        print(f"📝 Transcription Output: {transcription}", file=sys.stderr)  # Force print

        # Step 3: Summarise the transcribed text
        summary = summarise_text(transcription)
        print(f"📌 Summary Output: {summary}", file=sys.stderr)  # Force print

        return {"summary": summary}
    except Exception as e:
        print(f"❌ Error: {str(e)}", file=sys.stderr)  # Force print errors
        raise HTTPException(status_code=500, detail=str(e))