from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import data_access.aggregated_info
import schemas.aggregated_info
import data_access

from dependencies.database import get_db

router = APIRouter()


@router.post("/aggregated-info/find-skus-in-units", tags=["AggregatedInfo"],
             response_model=list[schemas.aggregated_info.FoundUnit])
async def find_skus_in_units(sku_ids: list[int], db: Session = Depends(get_db)):
    """Find units containing needed skus"""
    resp = data_access.aggregated_info.find_skus_in_units(db, sku_ids)
    return [{
                "unit_barcode": unit_barcode,
                "skus": skus
            } for unit_barcode, skus in resp.items()]
