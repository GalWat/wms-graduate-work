from . import OrmBase
from pydantic import BaseModel


class SkuCreate(BaseModel):
    name: str
    tag_ids: list[int] | None


class Sku(OrmBase):
    id: int
    name: str
    tag_ids: list[int] | None
