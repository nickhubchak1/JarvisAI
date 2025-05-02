# Jarvis LLM Voice Assistant (Private and Ethical AI)

This project provides a voice-enabled, privacy-focused AI assistant inspired by Jarvis from Iron Man. It is designed for use in mobile apps and runs entirely offline in a Docker container. No user data is logged or transmitted to third parties.

The system uses the following components:

- Whisper for speech-to-text (STT)
- LLaMA 3 (quantized GGUF) for large language model inference
- Coqui TTS for generating Jarvis-style voice responses
- FastAPI for backend API serving

## Features

- Accepts voice input (WAV/FLAC format)
- Transcribes voice to text locally using Whisper
- Generates intelligent responses using a locally hosted LLaMA 3 model
- Synthesizes text responses into speech with a configurable Jarvis-like voice
- Returns audio files to mobile clients for playback

## Requirements

- Docker and Docker Compose
- Minimum 8GB RAM
- Internet access for initial model downloads (optional for offline use)

## Folder Structure

```
jarvis-assistant/
├── app/
│   ├── main.py
│   └── utils/
│       ├── whisper_infer.py
│       ├── llama3_infer.py
│       └── tts_infer.py
├── models/
│   └── llama-3-8b.gguf
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/jarvis-assistant.git
cd jarvis-assistant
```

### 2. Download LLaMA 3 GGUF Model

Download a quantized `.gguf` version of LLaMA 3 from Hugging Face.

Example using `wget`:

```bash
mkdir -p models
wget -O models/llama-3-8b.gguf https://huggingface.co/TheBloke/Llama-3-8B-GGUF/resolve/main/llama-3-8b.Q4_K_M.gguf
```

### 3. Build the Docker Container

```bash
docker-compose build
```

### 4. Run the Assistant

```bash
docker-compose up
```

The FastAPI server will start at:

```
http://localhost:8000
```

## API Usage

### POST /process-audio/

Sends a voice input and receives a spoken Jarvis-style response.

**Request**

- Method: `POST`
- Content-Type: `multipart/form-data`
- Form field: `file` (WAV or FLAC)

**Example with curl:**

```bash
curl -X POST http://localhost:8000/process-audio/   -H "accept: audio/wav"   -F "file=@test.wav" --output response.wav
```

**Response**

Returns a `.wav` audio file of the AI-generated spoken response.

## Privacy

This system is designed for local and offline deployment. No data is logged or shared externally.

- All speech and text processing occurs inside the Docker container.
- Whisper and LLaMA 3 run locally; no API keys or cloud inference are used.
- TTS runs with no telemetry or usage tracking.

## Troubleshooting

- Verify the presence of the `models/llama-3-8b.gguf` file.
- Whisper will automatically download the `base.en` model unless manually cached.
- Set the environment variable `COQUI_TOS_AGREED=1` to suppress Coqui warnings.

## License

This project is provided for research, educational, and ethical development use only. Ensure your application complies with local laws and data privacy guidelines.