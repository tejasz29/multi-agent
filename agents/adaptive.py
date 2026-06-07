from utils.groq_client import call_llm

SYSTEM = """You are an adaptive learning coach.
You receive a student's study progress (completed and missed days).
Provide:
1. A short analysis of their progress.
2. Specific recommendations for catching up on missed topics.
3. A motivational message.
Keep the response under 250 words."""

def get_adaptive_advice(completed: list, missed: list, remaining_days: int) -> str:
    prompt = f"""
Completed study sessions: {completed}
Missed study sessions: {missed}
Remaining days before exam: {remaining_days}
Give adaptive recommendations.
"""
    return call_llm(SYSTEM, prompt)