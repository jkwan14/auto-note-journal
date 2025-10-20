from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime, timezone
from db import Base


class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    content = Column(Text, nullable=False)
    summary = Column(Text)
    mood = Column(String(50))
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
