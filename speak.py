import requests
from pydub import AudioSegment
from pydub.playback import play
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "kL06KYMvPY56NluIQ72m"

is_speaking = False

def speak(text, retries=3):
    global is_speaking
    is_speaking = True

    if not API_KEY:
        print("❌ ElevenLabs API key not found.")
        is_speaking = False
        return

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.55,
            "similarity_boost": 0.75
        }
    }

    for attempt in range(retries):
        try:
            response = requests.post(url, json=data, headers=headers, timeout=20)
            response.raise_for_status()

            audio = AudioSegment.from_mp3(response.content)

            play(audio)  # ✅ Cross-platform playback

            time.sleep(0.4)
            break

        except Exception as e:
            print(f"⚠️ Voice error (attempt {attempt+1}/{retries}): {e}")
            time.sleep(1)

    is_speaking = False
