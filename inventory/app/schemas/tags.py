from pydantic import BaseModel


class TagCreate(BaseModel):
    name: str


class Tag(BaseModel):
    id: int
    name: str
