from fastapi import APIRouter
from backend.src.api.users_endpoints import user_router

api_router = APIRouter()
api_router.include_router(user_router)
# TODO: include api_router
