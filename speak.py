import requests
from pydub import AudioSegment
import winsound
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key securely
API_KEY = os.getenv("API_KEY")

# Your existing voice ID (unchanged)
VOICE_ID = "kL06KYMvPY56NluIQ72m"

# 🔒 Speaking lock
is_speaking = False


def speak(text, retries=3):
    global is_speaking
    is_speaking = True

    if not API_KEY:
        print("❌ ElevenLabs API key not found. Check .env file.")
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
            response = requests.post(
                url,
                json=data,
                headers=headers,
                timeout=20
            )
            response.raise_for_status()

            # Save audio
            with open("reply.mp3", "wb") as f:
                f.write(response.content)

            # Convert MP3 → WAV
            audio = AudioSegment.from_mp3("reply.mp3")
            audio.export("reply.wav", format="wav")

            # 🔊 Play and WAIT till finished
            winsound.PlaySound("reply.wav", winsound.SND_FILENAME)

            # Cleanup
            os.remove("reply.mp3")
            os.remove("reply.wav")

            time.sleep(0.4)
            break

        except Exception as e:
            print(f"⚠️ Voice error (attempt {attempt + 1}/{retries}): {e}")
            time.sleep(1)

    is_speaking = False
