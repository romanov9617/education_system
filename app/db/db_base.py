from config import settings

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    settings.DB_URL
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False
)
