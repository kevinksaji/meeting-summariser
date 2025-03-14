from fastapi import FastAPI
from app.routes import auth, upload, transcription, summarisation

# Create a FastAPI instance
app = FastAPI(title="Meeting Summariser API")

# Include the routers from the routes module
app.include_router(auth.router, prefix="/auth")
app.include_router(upload.router, prefix="/upload")
app.include_router(transcription.router, prefix="/transcribe")
# app.include_router(summarisation.router, prefix="/summarise")

# Define a root route
@app.get("/")
def root():
    return {"message": "Welcome to the Meeting Summariser API!"}