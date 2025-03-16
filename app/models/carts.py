from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from models import intpk, uuidpk
from core.database import Base
import uuid


class CartModel(Base):
	__tablename__ = 'carts'

	id: Mapped[uuidpk]
	userId: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))

	user: Mapped[uuid.UUID] = relationship('UserModel', back_populates='cart')
	cart_items = relationship('CartItemsModel', back_populates='cart')

class CartItemsModel(Base):
	__tablename__ = 'cart_items'

	id: Mapped[intpk]
	cartId: Mapped[uuid.UUID] = mapped_column(ForeignKey('carts.id', ondelete='CASCADE'))
	productId: Mapped[int] = mapped_column(ForeignKey('products.id', ondelete='CASCADE'))
	quantity: Mapped[int]
	color: Mapped[str]
	size: Mapped[int]

	cart = relationship('CartModel', back_populates='cart_items')
	product = relationship('ProductModel', back_populates='cart_items')