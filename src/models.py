import datetime

from sqlalchemy import String, Date
from sqlalchemy.schema import Table
from sqlalchemy.orm import Mapped, mapped_column

from src.database import engine, Base

Base.prepare(autoload_with=engine)

# In case if we want create Model from DB

# class Question(Base):
#     __tablename__ = "question"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     text: Mapped[str] = mapped_column(String(256))
#     answer: Mapped[str] = mapped_column(String(256))
#     created_date: Mapped[datetime.date]

# In case if we create Model from existing DB
Question = Base.classes.question