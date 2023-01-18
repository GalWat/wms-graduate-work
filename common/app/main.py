from fastapi import FastAPI
from routers import location_groups, locations, units

app = FastAPI()

app.include_router(location_groups.router)
app.include_router(locations.router)
app.include_router(units.router)
