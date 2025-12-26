from qa import qa
from llm_logic import get_llm_answer


def get_answer(user_text):
    """
    Hybrid logic:
    1. Answer from offline Q&A if available
    2. Otherwise, fallback to local LLM (Ollama)
    """

    user_text = user_text.lower()

    # 1️⃣ Offline Q&A
    for question in qa:
        if question in user_text:
            return qa[question]

    # 2️⃣ General-purpose LLM
    return get_llm_answer(user_text)
