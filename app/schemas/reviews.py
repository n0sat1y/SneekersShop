from datetime import datetime
import uuid
from pydantic import BaseModel

class CreateReviewSchema(BaseModel):
	productId: int
	comment: str
	rating: int

class ReviewSchema(CreateReviewSchema):
	id: uuid.UUID
	userId: uuid.UUID
	createdAt: datetime
	userName: str