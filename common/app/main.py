import psycopg2
from config import settings
from fastapi import FastAPI
from models import LocationGroup

app = FastAPI()

conn = psycopg2.connect(
    host=settings.db.host,
    database=settings.db.database,
    user=settings.db.user,
    password=settings.db.password,
    port=settings.db.port
)
cur = conn.cursor()


@app.get("/")
async def read_root():
    return {
        "Hello": "World"
    }


@app.post("/location_groups/create")
async def create_location_group(location_group: LocationGroup) -> int:
    """Create a location group"""
    cur.execute(f"INSERT INTO location_groups VALUES (DEFAULT, '{location_group.name}') RETURNING id")
    conn.commit()

    row = cur.fetchone()
    return row[0]
