from schemas.units import (
    CreateUnitResponse,
    CreateUnitRequest,
    GetUnitResponse
)
from queries.units import UnitsQueries

from fastapi import APIRouter

router = APIRouter()


@router.post("/units/create", tags=["Units"], response_model=CreateUnitResponse)
async def create_unit(unit: CreateUnitRequest):
    """Create a unit"""
    result = UnitsQueries().insert_unit(barcode="", type_id=unit.type_id, current_location_id=unit.location)
    unit_id = result["id"]
    unit_barcode = f"un{unit_id}"
    UnitsQueries().update_unit_barcode(unit_id=unit_id, barcode=unit_barcode)
    return result


@router.get("/units/{unit_id}", tags=["Units"], response_model=GetUnitResponse)
async def get_unit(unit_id: int):
    """Get a unit"""
    query_result = UnitsQueries().select_unit(unit_id)
    return GetUnitResponse(**query_result)
