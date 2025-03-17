from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from app.db.base import Base

class Note(Base):
    __tablename__ = 'note'
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String,unique=False, nullable=False)
    content: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)
