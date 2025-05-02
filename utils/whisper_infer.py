import whisper

model = whisper.load_model("base.en")

def transcribe_audio(path):
    result = model.transcribe(path)
    return result["text"]
