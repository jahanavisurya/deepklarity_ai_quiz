from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session

# ============================================
# DIRECT POSTGRESQL CONNECTION (YOUR CONFIG)
# ============================================

# Your real PostgreSQL URL with encoded '@'
DATABASE_URL = "postgresql://postgres:janu%40123@localhost:5432/deepklarity"

# ============================================

# Create engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# Session maker
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

