from fastapi import APIRouter
from controllers.users_controller import create_user, get_user, update_user, delete_user
from schemas.users_schema import UserSchema

router = APIRouter()

@router.post("/users/")
async def create_user_route(user: UserSchema):
    return await create_user(user.dict())

@router.get("/users/{user_id}")
async def get_user_route(user_id: str):
    return await get_user(user_id)

@router.put("/users/{user_id}")
async def update_user_route(user_id: str, user: UserSchema):
    return await update_user(user_id, user.dict())

@router.delete("/users/{user_id}")
async def delete_user_route(user_id: str):
    return await delete_user(user_id)
