from typing import Optional
import datetime

from pydantic import BaseModel, Field


class HistoryBase(BaseModel): 
    user_id:str = Field(None, title="user_id")
    data_type: str = Field(None, title="track or record")
    track_date: Optional[datetime.datetime]
    track_length: Optional[int]
    start_date: Optional[datetime.datetime]
    end_date: Optional[datetime.datetime]
    
class HistoryCreate(HistoryBase):
    pass

class HistoryCreateResponse(HistoryCreate):
    id: int = Field(None, title="id")
    class Config:
        orm_mode = True
        
class History(HistoryBase):
    id: int = Field(None, title="id")
    class Config:
        orm_mode = True