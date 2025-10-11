from fastapi import APIRouter

user_router = APIRouter(
        prefix="/users",
        tags=["users"]
        )


# TODO: pydantic schema
@user_router.post("/",
        response_description="New user has been created",
        tags=["users"],)
async def create_user(user): # TODO: pydantic schema
    return {"user_id": "Moc responce"}


@user_router.get("/",
                 response_description="List of users retrieved seccessfully",
                 tags=["users"])
async def read_users(): # TODO: add pydantic schema 
    user_data = "Moc responce"
    return user_data


@user_router.delete("/",
                    response_description="User has been deleted")
async def detele_user(user_id):
    # TODO: delete logic  
    return {"user_id": user_id,
            "deleted": True}


@user_router.patch("/",
                   response_description="User has been updated")
async def update_user(user_id, data):
    # TODO: update logic
    return {"user_id": user_id,
            "updated": True}
