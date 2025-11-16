import json
from datetime import datetime
from sqlalchemy.orm import Session
from .models import QuizPage

async def process_quiz(url: str, db: Session):

    # MOCK SAFE OUTPUT (because scraper is not connected)
    quiz_data = {
        "url": url,
        "title": "Sample Title",
        "summary": "Sample Summary",
        "key_entities": {},
        "sections": [],
        "quiz": [
            {
                "question": "Who is mentioned in the article?",
                "options": ["Alan Turing", "Einstein", "Newton", "Tesla"],
                "answer": "Alan Turing",
                "difficulty": "easy",
                "explanation": "Alan Turing is main subject."
            }
        ],
        "related_topics": ["Cryptography", "Computer Science"],
        "created_at": datetime.now().isoformat()
    }

    db_page = QuizPage(**quiz_data)

    db.add(db_page)
    db.commit()
    db.refresh(db_page)

    return db_page

