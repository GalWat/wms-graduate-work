from . import OrmBase
from pydantic import BaseModel


class ProductCreate(BaseModel):
    unit_barcode: str
    supply_id: int | None
    sku_id: int


class Product(OrmBase):
    id: int
    barcode: str
    unit_barcode: str
    sku_id: int
    supply_id: int | None
