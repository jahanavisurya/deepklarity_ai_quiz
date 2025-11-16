from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import get_db
from .quiz_generator import process_quiz
from .database import engine, Base
from .models import QuizPage

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root
@app.get("/")
async def root():
    return {"status": "ok"}


# --------------------------
#  POST /generate
# --------------------------
@app.post("/generate")
async def generate_quiz(data: dict, db: Session = Depends(get_db)):
    url = data["url"]
    return await process_quiz(url, db)


# --------------------------
#  GET /history
# --------------------------
@app.get("/history")
async def history(db: Session = Depends(get_db)):
    items = db.query(QuizPage).order_by(QuizPage.id.desc()).all()
    return items


# --------------------------
#  GET /quiz/{id}  ← FIXED
# --------------------------
@app.get("/quiz/{quiz_id}")
async def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(QuizPage).filter(QuizPage.id == quiz_id).first()

    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return quiz
