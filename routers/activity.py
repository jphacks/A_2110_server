from typing import List
from fastapi import APIRouter
import schemas.activity as activity_schema
router = APIRouter()

@router.get("/history/{user_id}", response_model=List[activity_schema.History])
async def getactivityhistory():
  return [activity_schema.History(id=1, data_type = "track")]

@router.post("/history/{user_id}", response_model=activity_schema.ActivityCreateResponse)
async def postactivity(activity_entry: activity_schema.ActivityCreate):
  return activity_schema.ActivityCreateResponse(id=1, **activity_entry.dict())

@router.delete("/history/{user_id}")
async def clearactivityhistory():
  pass