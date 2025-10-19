from abc import ABC, abstractmethod
from typing import Generic, Literal, Optional, TypeVar

from database.models import engine
from sqlalchemy import ClauseElement, asc, desc, insert, select
from sqlalchemy.ext.asyncio import async_sessionmaker

T = TypeVar("T")


class AbstractRepository(ABC, Generic[T]):
    @abstractmethod
    async def create_one() -> T:
        raise NotImplementedError

    @abstractmethod
    async def read_one() -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    async def read_all() -> list[T]:
        raise NotImplementedError

    # @abstractmethod
    # async def update_one():
    #     raise NotImplementedError

    # @abstractmethod
    # async def delete_one():
    #     raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository, Generic[T]):
    model: type[T]
    SessionLocal = async_sessionmaker(engine)

    async def create_one(self, data: dict) -> T:
        async with self.SessionLocal() as session:
            statement = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(statement)
            await session.commit()
            return res.scalar_one()

    async def read_all(
        self,
        filter_clause: Optional[ClauseElement] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        order_by: Optional[str] = None,
    ) -> list[T]:
        async with self.SessionLocal() as session:
            statement = select(self.model)

            if filter_clause is not None:
                statement = statement.where(filter_clause)

            if order and order_by:
                column = getattr(self.model, order_by, None)

                if column is None:
                    raise ValueError(f"Invalid order_by column: {order_by}")

                if order == "asc":
                    statement = statement.order_by(asc(column))
                if order == "desc":
                    statement = statement.order_by(desc(column))

            res = await session.execute(statement=statement)
            return res.scalars().all()

    async def read_one(self, id: Optional[int]) -> T | None:
        async with self.SessionLocal() as session:
            statement = select(self.model).where(self.model.id == id)
            res = await session.execute(statement=statement)
            return res.scalar_one_or_none()
