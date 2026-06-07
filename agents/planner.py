from utils.groq_client import call_llm
import json, re

SYSTEM = """You are an expert academic planner. 
Given a list of subjects and the number of study days, generate a structured day-wise study plan.
Respond ONLY with a valid JSON array. Each element must have:
  "day" (int), "subject" (string), "topics" (string, comma-separated).
Distribute subjects evenly. Progress from basics to advanced. Include at least 2 revision days at the end.
Do NOT include any explanation or markdown — only the raw JSON array."""

def generate_plan(subjects: list[str], days: int) -> list[dict]:
    prompt = f"Subjects: {', '.join(subjects)}\nStudy days available: {days}\nGenerate the plan."
    raw = call_llm(SYSTEM, prompt)
    # Strip possible markdown code fences
    raw = re.sub(r"```(?:json)?", "", raw).strip().rstrip("`").strip()
    return json.loads(raw)