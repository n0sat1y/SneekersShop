from datetime import datetime
from typing import Annotated
from sqlalchemy import text, DateTime, TIMESTAMP
from sqlalchemy.orm import mapped_column

__all__ = [
    'ProductModel',
    'UserModel', 
    'ReviewModel',
    'CartModel',
    'CartItemsModel',
    'OrderModel',
    'OrderItemsModel',
    'intpk',
    'created_at'
]

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[
    datetime,
    mapped_column(
        server_default=text("TIMEZONE('UTC', now())")
    )
]

# Import models after defining the types
from .products import ProductModel
from .users import UserModel, ReviewModel
from .orders import OrderModel, OrderItemsModel
from .carts import CartModel, CartItemsModel
