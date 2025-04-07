from config import settings
from app.database.base import Base
from app.database.base import async_session
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BIGINT, String, Enum, ForeignKey, Boolean


# class Test(Base):
#     __tablename__ = 'tests'
#
#     id = mapped_column(BIGINT, primary_key=True)
#
#     @staticmethod
#     async def add_test(test_id: int) -> None:
#         async with async_session() as session:
#             test = await session.scalar(select(Test).where(Test.id == test_id))
#             if not test:
#                 session.add(test(id=test_id))
#                 await session.commit()
