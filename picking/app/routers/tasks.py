from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import api_schemas
import bll.tasks
from bll.constants import TaskStatus

from dependencies.database import get_db

router = APIRouter()


@router.post("/tasks/create-task", tags=["Tasks"], response_model=api_schemas.ShortTask)
async def create_task(task: api_schemas.TaskCreate, db: Session = Depends(get_db)):
    """Create a new task"""
    return bll.tasks.create_task(db, task)


@router.get("/tasks/task_info/{task_id}", tags=["Tasks"], response_model=api_schemas.DetailedTask)
async def get_task_info(task_id: int, db: Session = Depends(get_db)):
    """Get task by id"""
    task_data = bll.tasks.get_all_task_data(db, task_id)
    task = task_data["task"]
    picked_products = task_data["picked_products"]
    needed_skus = task_data["needed_skus"]

    return api_schemas.DetailedTask(
        id=task.id,
        status=task.status,
        status_str=TaskStatus(task.status).name,
        skus=[api_schemas.Sku(id=sku.sku_id, count=sku.count) for sku in needed_skus],
        picked_products=[api_schemas.Product(barcode=product.product_barcode, sku_id=product.sku_id) for product in
                         picked_products],
        progress=api_schemas.Progress(total=sum([sku.count for sku in needed_skus]), picked=len(picked_products))
    )
