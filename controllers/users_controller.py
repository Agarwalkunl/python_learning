from fastapi.responses import JSONResponse
from db import get_database

db = get_database()

async def create_user(user_data: dict):
    collection = db["users"]
    result = await collection.insert_one(user_data)
    return JSONResponse(status_code=201, content={"message": "User created", "id": str(result.inserted_id)})

async def get_user(user_id: str):
    collection = db["users"]
    user = await collection.find_one({"_id": user_id})
    if user is None:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    return user

async def update_user(user_id: str, user_data: dict):
    collection = db["users"]
    result = await collection.update_one({"_id": user_id}, {"$set": user_data})
    if result.matched_count == 0:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    return JSONResponse(status_code=200, content={"message": "User updated"})

async def delete_user(user_id: str):
    collection = db["users"]
    result = await collection.delete_one({"_id": user_id})
    if result.deleted_count == 0:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    return JSONResponse(status_code=200, content={"message": "User deleted"})
