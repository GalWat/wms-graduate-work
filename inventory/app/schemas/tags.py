from pydantic import BaseModel
from . import OrmBase


class TagCreate(BaseModel):
    name: str


class Tag(OrmBase):
    id: int
    name: str
