# 🎙️ General-Purpose AI Voice Assistant (Offline)

This project is a **general-purpose AI voice assistant** that supports:
- Voice input
- Intelligent responses
- Offline predefined Q&A
- General open-domain answers using a **local LLM**
- Voice output (Text-to-Speech)

The system is designed to run on **low-end machines (4GB RAM)** and works **offline for reasoning**.

---

## ✨ Features

- 🎤 Speech-to-Text (voice input)
- 🧠 Hybrid intelligence:
  - Offline predefined answers (company/domain questions)
  - Local open-source LLM for general questions
- 🔌 Fully offline reasoning (no cloud LLM APIs)
- 🔊 Text-to-Speech output
- 💻 Works on Windows & Ubuntu
- 🧩 Modular and extensible architecture

---

## 🏗️ Architecture Overview

User Voice
↓
Speech-to-Text
↓
Logic Router
├── Offline Q&A (qa.py)
└── Local LLM (Ollama)
↓
Text-to-Speech

---

## 📁 Project Structure

Voicebot/
│
├── main.py # Application entry point
├── listen.py # Speech-to-text
├── speak.py # Text-to-speech
├── logic.py # Hybrid logic (offline + LLM)
├── qa.py # Predefined offline Q&A
├── llm_logic.py # Local LLM (Ollama) integration
│
├── requirements.txt
├── README.md
├── .env # API keys (not committed)
├── .gitignore
└── venv/ # Virtual environment (ignored)


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd Voicebot
```
### 2️⃣ Create virtual environment
```bash
python -m venv venv
## Activate
venv\Scripts\activate
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
## 🧠 Local LLM Setup (Ollama)

This project uses Ollama to run a lightweight open-source LLM locally.

Install Ollama

### Windows

Download installer from https://ollama.com

Install and restart system

### Linux / Ubuntu
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
### Pull the model
```bash
ollama pull phi
```
### Test
```bash
ollama run phi
```
## 🔑 Environment Variables

Create a .env file in the project root:
```bash
ELEVENLABS_API_KEY=your_api_key_here
```
⚠️ .env is excluded from GitHub via .gitignore.

### Run the App:
``` bash
python main.py
```
### Say:
- “What is your company name?” (offline)
- “Explain machine learning” (LLM)
- “Stop” (exit)

## ⚠️ Known Limitations

- Small response delay due to local LLM + TTS
- No internet-based knowledge updates
- Voice latency depends on hardware and network (for TTS)

## 🚀 Future Improvements

- Offline Text-to-Speech
- Hindi / Marathi language support
- Streaming TTS for reduced latency
- Better intent detection

## 📌 Summary

This project demonstrates a hybrid, general-purpose AI voice assistant using:

- Offline rule-based logic
- Local open-source language models
- Modular voice pipeline

###### Designed for privacy, offline usage, and low-resource systems.

## Author:
##### Yashraj Patil

