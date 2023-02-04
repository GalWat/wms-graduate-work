from pydantic import BaseModel


class CreateSkuRequest(BaseModel):
    name: str
    tag_ids: list[int] | None


class CreateSkuResponse(BaseModel):
    id: int


class GetSkuResponse(BaseModel):
    id: int
    name: str
    tag_ids: list[int] | None
