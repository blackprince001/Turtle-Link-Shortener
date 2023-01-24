from fastapi import APIRouter, Depends
from schemas.user import UserCreate
from utils.database_utils import get_db
from sqlalchemy.orm import Session
from turtle_link_shortener.models import User as UserModel

user = APIRouter()


@user.post("/user/create", tags=["users"])
async def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(**new_user.dict())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@user.get("/user/{user_id}", tags=["users"])
async def get_user(user_id: int, db: Session = Depends(get_db)):
    pass


@user.post("/user/{url}", tags=["users"])
async def shorten_link(url: str, custom_url: str, db: Session = Depends(get_db)):
    pass


@user.get("/user/{custom}", tags=["users"])
async def forward(custom_url: str, db: Session = Depends(get_db)):
    pass
