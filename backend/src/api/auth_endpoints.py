from authx import AuthX, AuthXConfig
from fastapi import APIRouter, Response

from api.auth_key import SECRET_KEY
from repositories.user_repository import UserRepository
from schemas.user_schemas import (
    TokenResponseSchema,
    UserCreateSchema,
    UserLoginSchema,
    UserReadSchema,
)
from services.auth_service import AuthService

auth_router = APIRouter(prefix="", tags=["Auth"])

config = AuthXConfig()
config.JWT_SECRET_KEY = SECRET_KEY
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_COOKIE_CSRF_PROTECT = False


security = AuthX(config=config)


@auth_router.post("/login", response_model=TokenResponseSchema)
async def login(credentials: UserLoginSchema, responce: Response):
    auth_service = AuthService(UserRepository)
    token = await auth_service.authenticate_user(
        security=security, username=credentials.username, password=credentials.password
    )
    responce.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
    return {"access_token": token}


@auth_router.post("/register")
async def register(credentials: UserCreateSchema, responce: Response) -> UserReadSchema:
    service = AuthService(UserRepository)
    user = await service.registrate_user(credentials)
    return user
