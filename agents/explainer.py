from utils.groq_client import call_llm

SYSTEM = """You are a friendly tutor. Explain the given topics in simple, beginner-friendly language.
Use bullet points. Keep it concise (under 300 words per topic)."""

def explain_topics(subject: str, topics: str) -> str:
    prompt = f"Subject: {subject}\nTopics: {topics}\nExplain each topic briefly."
    return call_llm(SYSTEM, prompt)