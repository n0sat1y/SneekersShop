from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

from app.utils import validate_token_type, decode_jwt

bearer = HTTPBearer()

def token_dep(
		creds: HTTPAuthorizationCredentials = Depends(bearer)
		):
	try:
		decoded_token = decode_jwt(creds.credentials)
		token = validate_token_type(decoded_token, 'access')
		user_id = token.get('sub')
		if not user_id:
			raise HTTPException(status_code=401, detail='Invalid token')
		return user_id
	except jwt.exceptions.ExpiredSignatureError as e:
		raise HTTPException(status_code=401, detail='Token has expired')