from fastapi import FastAPI
from routers import location_groups

app = FastAPI()

app.include_router(location_groups.router)
