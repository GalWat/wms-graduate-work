from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import tags as schemas
from data_access import tags as data_access
from dependencies.database import get_db

router = APIRouter()


@router.post("/tags/create", tags=["Tags"])
async def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    """Create a new tag"""
    return data_access.create_tag(db, tag)


@router.get("/tags/{tag_id}", tags=["Tags"], response_model=schemas.Tag)
async def get_tag(tag_id: int, db: Session = Depends(get_db)):
    """Get tag by id"""
    return data_access.get_tag(db, tag_id)
