from sqlalchemy.orm import Session

import db_models
import api_schemas
from .constants import TaskStatus


def create_task(db: Session, task_data: api_schemas.TaskCreate):
    db_task = db_models.Task(status=TaskStatus.Created.value)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    db_skus = [db_models.Sku(task_id=db_task.id, sku_id=sku.id, count=sku.count) for sku in task_data.skus]
    db.add_all(db_skus)
    db.commit()

    return db_task


def get_all_task_data(db: Session, task_id: int):
    task = db.query(db_models.Task).filter(db_models.Task.id == task_id).first()
    needed_skus = db.query(db_models.Sku).filter(db_models.Sku.task_id == task_id).all()
    picked_products = db.query(db_models.Product).filter(db_models.Product.task_id == task_id).all()

    return {
        "task": task,
        "needed_skus": needed_skus,
        "picked_products": picked_products
    }
