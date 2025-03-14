# API Router allows us to define routes separately and then include them in main.py for better modularity
# UploadFile is a FastAPI class for handling file uploads efficiently
# File is a FastAPI class that specifies a file upload field in API requests
# aiofiles is a library that allows us to read and write files asynchronously. used over open() 
# because it allows for non-blocking file operations

# The upload_file function takes a file parameter of type UploadFile and writes the file to the uploads directory
# The function returns a dictionary containing the filename and path of the uploaded file

from fastapi import APIRouter, UploadFile, File 
import aiofiles
import os

router = APIRouter()

UPLOAD_DIR = "uploads"  # Define the directory where files will be uploaded

os.makedirs(UPLOAD_DIR, exist_ok=True)  # Create the uploads directory if it does not exist

# Define a route for uploading files
@router.post("/")
async def upload_file(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}" # File is saved in the uploads directory with the filename provided by the client

    async with aiofiles.open(file_path, "wb") as f: # Open the file in write binary mode asynchronously
        content = await file.read() # Reads the uploaded file content asynchronously
        await f.write(content) # Writes the content to the file asynchronously

    return {"filename": file.filename, "path": file_path} # Returns a dictionary containing the filename and path of the uploaded file