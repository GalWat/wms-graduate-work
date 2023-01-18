from schemas.locations import (
    CreateLocationRequest,
    CreateLocationResponse,
    GetLocationResponse
)
from queries.locations import LocationsQueries

from fastapi import APIRouter

router = APIRouter()


@router.post("/locations/create", tags=["Locations"], response_model=CreateLocationResponse)
async def create_location(location: CreateLocationRequest):
    """Create a location group"""
    result = LocationsQueries().insert_location(barcode="", type_id=location.type_id, group_id=location.group_id)
    location_id = result["id"]
    location_barcode = f"lc{location_id}"
    LocationsQueries().update_location_barcode(location_id=location_id, barcode=location_barcode)
    return result


@router.get("/locations/{location_id}", tags=["Locations"], response_model=GetLocationResponse)
async def get_location(location_id: int):
    """Get a location group"""
    query_result = LocationsQueries().select_location(location_id)
    return GetLocationResponse(**query_result)
