import subprocess

def get_llm_answer(question):
    """
    Calls local Ollama model (phi) for general-purpose answers.
    """

    result = subprocess.run(
        ["ollama", "run", "phi"],
        input=question,
        text=True,
        capture_output=True,
        shell=True   # ✅ IMPORTANT for Windows
    )

    return result.stdout.strip()
