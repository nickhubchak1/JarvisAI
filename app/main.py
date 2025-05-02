from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uuid, os

from app.utils.whisper_infer import transcribe_audio
from app.utils.llama3_infer import generate_response
from app.utils.tts_infer import synthesize_speech

app = FastAPI()

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    uid = str(uuid.uuid4())
    input_path = f"/tmp/{uid}_input.wav"
    output_path = f"/tmp/{uid}_output.wav"

    # Save uploaded file
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Whisper: STT
    prompt = transcribe_audio(input_path)

    # LLaMA 3: LLM response
    response = generate_response(prompt)

    # TTS: convert response to voice
    synthesize_speech(response, output_path)

    return FileResponse(output_path, media_type="audio/wav")
