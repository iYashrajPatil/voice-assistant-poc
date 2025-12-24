import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    # ✅ Balanced settings (IMPORTANT)
    r.energy_threshold = 250
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1.2
    r.phrase_threshold = 0.3
    r.non_speaking_duration = 0.6

    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1.2)

        try:
            audio = r.listen(
                source,
                timeout=5,              # wait max 5 sec for speech
                phrase_time_limit=8     # max length of sentence
            )
        except sr.WaitTimeoutError:
            return ""

    try:
        text = r.recognize_google(audio, language="en-IN")
        print("You said:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""

    except sr.RequestError as e:
        print(f"❌ Speech service error: {e}")
        return ""
