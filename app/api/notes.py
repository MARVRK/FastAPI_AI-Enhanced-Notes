from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.services.notes import (
    get_note, create_note, delete_note, update_note, get_notes
)
from app.services.openai import summarize_all_notes
from app.services.statistics import get_notes_statistics
from app.db.session import get_db
from app.schemas.notes import NoteCreate, NoteUpdate, NoteResponse

router = APIRouter()


@router.get("/notes/summary")
def summarize_notes_endpoint(db: Session = Depends(get_db)):
    return summarize_all_notes(db)
@router.post("/notes/", response_model=NoteResponse)
def create_note_endpoint(note_data: NoteCreate, db: Session = Depends(get_db)):
    try:
        return create_note(note_data, db)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.get("/notes/")
def get_notes_endpoint(db: Session = Depends(get_db)):
    note = get_notes(db)
    if not note:
        return {"Message": "no notes found in database"}
    return note

@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    note = get_note(note_id, db)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/notes/{note_id}", response_model=NoteResponse)
def update_note_endpoint(note_id: int, note_data: NoteUpdate, db: Session = Depends(get_db)):
    updated_note = update_note(note_id, note_data, db)
    if updated_note == "Note not found":
        raise HTTPException(status_code=404, detail="Note not found in database")
    return updated_note

@router.delete("/notes/{note_id}")
def delete_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    result = delete_note(note_id, db)
    if result == "Note not found":
        raise HTTPException(status_code=404, detail="Note not found")
    return JSONResponse(status_code=200, content=result)


@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):
    try:
        return get_notes_statistics(db)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
