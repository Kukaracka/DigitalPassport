from database.models import UserModel
from schemas.user_schemas import UserCreateSchema, UserReadSchema
from utils.repository import SQLAlchemyRepository


class UserService:
    def __init__(self, users_repo: SQLAlchemyRepository[UserModel]):
        self.users_repo: SQLAlchemyRepository = users_repo()

    async def add_user(self, user: UserCreateSchema):
        users_dict = user.model_dump()
        user_id = await self.users_repo.create_one(users_dict)
        return user_id

    async def read_all_users(self) -> list[UserReadSchema]:
        user_data: list[UserModel] = await self.users_repo.read_all()
        users_schema = [UserReadSchema.from_orm(user) for user in user_data]
        return users_schema
