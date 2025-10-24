from authx import AuthX, AuthXConfig
from authx.exceptions import JWTDecodeError
from fastapi import Depends, HTTPException, Request

from api.auth_key import SECRET_KEY
from repositories.user_repository import UserRepository

config = AuthXConfig()
config.JWT_SECRET_KEY = SECRET_KEY
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_COOKIE_CSRF_PROTECT = False


security = AuthX(config=config)


async def verify_token(request: Request):
    try:
        result = await security.access_token_required(request)
        return result
    except JWTDecodeError as e:
        if "expired" in str(e).lower():
            raise HTTPException(status_code=401, detail="Token has expired")
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        print(f"Other auth error: {e}")  # Отладочная информация
        raise HTTPException(status_code=401, detail="Authentication failed")


async def get_current_authorised_user(
    payload: dict = Depends(verify_token),
):
    user_id = int(payload.sub)

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user = await UserRepository().read_one(user_id)
    return user
