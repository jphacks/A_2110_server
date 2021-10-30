from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from db import get_db
import schemas.user as user_schema
import CRUDs.user as user_crud
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

@router.get("/user/{user_id}/score", response_model=user_schema.Score)
async def addScore(user_id:str, db:AsyncSession = Depends(get_db)):
  return await user_crud.get_score(db,userid=user_id)

@router.post("/user/{user_id}/score", response_model=user_schema.ScoreDataCreateResponse)
async def addScore(user_id:str, score_body: user_schema.ScoreCreate, db:AsyncSession = Depends(get_db)):
  return await user_crud.init_score(db,user_id=user_id,**score_body.dict())

@router.put("/user/{user_id}/score")
async def addScore(user_id:str, score_body: user_schema.ScoreCreate):
  return user_schema.ScoreDataCreateResponse(userid=user_id, **score_body.dict())