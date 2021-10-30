from typing import Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select
from sqlalchemy.engine import Result

import models.user as user_model
import schemas.user as user_schema

async def init_score(
  db:AsyncSession, user_id:str, score_init: user_schema.ScoreCreate
)-> user_model.Score:
  score = user_model.Score(user_id=user_id, **score_init.dict())
  db.add(score)
  await db.commit()
  await db.refresh(score)
  return score

async def get_score(db:AsyncSession,user_id:str)-> Tuple[int,int,int,int]:
  result: Result = await(
    db.execute(
      select(
        user_model.Score.exp,
        user_model.Score.streak,
        user_model.Score.times,
        user_model.Score.activity_length
      ).where(user_model.Score.user_id == user_id)
    )
  )