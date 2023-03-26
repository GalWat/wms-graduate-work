from pydantic import BaseModel


class OrmBase(BaseModel):
    class Config:
        orm_mode = True


class Sku(BaseModel):
    id: int
    count: int


class Product(BaseModel):
    barcode: str
    sku_id: int


class Progress(BaseModel):
    picked: int
    total: int


class TaskCreate(BaseModel):
    skus: list[Sku]


class ShortTask(OrmBase):
    id: int
    status: int


class DetailedTask(BaseModel):
    id: int
    status: int
    status_str: str
    skus: list[Sku]
    picked_products: list[Product]
    progress: Progress
