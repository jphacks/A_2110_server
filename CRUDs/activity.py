from datetime import datetime
from typing import List, Optional, Tuple

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import query
from sqlalchemy.orm.attributes import History
from sqlalchemy.orm.query import Query
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.sqltypes import String
import models.activity as activity_model
import schemas.activity as activity_schema
from sqlalchemy import select
from sqlalchemy.engine import Result

async def create_entry(
    db: AsyncSession, user_id:str, activity_create: activity_schema.HistoryCreate
)-> activity_model.History:
    history = activity_model.History(**activity_create.dict())
    db.add(history)
    await db.commit()
    await db.refresh(history)
    return history

async def get_track_entry(db: AsyncSession)->List[Tuple[activity_model.History]]:
    result: Result = await (db.execute(
            select(
                ['*']
            ).where(activity_model.History.data_type == 'track')
        )
    )
    return result.all()

async def get_entry(db: AsyncSession, history_id: int) -> Optional[activity_model.History]:
    result: Result = await db.execute(
        select(activity_model.History).where(activity_model.History.id == history_id)
    )
    history: Optional[Tuple[activity_model.History]] = result.first()
    return history[0] if history is not None else None

async def delete_history(db:AsyncSession, orig:activity_model.History) -> None:
    await db.delete(orig)
    await db.commit()