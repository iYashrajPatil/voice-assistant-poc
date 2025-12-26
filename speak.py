import requests
import os
from dotenv import load_dotenv
from pydub import AudioSegment
from pydub.playback import play

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "kL06KYMvPY56NluIQ72m"

def speak(text):
    if not API_KEY:
        print("❌ ElevenLabs API key not found.")
        return

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.55,
            "similarity_boost": 0.75
        }
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        # ✅ Always treat response as binary MP3
        with open("reply.mp3", "wb") as f:
            f.write(response.content)

        # ✅ Let pydub auto-detect format
        audio = AudioSegment.from_file("reply.mp3")
        play(audio)

        os.remove("reply.mp3")

    except Exception as e:
        print(f"⚠️ TTS error: {e}")
