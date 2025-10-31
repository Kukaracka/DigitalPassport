from authx import AuthX
from fastapi import HTTPException, security

from schemas.user_schemas import UserCreateSchema, UserReadSchema
from utils.repository import SQLAlchemyRepository


class AuthService:
    def __init__(self, users_repo_cls: SQLAlchemyRepository):
        self.users_repo: SQLAlchemyRepository = users_repo_cls()
        self.security = security

    async def authenticate_user(
        self, security: AuthX, username: str, password: str
    ) -> str:
        user = await self.users_repo.get_by_username(username)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid username")

        if user.password != password:
            raise HTTPException(status_code=401, detail="Invalid password")

        token = security.create_access_token(uid=str(user.id))
        return token

    async def registrate_user(self, user_data: UserCreateSchema) -> UserReadSchema:
        existing_user = await self.users_repo.get_by_username(user_data.username)
        if existing_user:
            raise HTTPException(
                status_code=409, detail="User with this username already exists"
            )

        user_dict = user_data.model_dump()
        user_id = await self.users_repo.create_one(user_dict)

        user = await self.users_repo.read_one(user_id)
        return UserReadSchema.from_orm(user)
