from sqlalchemy.orm import Session

import models
from schemas import tags as schemas


def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()


def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
