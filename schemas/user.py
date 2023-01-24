from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    is_deleted: bool = False


class User(UserBase):

    class Config:
        orm_mode = True


class AdminCreate(UserCreate):
    is_admin: bool = True


class Admin(UserBase):

    class Config:
        orm_mode = True
        