from config import settings
from sqlalchemy import func
from typing import Annotated
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url=settings.SQL_URL)
async_session = async_sessionmaker(engine)

created_at = Annotated[datetime, mapped_column(server_default=func.now())]


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
