from schemas.locations import (
    CreateLocationRequest,
    CreateLocationResponse,
    GetLocationResponse,
    UnitLocation,
    LocationWithUnits
)
from queries.locations import LocationsQueries

from fastapi import APIRouter

router = APIRouter()


@router.post("/locations/create", tags=["Locations"], response_model=CreateLocationResponse)
async def create_location(location: CreateLocationRequest):
    """Create a location group"""
    result = LocationsQueries().insert_location(barcode="", type_id=location.type_id, group_id=location.group_id,
                                                x=location.x, y=location.y)
    location_id = result["id"]
    location_barcode = f"lc{location_id}"
    LocationsQueries().update_location_barcode(location_id=location_id, barcode=location_barcode)
    return result


@router.get("/locations/{location_id}", tags=["Locations"], response_model=GetLocationResponse)
async def get_location(location_id: int):
    """Get a location group"""
    query_result = LocationsQueries().select_location(location_id)
    return GetLocationResponse(**query_result)


@router.post("/locations/find-locations-by-units", tags=["Locations"], response_model=list[UnitLocation])
async def find_locations_by_units(unit_barcodes: list[str]):
    """Find locations by units"""
    barcodes = tuple(unit_barcodes)
    query_result = LocationsQueries().select_locations_by_units(barcodes)
    return [UnitLocation(**x) for x in query_result]


@router.post("/locations/group-units-into-locations", tags=["Locations"], response_model=list[LocationWithUnits])
async def group_units_into_locations(unit_barcodes: list[str]):
    """Group units into locations"""
    barcodes = tuple(unit_barcodes)
    query_result = LocationsQueries().select_locations_by_units(barcodes)

    mapped = {}
    for unit in query_result:
        loc_id = unit["location_id"]

        if loc_id not in mapped:
            mapped[loc_id] = {

                "location_id": loc_id,
                "x": unit["x"],
                "y": unit["y"],
                "unit_barcodes": [unit["unit_barcode"]]
            }
        else:
            mapped[loc_id]["unit_barcodes"].append(unit["unit_barcode"])

    return [LocationWithUnits(**x) for x in mapped.values()]
