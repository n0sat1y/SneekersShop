from datetime import datetime
from typing import Annotated
from sqlalchemy import text, TIMESTAMP
from sqlalchemy.orm import mapped_column

# Определяем базовые типы
intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[
    datetime,
    mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("TIMEZONE('UTC', now())")
    )
]

# Сначала импортируем модели
from .products import ProductModel
from .users import UserModel, ReviewModel
from .orders import OrderModel, OrderItemsModel
from .carts import CartModel, CartItemsModel

# Потом объявляем что экспортировать
__all__ = [
    'ProductModel',
    'UserModel', 
    'ReviewModel',
    'CartModel',
    'CartItemsModel',
    'OrderModel',
    'OrderItemsModel',
]