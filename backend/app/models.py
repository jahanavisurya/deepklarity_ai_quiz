from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.sql import func
from .database import Base

class QuizPage(Base):
    __tablename__ = "quiz_pages"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    title = Column(String, nullable=True)
    summary = Column(String, nullable=True)
    key_entities = Column(JSON, nullable=True)
    sections = Column(JSON, nullable=True)
    quiz = Column(JSON, nullable=True)
    related_topics = Column(JSON, nullable=True)
    created_at = Column(String, server_default=func.now())
