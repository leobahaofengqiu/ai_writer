import os, requests
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def _call_gemini(prompt: str):
    if not GEMINI_API_KEY:
        return "Gemini API key missing."
    res = requests.post(
        f"{BASE_URL}?key={GEMINI_API_KEY}",
        json={"contents":[{"parts":[{"text": prompt}]}]}
    )
    data = res.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"AI error: {str(e)}"

def generate_assignment(topic: str, subject: str):
    prompt = f"""
    Write a detailed, well-structured academic assignment on the topic '{topic}' for subject '{subject}'.
    The assignment must include:
    - A clear title
    - Introduction
    - 2–3 main body sections with headings
    - A formal conclusion
    - Maintain academic formatting, clarity, and tone.
    """
    return _call_gemini(prompt)

def generate_proposal(topic: str, subject: str):
    prompt = f"""
    Write a professional project proposal for the topic '{topic}' under subject '{subject}'.
    Include:
    - Proposal title
    - Problem statement
    - Objectives
    - Methodology
    - Expected outcomes
    - Timeline (short version)
    Use formal and business-style writing.
    """
    return _call_gemini(prompt)
