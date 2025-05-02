from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

def synthesize_speech(text, output_path):
    tts.tts_to_file(text=text, file_path=output_path)
