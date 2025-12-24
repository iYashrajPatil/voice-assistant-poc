# Voice Assistant – Python (POC)

## Overview
This project is a Python-based conversational voice assistant developed as a proof of concept.  
It accepts user voice input, processes predefined company-related questions offline, and responds using a female text-to-speech voice.

## Features
- Voice input using microphone
- Speech-to-text using Google Speech Recognition (Indian English)
- Offline company Q&A (no LLM / no AI model)
- Female voice output using ElevenLabs TTS
- Windows-compatible audio playback
- Error handling and retry mechanism for TTS

## Tech Stack
- Python 3.10
- SpeechRecognition
- ElevenLabs Text-to-Speech API
- FFmpeg
- Windows native audio playback

## Project Flow
1. User speaks a question
2. Speech is converted to text
3. Text is matched with predefined company FAQs
4. Response is converted to speech
5. Audio is played back to the user

## Known Limitations
- Speech recognition accuracy depends on microphone quality
- Always-on listening may miss initial words in some cases
- Internet required for TTS and STT

## How to Run
1. Create and activate virtual environment
2. Install dependencies:
pip install -r requirements.txt
3. Add ElevenLabs API key in `speak.py`
4. Run:

## Future Improvements
- Push-to-talk or wake-word support
- Hindi and Marathi language support
- Improved intent detection
- Offline speech recognition

