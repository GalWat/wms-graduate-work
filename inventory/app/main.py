from fastapi import FastAPI
from routers import tags, skus, products, aggregated_info

app = FastAPI()

app.include_router(tags.router)
app.include_router(skus.router)
app.include_router(products.router)
app.include_router(aggregated_info.router)

