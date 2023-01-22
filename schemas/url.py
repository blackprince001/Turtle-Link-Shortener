from pydantic import BaseModel
from datetime import datetime


class URLBase(BaseModel):
    target_url: str


class URL(URLBase):
    is_active: bool
    time_created: datetime
    clicks: int

    class Config:
        orm_mode = True


class URLInfo(URL):
    custom_url: str
    admin_url: str
    