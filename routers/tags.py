from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app import models, schemas

router = APIRouter(
    prefix="/tags",
    tags=["tags"]
)

@router.post("/", response_model = schemas.TagResponse, status_code=201)
def create_tag(tag: schemas.TagCreate, db: Session=Depends(get_db)):
    return crud.create_tag(db=db, tag=tag)

@router.get("/{tag_id}", response_model=schemas.TagResponse)
def get_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = crud.get_tag(db=db, tag_id=tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="tag not found")
    return tag

@router.get("/", response_model = list[schemas.TagResponse])
def get_tags(db: Session = Depends(get_db)):
    return crud.get_tags(db=db)

@router.delete("/{tag_id}", status_code=204)
def delete_tag(tag_id: int, db: Session=Depends(get_db)):
    del_tag = crud.delete_tag(db=db, tag_id=tag_id)
    if del_tag is None:
        raise HTTPException(status_code=404, detail="tag not found")