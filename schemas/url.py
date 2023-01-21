from pydantic import BaseModel


class URLBase(BaseModel):
    pass


class URLShortener(URLBase):
    pass


class URL(URLBase):

    class Config:
        orm_mode = True