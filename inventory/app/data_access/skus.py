from sqlalchemy.orm import Session

import models
from schemas import skus as schemas


def get_sku(db: Session, sku_id: int):
    return db.query(models.Sku).filter(models.Sku.id == sku_id).first()


def create_sku(db: Session, sku: schemas.SkuCreate):
    db_sku = models.Sku(name=sku.name, tag_ids=sku.tag_ids)
    db.add(db_sku)
    db.commit()
    db.refresh(db_sku)
    return db_sku
