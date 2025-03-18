from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app.models import intpk, uuidpk
from app.core.database import Base
import uuid

class CartModel(Base):
	__tablename__ = 'cart'

	id: Mapped[intpk]
	userId: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
	productId: Mapped[int] = mapped_column(ForeignKey('products.id', ondelete='CASCADE'))
	quantity: Mapped[int]
	color: Mapped[str]
	size: Mapped[int]

	user = relationship('UserModel', back_populates='cart')
	product = relationship('ProductModel', back_populates='cart')