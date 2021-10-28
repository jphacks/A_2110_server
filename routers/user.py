from fastapi import APIRouter
router = APIRouter()

@router.get("/user/{user_id}")
async def user_info():
  pass

@router.post("/user")
async def register_user():
  pass

@router.put("/user/{user_id}")
async def change_user_info():
  pass

@router.delete("/user/{user_id}")
async def clear_user_info():
  pass