from fastapi import APIRouter
router = APIRouter()

@router.get("/history/{user_id}")
async def getactivityhistory():
  pass

@router.post("/history/{user_id}")
async def postactivity():
  pass

@router.delete("/history/{user_id}")
async def clearactivityhistory():
  pass