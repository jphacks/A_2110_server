from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from db import Base


class History(Base):
    __tablename__ = "histories"

    id = Column(Integer, primary_key=True)
    data_type= Column(String(32))
    track_length= Column(Integer)
    record_start_date=Column(DateTime)
    record_end_date=Column(DateTime)