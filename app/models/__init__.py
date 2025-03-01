from typing import Annotated
from sqlalchemy.orm import mapped_column

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[str, mapped_column(server_default='now()')]

# Import models after defining the types
from .products import ProductModel
from .users import UserModel, ReviewModel
from .orders import OrderModel, OrderItemsModel
from .carts import CartModel, CartItemsModel

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