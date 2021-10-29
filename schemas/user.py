from typing import Optional
import datetime

from pydantic import BaseModel, Field

class Score(BaseModel):
  exp: int = Field(None, example="経験値")
  times:int = Field(None, example="運動回数")
  streak: int = Field(None, example="運動継続日数")
  activity_length: int = Field(None, example="累計運動時間")
  
class Deadzone(BaseModel):
  x: float = 2
  y: float = 2
  z: float = 2

class Settings(BaseModel):
  deadzone_sensor :Deadzone
  vacation_mode : bool = False
  debug_user : bool = False
  twitter : Optional[str]
  instagram : Optional[str]
  
class Userdata(BaseModel):
  userid: str
  name: str
  email: str
  picture: str
  settings: Settings
  score: Score
  
