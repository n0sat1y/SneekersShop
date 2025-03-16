from datetime import datetime
from typing import Annotated
import uuid
from sqlalchemy import text, TIMESTAMP, UUID
from sqlalchemy.orm import mapped_column

# Определяем базовые типы
intpk = Annotated[int, mapped_column(primary_key=True)]
uuidpk = Annotated[
    uuid.UUID,
    mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,  # Автоматическая генерация UUID
        unique=True,  # Гарантия уникальности
        nullable=False  # Поле не может быть NULL
    )
]
created_at = Annotated[
    datetime,
    mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("TIMEZONE('UTC', now())")
    )
]

# Сначала импортируем модели
from app.models.products import ProductModel
from app.models.users import UserModel, ReviewModel
from app.models.orders import OrderModel, OrderItemsModel
from app.models.carts import CartModel, CartItemsModel

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