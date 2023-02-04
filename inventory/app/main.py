from fastapi import FastAPI
from routers import skus

app = FastAPI()

app.include_router(skus.router)
