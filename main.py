from listen import listen
from logic import get_answer
from speak import speak
import random

print("🤖 Voice Assistant Started")
print("Say 'stop' to exit")

# Short, natural fillers to mask thinking delay
FILLERS = [
    "Let me check that for you.",
    "One moment please.",
    "Let me think.",
    "Checking that now."
]

while True:
    user_text = listen()

    # If speech was not understood, listen again
    if not user_text:
        continue

    # Exit condition
    if "stop" in user_text or "exit" in user_text:
        speak("Goodbye. Have a nice day.")
        break

    # 🧠 Speak a short filler BEFORE heavy processing
    filler = random.choice(FILLERS)
    speak(filler)

    # Get answer (offline first, then LLM)
    answer = get_answer(user_text)
    print("Bot:", answer)

    # Speak the final answer
    speak(answer)
