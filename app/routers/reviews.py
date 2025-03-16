from fastapi import APIRouter, Depends, HTTPException

from app.routers.deps import token_dep
from app.core.database import SessionDep
from app.schemas import CreateReviewSchema, ReviewSchema
from app.repositories import ReviewRepository, UserRepository

router = APIRouter(tags=['Reviews'])

@router.post('/review')
async def create_review(
	session: SessionDep,
	review: CreateReviewSchema,
	user_id = Depends(token_dep)
) -> ReviewSchema:
	review = await ReviewRepository.create_review(session, review, user_id)
	user = await UserRepository.get_user_by_id(session, user_id)
	review_dict = review.__dict__
	review_schema = ReviewSchema(**review_dict, createdAt=review_dict['created_at'], userName=user.name)
	return review_schema

@router.get('/reviews')
async def get_reviews(
	session: SessionDep
):
	return await ReviewRepository.get_reviews(session)