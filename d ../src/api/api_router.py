from fastapi import APIRouter

from api import auth_endpoints, user_endpoints, debug_endpoints

api_router = APIRouter()
api_router.include_router(user_endpoints.user_router)
api_router.include_router(auth_endpoints.auth_router)
api_router.include_router(debug_endpoints.debug_router)
