from sqlalchemy.orm import Session
from models import Entry
from schemas import EntryCreate, EntryUpdate

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

def delete_entry(db: Session, entry_id: int):
    db_entry = db.query(Entry).filter(Entry.id == entry_id).first()
    if db_entry:
        db.delete(db_entry)
        db.commit()
        return True
    return False

def update_entry(db: Session, entry_id: int, entry_update: EntryUpdate):
    db_entry = db.query(Entry).filter(Entry.id == entry_id).first()
    if not db_entry:
        return None

    if entry_update.title is not None:
        db_entry.title = entry_update.title
    if entry_update.content is not None:
        db_entry.content = entry_update.content
    if entry_update.summary is not None:
        db_entry.summary = entry_update.summary
    if entry_update.mood is not None:
        db_entry.mood = entry_update.mood

    db.commit()
    db.refresh(db_entry)
    return db_entry
