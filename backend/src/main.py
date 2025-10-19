from fastapi import FastAPI
from api.api_router import api_router
import uvicorn

from database.models import Base, engine

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI()
app.add_event_handler("startup", create_tables)

app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
