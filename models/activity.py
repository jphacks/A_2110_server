from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.sqltypes import Date, DateTime

from db import Base


class History(Base):
    __tablename__ = "histories"

    id = Column(Integer, primary_key=True)
    user_id= Column(String(1024))
    data_type= Column(String(32))
    track_date = Column(DateTime)
    track_length = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)