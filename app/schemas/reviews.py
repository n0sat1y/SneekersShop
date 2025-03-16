from datetime import datetime
from pydantic import BaseModel

class CreateReviewSchema(BaseModel):
	productId: int
	comment: str
	rating: int

class ReviewSchema(CreateReviewSchema):
	id: int
	userId: int
	createdAt: datetime
	userName: str