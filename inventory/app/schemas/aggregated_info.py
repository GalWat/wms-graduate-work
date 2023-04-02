from pydantic import BaseModel


class FoundSku(BaseModel):
    sku_id: int
    count: int


class FoundUnit(BaseModel):
    unit_barcode: str
    skus: list[FoundSku]
