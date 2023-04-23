from queries.locations import LocationsQueries

from fastapi import APIRouter
from bll.svg_plan_drawer import Drawer
import bll.routing
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/routing/warehouse-plan", tags=["Routing"], response_class=HTMLResponse)
async def get_warehouse_plan():
    """Get warehouse plan in SVG format"""
    query_result = LocationsQueries().select_locations_by_type(type_id=2)  # Rack
    racks = {(rack["x"], rack["y"]): rack["orientation"] for rack in query_result}

    drawer = Drawer(block_size=25, w_count=32, h_count=17, pixel_scale=2)
    return HTMLResponse(content=drawer.draw(racks).as_html(), status_code=200)


@router.post("/routing/warehouse-plan", tags=["Routing"], response_class=HTMLResponse)
async def get_warehouse_plan(location_ids: list[int]):
    """Draw warehouse plan in SVG format with marked locations"""
    query_result = LocationsQueries().select_locations_by_type(type_id=2)  # Rack
    racks = {(rack["x"], rack["y"]): rack["orientation"] for rack in query_result}

    query_result = LocationsQueries().select_locations(tuple(location_ids))
    marked_racks = {(rack["x"], rack["y"]) for rack in query_result}

    drawer = Drawer(block_size=25, w_count=32, h_count=17, pixel_scale=2)
    return HTMLResponse(content=drawer.draw(racks, marked_racks).as_html(), status_code=200)


@router.get("/routing/start-distance-calculation", tags=["Routing"])
async def start_distance_calculation():
    """Start distance calculation"""
    pass


@router.get("/routing/all-distances", tags=["Routing"])
async def get_all_distances():
    """Get distances between all locations"""
    return str(bll.routing.calculate_distance_between_all())


@router.post("/routing/map-locations-into-floor-coordinates", tags=["Routing"])
async def map_locations_into_floor_coordinates(location_ids: list[int]):
    """Map locations into floor coordinates"""
    return str(bll.routing.map_locations_into_floor_coordinates(location_ids))
