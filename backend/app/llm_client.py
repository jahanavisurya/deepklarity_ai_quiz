import os, json, re
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('LLM_API_KEY')
def generate_quiz(title, summary, full_text):
    # Simple stub: produce 5 sample questions based on title
    return [{
        "question": f"What is {title} known for?",
        "options": ["A","B","C","D"],
        "answer": "A",
        "difficulty": "easy",
        "explanation": "Sample explanation"
    }]
def generate_related(title, summary):
    return ["Related Topic 1", "Related Topic 2"]
