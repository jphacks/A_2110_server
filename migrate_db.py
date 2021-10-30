from sqlalchemy import create_engine

from models.activity import Base as Base_activity
from models.user import Base as Base_user

DB_URL = "mysql+pymysql://root@db_server:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base_activity.metadata.drop_all(bind=engine)
    Base_activity.metadata.create_all(bind=engine)
    Base_user.metadata.drop_all(bind=engine)
    Base_user.metadata.create_all(bind=engine)
    


if __name__ == "__main__":
    reset_database()