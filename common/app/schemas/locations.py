from pydantic import BaseModel


class CreateLocationRequest(BaseModel):
    type_id: int
    group_id: int
    x: int
    y: int
    orientation: int


class CreateLocationResponse(BaseModel):
    id: int


class GetLocationResponse(BaseModel):
    id: int
    barcode: str
    type_id: int
    group_id: int
    x: int
    y: int
    orientation: int


class UnitLocation(BaseModel):
    unit_barcode: str
    location_id: int
    x: int
    y: int


class LocationWithUnits(BaseModel):
    location_id: int
    x: int
    y: int
    unit_barcodes: list[str]
