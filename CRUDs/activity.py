from sqlalchemy.ext.asyncio import AsyncSession

import models.activity as activity_model
import schemas.activity as activity_schema

async def create_task(
    db: AsyncSession, activity_create: activity_schema.ActivityCreateResponse
) -> activity_model.Task:
    history = activity_model.History(**activity_schema.dict())
    db.add(history)
    await db.commit()
    await db.refresh(history)
    return history