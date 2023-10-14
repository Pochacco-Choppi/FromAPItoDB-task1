from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base, AutomapBase

from src.config import POSTGRES_USER, POSTGRES_PASSWORD, DATABASE_HOST, DATABASE_PORT

Base = automap_base()

SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}'
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
