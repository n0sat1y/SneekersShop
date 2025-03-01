from core.batabase import Base
from models import *

from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey


class UserModel(Base):
	__tablename__ = 'users'

	id: Mapped[intpk]
	name: Mapped[str]
	email: Mapped[str]
	password: Mapped[bytes]
	created_at: Mapped[created_at]

	reviews: Mapped[list["ReviewModel"]] = relationship('ReviewModel', back_populates='user')
	orders: Mapped[list["OrderModel"]] = relationship('OrderModel', back_populates='user')
	cart: Mapped["CartModel"] = relationship('CartModel', back_populates='user')


class ReviewModel(Base):
	__tablename__ = 'reviews'

	id: Mapped[intpk]
	rating: Mapped[int]
	comment: Mapped[str]
	created_at: Mapped[created_at]
	userId: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
	productId: Mapped[int] = mapped_column(ForeignKey('products.id', ondelete='CASCADE'))

	user: Mapped['UserModel'] = relationship('UserModel', back_populates='reviews')
	product: Mapped['ProductModel'] = relationship('ProductModel', back_populates='reviews')