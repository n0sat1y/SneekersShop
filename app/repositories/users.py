from core.database import session
from models import UserModel
from schemas import *
from utils import hash_password, validate_password

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException


class UserRepository:
	@classmethod
	async def get_user_by_email(cls, session: AsyncSession, email: str):
		try:
			stmt = select(UserModel).where(UserModel.email == email)
			result = await session.execute(stmt)
			return result.scalar_one_or_none()
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))


	@classmethod
	async def get_user_by_id(cls, session: AsyncSession, id: int):
		try:
			stmt = select(UserModel).where(UserModel.id == id)
			result = await session.execute(stmt)
			return result.scalar_one_or_none()
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))


	@classmethod
	async def create_user(cls, session: AsyncSession, user: CreateUserSchema):
		try:
			user_dict = user.model_dump()
			user_dict['password'] = hash_password(user_dict['password'])
			user_model = UserModel(**user_dict)
			session.add(user_model)
			await session.flush()
			await session.commit()
			return user_model
		except Exception as e:
			raise HTTPException(status_code=500, detail=str(e))