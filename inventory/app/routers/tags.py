from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from schemas import tags as schemas
from bll import tags as bll
from dependencies.database import get_db

router = APIRouter()


@router.post("/tags/create", tags=["Tags"])
async def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    """Create a new tag"""
    return bll.create_tag(db, tag)


@router.get("/tags/{tag_id}", tags=["Tags"], response_model=schemas.Tag)
async def get_tag(tag_id: int, db: Session = Depends(get_db)):
    """Get tag by id"""
    return bll.get_tag(db, tag_id)

