from pydantic import BaseModel, EmailStr

class BaseUserSchema(BaseModel):
	email: EmailStr

class CreateUserSchema(BaseUserSchema):
	name: str
	password: str

class GetUserSchema(BaseUserSchema):
	id: int
	name: str

class LoginUserSchema(BaseUserSchema):
	password: str

class TokenSchema(BaseModel):
	access: str
	refresh: str
	token_type: str = 'Bearer'