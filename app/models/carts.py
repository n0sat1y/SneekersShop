from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ARRAY, ForeignKey, String, Integer
from models import intpk, created_at
from core.batabase import Base


class CartModel(Base):
	__tablename__ = 'carts'

	id: Mapped[intpk]
	userId: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))

	user: Mapped[int] = relationship('UserModel', back_populates='cart')
	cart_items = relationship('CartItemsModel', back_populates='cart')

class CartItemsModel(Base):
	__tablename__ = 'cart_items'

	id: Mapped[intpk]
	cartId: Mapped[int] = mapped_column(ForeignKey('carts.id', ondelete='CASCADE'))
	productId: Mapped[int] = mapped_column(ForeignKey('products.id', ondelete='CASCADE'))
	quantity: Mapped[int]
	color: Mapped[str]
	size: Mapped[int]

	cart = relationship('CartModel', back_populates='cart_items')
	product = relationship('ProductModel', back_populates='cart_items')