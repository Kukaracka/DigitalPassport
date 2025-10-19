from sqlalchemy import select
from database.models import UserModel
from utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository[UserModel]):
    model = UserModel

    async def get_by_username(self, username: str) -> UserModel | None:
        async with self.SessionLocal() as session:
            statement = select(UserModel).where(UserModel.username == username)
            result = await session.execute(statement=statement)
            return result.scalar_one_or_none()
