from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from schemas.users import GetUserSchema
from schemas import CreateUserSchema, LoginUserSchema, TokenSchema
from repositories import UserRepository
from core.database import SessionDep
from utils import encode_access_jwt, encode_refresh_jwt, validate_password, decode_jwt, validate_token_type

router = APIRouter(tags=['Users'])

bearer = HTTPBearer()

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

@router.get('/users/me', response_model=GetUserSchema)
async def get_user(
	session: SessionDep,
	creds: HTTPAuthorizationCredentials = Depends(bearer)
):
	decoded_token = decode_jwt(creds.credentials)
	token = validate_token_type(decoded_token, 'access')
	user_id = token.get('sub')
	if not user_id:
		raise HTTPException(status_code=401, detail='Invalid token')
	user = await UserRepository.get_user_by_id(session, int(user_id))
	return GetUserSchema(**user.__dict__)