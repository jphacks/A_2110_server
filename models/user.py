from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.traversals import ColIdentityComparatorStrategy

from db import Base

class Score(Base):
  __tablename__ = "score"
  user_id = Column(String(256), primary_key=True, nullable=False)
  exp: Column(Integer)
  times: Column(Integer)
  streak: Column(Integer)
  activity_length: Column(Integer)
