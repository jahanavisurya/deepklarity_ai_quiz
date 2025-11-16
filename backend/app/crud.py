from sqlalchemy.orm import Session
from . import models

def get_quiz_by_url(db: Session, url: str):
    return db.query(models.QuizPage).filter(models.QuizPage.url == url).first()

def create_quiz_page(db: Session, data: dict):
    obj = models.QuizPage(
        url=data['url'],
        title=data.get('title'),
        summary=data.get('summary'),
        key_entities=data.get('key_entities'),
        sections=data.get('sections'),
        full_text=data.get('full_text'),
        quiz=data.get('quiz'),
        related_topics=data.get('related_topics')
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def list_quiz_pages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.QuizPage).order_by(models.QuizPage.created_at.desc()).offset(skip).limit(limit).all()

def get_quiz_by_id(db: Session, qid: int):
    return db.query(models.QuizPage).filter(models.QuizPage.id == qid).first()
