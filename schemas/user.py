from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):

    class Config:
        orm_mode = True


class AdminCreate(UserBase):
    is_admin: bool = True


class Admin(UserBase):

    class Config:
        orm_mode = True
        