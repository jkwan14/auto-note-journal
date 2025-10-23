from sqlalchemy.orm import Session
from models import Entry
from schemas import EntryCreate

def get_entries(db: Session):
    return db.query(Entry).all()

def get_entry_by_id(db: Session, entry_id: int):
    return db.query(Entry).filter(Entry.id == entry_id).first()

def create_entry(db: Session, entry: EntryCreate):
    new_entry = Entry(title=entry.title, content=entry.content)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def delete_entry(db: Session, entry_id: int)
    db_entry = db.query(Entry).filter(Entry.id == entry.id).first()
    if db_entry:
        db.delete(db_entry)
        db.commit()
        return True
    return False
