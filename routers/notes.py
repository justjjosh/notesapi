from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app import models, schemas

router = APIRouter(
    prefix="/notes",
    tags=["notes"]
)

@router.post("/", response_model = schemas.NoteResponse, status_code=201)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db=db, note=note)

@router.get("/{note_id}", response_model = schemas.NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db=db, note_id=note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note

@router.get("/", response_model = list[schemas.NoteResponse])
def get_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_notes(db=db, skip=skip, limit=limit)

@router.put("/{note_id}", response_model = schemas.NoteResponse)
def update_note(note_id: int, note: schemas.NoteUpdate, db: Session=Depends(get_db)):
    upd_note = crud.update_note(db=db, note=note, note_id=note_id)
    if upd_note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return upd_note

@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    del_note = crud.delete_note(db=db, note_id=note_id)
    if del_note is None:
        raise HTTPException(status_code=404, detail="note not found")

#many to many relationship
@router.post("/{note_id}/tags/{tag_id}", response_model=schemas.NoteResponse, status_code = 201)
def add_tag_to_note(note_id: int, tag_id: int, db: Session=Depends(get_db)):
    added_tag = crud.add_tag_to_note(db=db, note_id=note_id, tag_id=tag_id)
    if added_tag is None:
        raise HTTPException(status_code=404, detail="invalid note or tag")
    return added_tag

@router.delete("/{note_id}/tags/{tag_id}", status_code = 204)
def remove_tag_from_note(note_id: int, tag_id: int, db: Session=Depends(get_db)):
    removed_tag = crud.remove_tag_from_note(db=db, note_id=note_id, tag_id = tag_id)
    if removed_tag is None:
        raise HTTPException(status_code=404, detail="invalid note or tag")
