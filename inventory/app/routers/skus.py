from fastapi import APIRouter

router = APIRouter()


@router.get("/skus/test", tags=["Skus"])
async def get_test():
    """Get a sku"""
    return "Hello from Inventory"

