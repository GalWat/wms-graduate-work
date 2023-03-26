from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id = mapped_column(Integer, primary_key=True, index=True)
    status = mapped_column(Integer, nullable=False)


class Sku(Base):
    __tablename__ = "needed_skus"

    id = mapped_column(Integer, primary_key=True, index=True)
    task_id = mapped_column(Integer, ForeignKey("tasks.id"))
    sku_id = mapped_column(Integer, nullable=False)
    count = mapped_column(Integer, nullable=False)


class Product(Base):
    __tablename__ = "picked_products"

    id = mapped_column(Integer, primary_key=True, index=True)
    task_id = mapped_column(Integer, ForeignKey("tasks.id"))
    product_barcode = mapped_column(String(40), nullable=False)
    sku_id = mapped_column(Integer, nullable=False)
