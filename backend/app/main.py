from fastapi import FastAPI
from app.routes import auth, upload, transcription, summarisation

app = FastAPI(title="Meeting Summariser API")

app.include_router(auth.router, prefix="auth")
app.include_router(upload.router, prefix="upload")
app.include_router(transcription.router, prefix="transcribe")
app.include_router(summarisation.router, prefix="summarise")

@app.get("/")
def root():
    return {"message": "Welcome to the Meeting Summariser API!"}