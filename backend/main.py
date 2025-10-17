from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
app = FastAPI(title="Auto-Note Journal", version= "0.1.0")

@app.get("/test")
def health():
    return {"Status": "Pass"}
