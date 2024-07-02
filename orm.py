from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List

class Base(DeclarativeBase):
    pass

product_shop_table = Table(
    "product_shop",
    Base.metadata,
    Column("product_id", ForeignKey("products.id")),
    Column("shop_id", ForeignKey("shops.id")),
)

branded_product_shop_table = Table(
    "branded_product_shop",
    Base.metadata,
    Column("branded_product_id", ForeignKey("branded_products.id")),
    Column("shop_id", ForeignKey("shops.id")),
)


class Shop(Base):
    __tablename__ = "shops"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    unit: Mapped[str] = mapped_column(String(100))
    brands: Mapped[List["BrandedProduct"]] = relationship(back_populates="product")
    shops: Mapped[List["Shop"]] = relationship(secondary=product_shop_table)

class BrandedProduct(Base):
    __tablename__ = "branded_products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id")) 
    product: Mapped["Product"] = relationship(back_populates="brands")
    shops: Mapped[List["Shop"]] = relationship(secondary=branded_product_shop_table)


class StorageEntry(Base):
    __tablename__ = "storage_entries"
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    storage_id: Mapped[int] = mapped_column(ForeignKey("storages.id"), primary_key=True)
    product: Mapped["Product"] = relationship()
    storage: Mapped["Storage"] = relationship(back_populates="entries")
    quantity: Mapped[int] = mapped_column()

class Storage(Base):
    __tablename__ = "storages"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    entries: Mapped[List["StorageEntry"]] = relationship(back_populates="storage")

class ShoppingEntry(Base):
    __tablename__ = "shopping_entries"
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    shopping_list_id: Mapped[int] = mapped_column(ForeignKey("shopping_lists.id"), primary_key=True)
    shopping_list: Mapped["ShoppingList"] = relationship(back_populates="entries")
    quantity: Mapped[int] = mapped_column()
    replacement: Mapped[bool] = mapped_column()

class ShoppingList(Base):
    __tablename__ = "shopping_lists"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    entries: Mapped[List["ShoppingEntry"]] = relationship(back_populates="shopping_list")

