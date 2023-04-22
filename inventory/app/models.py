from sqlalchemy import String, Integer, ForeignKey, ARRAY
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Tag(Base):
    __tablename__ = "tags"

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, nullable=False)


class Sku(Base):
    __tablename__ = "skus"

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String(255), nullable=False)
    tag_ids = mapped_column(ARRAY(Integer))


class Product(Base):
    __tablename__ = "products"

    id = mapped_column(Integer, primary_key=True, index=True)
    barcode = mapped_column(String(40), unique=True, nullable=False)
    unit_barcode = mapped_column(String(40))
    supply_id = mapped_column(Integer)
    stock_type = mapped_column(Integer, default=1)
    sku_id = mapped_column(Integer, ForeignKey("skus.id"))
