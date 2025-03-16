from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from models import ReviewModel
from schemas import CreateReviewSchema


class ReviewRepository:
	@classmethod
	async def create_review(cls, 
		session: AsyncSession, 
		review: CreateReviewSchema, 
		user_id: int
	) -> ReviewModel:
		try:
			review_dict = review.model_dump()
			review_model = ReviewModel(**review_dict, userId=user_id)
			session.add(review_model)
			await session.commit()
			await session.refresh(review_model)
			return review_model
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))
	
	@classmethod
	async def get_reviews(cls, session: AsyncSession):
		result = await session.execute(select(ReviewModel))
		return result.scalars().all()