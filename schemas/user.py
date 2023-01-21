from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    pass


class User(UserBase):

    class Config:
        orm_mode = True


class AdminCreate(UserBase):
    pass


class Admin(UserBase):

    class Config:
        orm_mode = True