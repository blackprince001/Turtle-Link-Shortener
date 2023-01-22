from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from .config import get_settings

Base = declarative_base()

engine = create_engine(
    get_settings().db_url, connect_args={"check_same_thread": False}
)
