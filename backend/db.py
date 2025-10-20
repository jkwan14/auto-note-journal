from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/auto_note_journal"

    class Config:
        env_file = ".env"


settings = Settings()


engine = create_engine(settings.DATABASE_URL, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
