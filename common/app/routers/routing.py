from queries.locations import LocationsQueries

from fastapi import APIRouter
from bll.svg_plan_drawer import Drawer
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/routing/warehouse-plan", tags=["Routing"], response_class=HTMLResponse)
async def get_warehouse_plan():
    """Get warehouse plan in SVG format"""
    query_result = LocationsQueries().select_locations_by_type(type_id=2)  # Rack
    racks = {(rack["x"], rack["y"]): rack["orientation"] for rack in query_result}

    drawer = Drawer(block_size=25, w_count=32, h_count=17, pixel_scale=2)
    return HTMLResponse(content=drawer.draw(racks).as_html(), status_code=200)


@router.get("/routing/start-distance-calculation", tags=["Routing"])
async def start_distance_calculation():
    """Start distance calculation"""
    pass


