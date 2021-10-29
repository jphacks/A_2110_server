from typing import Optional
import datetime

from pydantic import BaseModel, Field


    
class TrackData(BaseModel):
    date: datetime.datetime
    length: int =Field(None, example="秒で入れる")

class RecordData(BaseModel):
    start_date: datetime.datetime
    end_date: datetime.datetime

class Entry(BaseModel):
    data_type: str = Field(None, example="trackかrecordが入る")
    track_data: Optional[TrackData] = None
    record_data: Optional[RecordData] = None

class History(BaseModel):
    id: int
    userid: str
    entry: Entry
    
class ActivityCreate(Entry):
    pass

class ActivityCreateResponse(Entry):
    id: int
    userid: str
    class Config:
        orm_mode = True

