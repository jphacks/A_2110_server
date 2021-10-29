from typing import Optional
import datetime
from schemas.user import Score
from pydantic import BaseModel, Field

class Ranking(BaseModel):
  userid: str
  name: str
  picture: str
  twitter: Optional[str] =None
  instagram: Optional[str] = None
  score: Score
  