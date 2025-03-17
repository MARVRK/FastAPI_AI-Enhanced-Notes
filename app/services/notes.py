from datetime import datetime

from sqlalchemy.orm import Session
from app.models.notes import Note
from app.schemas.notes import NoteCreate, NoteUpdate, NoteResponse


def create_note(note_data: NoteCreate, db: Session):
    new_note = Note(title=note_data.title, content=note_data.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


def get_notes(db: Session):
    notes = db.query(Note).all()
    return notes


def get_note(note_id: int, db: Session):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        return "Note not found"
    return note


def update_note(note_id: int, note_data: NoteUpdate, db: Session):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        return "Note not found"

    updated = False

    if note.title is not None:
        note.title = note_data.title
        updated = True
    if note.content is not None:
        note.content = note_data.content
        updated = True

    if updated is True:
        note.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(note)
    return note


def delete_note(note_id: int, db: Session):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        return "Note not found"
    db.delete(note)
    db.commit()
    return {"message": f"Note {note_id} successfully deleted"}
