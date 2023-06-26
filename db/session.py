from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from typing import Generator            #new

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)



def get_db() -> Generator:   #new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def commit_rollback():
    try:
        await get_db.commit()
    except Exception:
        await get_db.rollback()
        raise
db=SessionLocal()