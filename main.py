from listen import listen
from logic import get_answer
from speak import speak, is_speaking
import time

print("🤖 Voice Assistant Started")
print("Say 'stop' to exit")

while True:

    # 🔒 Don't listen while speaking
    if is_speaking:
        time.sleep(0.1)
        continue

    user_text = listen()

    if user_text == "":
        continue

    if "stop" in user_text or "exit" in user_text:
        speak("Goodbye. Have a nice day.")
        break

    answer = get_answer(user_text)
    print("Bot:", answer)
    speak(answer)
