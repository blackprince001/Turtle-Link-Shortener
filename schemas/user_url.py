from pydantic import BaseModel
from datetime import datetime


class UserURLBase(BaseModel):
    pass


class UserURLCreate(UserURLBase):
    user_id: int
    link_created: str
    link_time_created: datetime


class UserURL(UserURLBase):
    
    class Config:
        orm_mode = True
        