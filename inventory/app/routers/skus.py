from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import skus as schemas
from data_access import skus as data_access

from dependencies.database import get_db

router = APIRouter()


@router.post("/skus/create", tags=["Skus"])
async def create_sku(sku: schemas.SkuCreate, db: Session = Depends(get_db)):
    """Create a new sku"""
    return data_access.create_sku(db, sku)


@router.get("/skus/{sku_id}", tags=["Skus"], response_model=schemas.Sku)
async def get_sku(sku_id: int, db: Session = Depends(get_db)):
    """Get sku by id"""
    return data_access.get_sku(db, sku_id)
