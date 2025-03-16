from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ARRAY, String, Integer
from typing import Optional
from app.core.database import Base
from app.models import intpk


class ProductModel(Base):
    __tablename__ = 'products'

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]
    colors: Mapped[list[str]] = mapped_column(ARRAY(String))
    category: Mapped[str]
    gender: Mapped[str]
    sizes: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    price: Mapped[int]
    # relationships
    cart_items = relationship('CartItemsModel', back_populates='product')
    reviews = relationship('ReviewModel', back_populates='product')
    order_items = relationship('OrderItemsModel', back_populates='product')