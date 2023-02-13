from fastapi import FastAPI
from routers import tags, skus

app = FastAPI()

app.include_router(tags.router)
app.include_router(skus.router)
