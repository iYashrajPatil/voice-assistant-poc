def get_answer(user_text):

    if "company" in user_text and "name" in user_text:
        return "Our company name is Electrosoft."

    if "who" in user_text and ("you" in user_text or "are you" in user_text):
        return "I am Electra, the company voice assistant."

    if "where" in user_text and ("located" in user_text or "location" in user_text):
        return "We are located in Maharashtra, India."

    if "what" in user_text and "do" in user_text and "company" in user_text:
        return "We provide software and artificial intelligence solutions."

    return "Sorry, I did not understand that. Please ask again."
