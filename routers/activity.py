from typing import List
from fastapi import APIRouter
from fastapi.params import Depends

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.session import Session
from db import get_db, session_normal
import CRUDs.activity as activity_crud
import schemas.activity as activity_schema
router = APIRouter()

@router.get("/history/{user_id}/track", response_model=List[activity_schema.History])
async def getactivityhistory(user_id:str,db: AsyncSession = Depends(get_db)):
  return await activity_crud.get_track_entry(db, user_id)

@router.get("/history/{user_id}/record", response_model=List[activity_schema.History])
async def getactivityhistory(user_id:str,db: AsyncSession = Depends(get_db)):
  return await activity_crud.get_record_entry(db, user_id)

@router.get("/history/", response_model=List[activity_schema.History])
async def getallhistory_debug(db: AsyncSession = Depends(get_db)):
  return await activity_crud.get_all_entry(db)

@router.post("/history/{user_id}", response_model=activity_schema.HistoryCreateResponse)
async def postactivity(user_id:str,activity_entry: activity_schema.HistoryCreate, db: AsyncSession = Depends(get_db)):
  return await activity_crud.create_entry(db,user_id,activity_entry)

@router.delete("/history/{user_id}/{history_id}", response_model=None)
async def clearactivityhistory(user_id:str,history_id: int,db:AsyncSession = Depends(get_db)):
  entry = await activity_crud.get_entry(db, history_id=history_id)
  if entry is None:
    return "error"
  return await activity_crud.delete_history(db,orig=entry)