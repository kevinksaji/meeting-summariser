from fastapi import APIRouter, HTTPException
from app.services.deepseek_service import summarise_text

router = APIRouter()

@router.post("/")
def summarise(data: dict):
    """
    API endpoint to summarize transcribed text.
    """
    text = data.get("text", "").strip()
    
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty for summarization.")
    
    try:
        summary = summarise_text(text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))