import whisper

def transcribe_audio(file_path: str):
    """ Transcribes an audio file using Whisper"""

    model = whisper.load_model("base")
    print("Model loaded sucessfully")
    result = model.transcribe(file_path) # use the in built transcribe method to transcribe the audio file

    return result["text"] # return the transcribed text