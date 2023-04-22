from sqlalchemy.orm import Session
from sqlalchemy import func

from models import Product
from constants import StockType


def find_skus_in_units(db: Session, sku_ids: list[int]):
    query_result = db.query(Product.unit_barcode, Product.sku_id, func.count(Product.id).label('count')) \
        .filter(Product.sku_id.in_(sku_ids)) \
        .filter(Product.stock_type == StockType.Valid) \
        .group_by(Product.unit_barcode, Product.sku_id) \
        .all()

    skus_in_units = {}
    for unit_barcode, sku_id, count in query_result:
        if unit_barcode not in skus_in_units:
            skus_in_units[unit_barcode] = []

        skus_in_units[unit_barcode].append({
            'sku_id': sku_id,
            'count': count
        })

    return skus_in_units
