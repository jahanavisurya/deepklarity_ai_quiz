from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict, Any
from datetime import datetime

class QuizItem(BaseModel):
    question: str
    options: List[str]
    answer: str
    difficulty: str
    explanation: Optional[str]

class QuizPageCreate(BaseModel):
    url: HttpUrl

class QuizPageOut(BaseModel):
    id: int
    url: HttpUrl
    title: Optional[str]
    summary: Optional[str]
    key_entities: Optional[Dict[str, Any]]
    sections: Optional[List[str]]
    quiz: Optional[List[QuizItem]]
    related_topics: Optional[List[str]]
    created_at: Optional[datetime]   # ⭐ FIXED — should be datetime not string

    class Config:
        orm_mode = True

