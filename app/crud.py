from sqlalchemy.orm import Session
from . import models, schemas

#Crud operations for Notes
def create_note(db: Session, note: schemas.NoteCreate):
    new_note = models.Note(**note.model_dump())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def get_notes(db: Session, skip: int = 0, limit: int = 10):
     return db.query(models.Note).offset(skip).limit(limit).all()

def update_note(db: Session, note_id: int, note: schemas.NoteUpdate):
    updated_note = get_note(db, note_id)
    if updated_note is None:
        return None
    
    for key, value in note.model_dump(exclude_unset=True).items():
        setattr(updated_note, key, value)

    db.add(updated_note)
    db.commit()
    db.refresh(updated_note)
    return updated_note

def delete_note(db: Session, note_id: int):
    deleted_note = get_note(db, note_id)
    if deleted_note is None:
        return None
    db.delete(deleted_note)
    db.commit()
    return deleted_note

#Crud operations for tags
def create_tag(db: Session, tag: schemas.TagCreate):
    new_tag = models.Tag(**tag.model_dump())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag

def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()

def get_tags(db: Session):
    return db.query(models.Tag).all()

def delete_tag(db: Session, tag_id: int):
    deleted_tag = get_tag(db, tag_id)
    if deleted_tag is None:
        return None
    db.delete(deleted_tag)
    db.commit()
    return deleted_tag

#Crud operations for relationships
def add_tag_to_note(db: Session, note_id: int, tag_id: int):
    note = get_note(db, note_id)
    tag = get_tag(db, tag_id)

    if note is None or tag is None: 
        return None
    
    note.tags.append(tag)

    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def remove_tag_from_note(db: Session, note_id: int, tag_id: int):
    note = get_note(db, note_id)
    tag = get_tag(db, tag_id)

    if note is None or tag is None:
        return None
    
    note.tags.remove(tag)
    if tag not in note.tags:
        return None
    
    db.add(note)
    db.commit()
    return note