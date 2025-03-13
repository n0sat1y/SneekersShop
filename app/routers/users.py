from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

from schemas.users import GetUserSchema
from schemas import CreateUserSchema, LoginUserSchema, TokenSchema
from repositories import UserRepository
from core.database import SessionDep
from utils import encode_access_jwt, encode_refresh_jwt, validate_password, decode_jwt, validate_token_type

from .deps import token_dep, bearer

router = APIRouter(tags=['Users'])


@router.post('/create_user')
async def create_user(user: CreateUserSchema, session: SessionDep):
	if not await UserRepository.get_user_by_email(session, user.email):
		usr = await UserRepository.create_user(session, user)
		return {'user_id': usr.id}
	raise HTTPException(status_code=400, detail='User has already registered')

@router.post('/login_user', response_model=TokenSchema)
async def login_user(session: SessionDep, user: LoginUserSchema):
	exception = HTTPException(status_code=401, detail='Wrong email or password')
	usr = await UserRepository.get_user_by_email(session, user.email)
	if not usr:
		raise exception
	if not validate_password(user.password, usr.password):
		raise exception
	access = encode_access_jwt({'sub': str(usr.id)})
	refresh = encode_refresh_jwt({'sub': str(usr.id)})
	return TokenSchema(access=access, refresh=refresh)

@router.post('/refresh', response_model=TokenSchema, response_model_exclude_none=True)
async def get_access_from_refresh(creds: HTTPAuthorizationCredentials = Depends(bearer)):
	try:
		token = decode_jwt(creds.credentials)
		refresh = validate_token_type(token, 'refresh')
		payload = {'sub': refresh.get('sub')}
		access_token = encode_access_jwt(payload)
		return TokenSchema(access=access_token, token_type='Baerer')
	except jwt.ExpiredSignatureError:
		raise HTTPException(status_code=401, detail='Refresh token has expired')

@router.get('/users/me', response_model=GetUserSchema)
async def get_user(
	session: SessionDep,
	user_id = Depends(token_dep)
):
	user = await UserRepository.get_user_by_id(session, user_id)
	return GetUserSchema(**user.__dict__)