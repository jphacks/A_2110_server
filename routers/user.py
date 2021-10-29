from fastapi import APIRouter
import schemas.user as user_schema
router = APIRouter()

@router.get("/user/{user_id}",response_model=user_schema.Userdata)
async def user_info():
  return user_schema.Userdata()

@router.post("/user")
async def register_user():
  pass

@router.put("/user/{user_id}")
async def change_user_info():
  pass

@router.delete("/user/{user_id}")
async def clear_user_info():
  pass