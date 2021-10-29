from typing import Optional
import datetime

from pydantic import BaseModel, Field

class Entry(BaseModel):
    id: int

    
class TrackData(BaseModel):
    date: datetime.datetime
    length: int =Field(None, example="秒で入れる")

class RecordData(BaseModel):
    start_date: datetime.datetime
    end_date: datetime.datetime

class History(BaseModel):
    id: int
    userid: str
    data_type: str = Field(None, example="trackかrecordが入る")
    track_data: Optional[TrackData] = None
    record_data: Optional[RecordData] = None

