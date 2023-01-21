from pydantic import BaseModel


class UserURLBase(BaseModel):
    pass


class UserURLCreate(UserURLBase):
    pass


class UserURL(UserURLBase):
    
    class Config:
        orm_mode = True