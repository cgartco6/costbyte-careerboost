from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./careerboost.db"  # Replace with Postgres for production

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def init_db():
    from models.user import User
    from models.resume import Resume
    from models.transaction import Transaction
    Base.metadata.create_all(bind=engine)
