from datetime import datetime
import uuid
from pydantic import BaseModel, EmailStr

class BaseUserSchema(BaseModel):
	email: EmailStr

class CreateUserSchema(BaseUserSchema):
	name: str
	password: str

class GetUserSchema(BaseUserSchema):
	id: uuid.UUID
	name: str
	created_at: datetime

class LoginUserSchema(BaseUserSchema):
	password: str

class TokenSchema(BaseModel):
	access: str | None = None
	refresh: str | None = None
	token_type: str | None = 'Bearer'