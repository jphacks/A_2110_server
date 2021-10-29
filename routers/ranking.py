from typing import List
from fastapi import APIRouter
import schemas.ranking as ranking_schema
router = APIRouter()

@router.get('ranking', response_model=List[ranking_schema.Ranking])
async def get_ranking():
  return [ranking_schema.Ranking(userid=0,name="a",picture="null",)]
