import sys
from fastapi import APIRouter, UploadFile, File, HTTPException
import aiofiles
from app.services.whisper_service import transcribe_audio
from app.services.deepseek_service import summarise_text

router = APIRouter()

UPLOAD_DIR = "uploads/"

@router.post("", response_model=dict)  # Accepts `/process`
@router.post("/", response_model=dict)  # Accepts `/process/`
async def process_meeting(file: UploadFile = File(...)):

    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    print(f"Received file: {file.filename}", file=sys.stderr)
    file_path = f"{UPLOAD_DIR}{file.filename}"

    # save the uploaded file
    async with aiofiles.open(file_path, "wb") as f:
        content = await file.read()
        await f.write(content)

    try:
        print(f"File saved: {file_path}", file=sys.stderr)

        # transcribe the audio file
        transcription = transcribe_audio(file_path)
        print(f"Transcription Output: {transcription}", file=sys.stderr)

        # summarise the transcribed text
        summary = summarise_text(transcription)
        print(f"Summary Output: {summary}", file=sys.stderr)

        return {"summary": summary}
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        raise HTTPException(status_code=500, detail=str(e))