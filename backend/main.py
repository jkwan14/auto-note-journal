from fastapi import FastAPI, HTTPException, Depends
from pydantic_settings import BaseSettings
from sqlalchemy.orm import Session
from typing import List

from db import get_db
import crud
from schemas import EntryOut, EntryCreate, EntryUpdate


class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
app = FastAPI(title="Auto-Note Journal", version= "0.1.0")

@app.get("/test")
def health():
    return {"Status": "Pass"}

@app.get("/entries", response_model=List[EntryOut])
def read_entries(db: Session = Depends(get_db)):
    return crud.get_entries(db)

@app.post("/entries", response_model=EntryOut)
def create_new_entry(entry: EntryCreate, db: Session = Depends(get_db)):
    return crud.create_entry(db, entry)

@app.get("/entries/{entry_id}", response_model=EntryOut)
def read_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = crud.get_entry_by_id(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

@app.patch("/entries/{entry_id}", response_model=EntryOut)
def patch_entry(entry_id: int, entry_update: EntryUpdate, db: Session = Depends(get_db)):
    updated = crud.update_entry(db, entry_id, entry_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Entry not found")
    return updated

@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_entry(db, entry_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"ok": True}

@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_entry(db, entry_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"ok": True}
