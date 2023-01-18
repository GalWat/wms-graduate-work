from pydantic import BaseModel


class CreateUnitRequest(BaseModel):
    type_id: int
    location: int


class CreateUnitResponse(BaseModel):
    id: int


class GetUnitResponse(BaseModel):
    id: int
    barcode: str
    type_id: int
    current_location_id: int
    target_location_id: int | None
