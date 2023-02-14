from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import products as schemas
from data_access import products as data_access

from dependencies.database import get_db

router = APIRouter()


@router.post("/products/create", tags=["Products"])
async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Create a new product"""
    return data_access.create_product(db, product)


@router.get("/products/{product_id}", tags=["Products"], response_model=schemas.Product)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    """Get product by id"""
    return data_access.get_product(db, product_id)
