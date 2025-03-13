from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from models import intpk, created_at
from core.database import Base


class OrderModel(Base):
	__tablename__ = 'orders'

	id: Mapped[intpk]
	userId: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
	totalPrice: Mapped[int]
	status: Mapped[str]
	created_at: Mapped[created_at]

	user = relationship('UserModel', back_populates='orders')
	order_items = relationship('OrderItemsModel', back_populates='order')

class OrderItemsModel(Base):
	__tablename__ = 'order_items'

	id: Mapped[intpk]
	orderId: Mapped[int] = mapped_column(ForeignKey('orders.id', ondelete='CASCADE'))
	productId: Mapped[int] = mapped_column(ForeignKey('products.id', ondelete='CASCADE'))
	quantity: Mapped[int]
	color: Mapped[str]
	size: Mapped[int]

	order = relationship('OrderModel', back_populates='order_items')
	product = relationship('ProductModel', back_populates='order_items')