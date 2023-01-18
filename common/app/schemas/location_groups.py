from pydantic import BaseModel


class CreateLocationGroupRequest(BaseModel):
    name: str


class CreateLocationGroupResponse(BaseModel):
    id: int


class GetLocationGroupResponse(BaseModel):
    id: int
    name: str
