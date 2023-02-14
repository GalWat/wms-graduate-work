from fastapi import FastAPI
from routers import tags, skus, products

app = FastAPI()

app.include_router(tags.router)
app.include_router(skus.router)
app.include_router(products.router)

