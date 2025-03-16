import bcrypt
from fastapi import HTTPException, status
import jwt
from datetime import datetime, timedelta

from app.core.keys import public_key_obj, private_key_obj

def hash_password(password: str) -> bytes:
	salt = bcrypt.gensalt()
	pwd = bcrypt.hashpw(password.encode(), salt)
	return pwd

def validate_password(user_password: str, model_password: bytes) -> bool:
	return bcrypt.checkpw(user_password.encode(), model_password)


def encode_jwt(
		payload: dict, 
		type: str, 
		timedelta_minutes: int =0, 
		timedelta_days: int = 0,
		key: str = private_key_obj,
		algorithm: str = 'RS256',
	):
	payload['iat'] = datetime.utcnow()
	payload['exp'] = datetime.utcnow() + timedelta(minutes=timedelta_minutes, days=timedelta_days)
	payload['type'] = type
	
	token = jwt.encode(payload, key, algorithm)
	return token

def encode_access_jwt(
		payload: dict, 
		token_lifetime_minutes: int = 15
	):
	return encode_jwt(payload, 'access', timedelta_minutes=token_lifetime_minutes)

def encode_refresh_jwt(
		payload: dict,
		token_lifetime_days: int = 30
	):
	return encode_jwt(payload, 'refresh', timedelta_days=token_lifetime_days)

def decode_jwt(
		token: str,
		key: str = public_key_obj,
		algorithm: str = 'RS256'
		):
	data = jwt.decode(token, key, algorithms=[algorithm])
	return data

def validate_token_type(
		token: str | dict, 
		token_type_to_validate: str
	):
	if type(token) == str:
		token = decode_jwt(token)
	token_type = token.get('type')
	if token_type != token_type_to_validate:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token type')
	return token