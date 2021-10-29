from sqlalchemy.engine import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

ASYNC_DB_URL = "mysql+aiomysql://root@db_server:3306/demo?charset=utf8"
DB_URL = "mysql+pymysql://root@db_server:3306/demo?charset=utf8"
engine = create_engine(DB_URL)
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()

def session_normal():
    db = None
    try:
        db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        yield db
    finally:
        db.close()

async def get_db():
    async with async_session() as session:
        yield session