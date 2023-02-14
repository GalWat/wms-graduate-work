from sqlalchemy.orm import Session

import models
from schemas import products as schemas


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict(), barcode="")
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    db_product.barcode = f"pr{db_product.id}"
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
