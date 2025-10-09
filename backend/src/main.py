from fastapi import FastAPI
from backend.src.api.api_router import api_router
import uvicorn

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("backend.src.main:app", reload=True)
