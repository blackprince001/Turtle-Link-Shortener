from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from schemas.user import UserCreate
from schemas.url import URLBase
from utils.database_utils import get_db
from utils.router_utils import generate_keys
from sqlalchemy.orm import Session
from sqlalchemy import select
from turtle_link_shortener.models import User as UserModel, URL as URLModel, UserURL
from turtle_link_shortener.security import Password
from turtle_link_shortener.errors import UserNotFound, URLNotValid, URLForwardError
from pydantic import HttpUrl
from datetime import datetime

user = APIRouter()


@user.post("/user/create", tags=["users"])
async def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(**new_user.dict())
    db_user.password = Password.hash(db_user.password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@user.get("/user/{user_id}", tags=["users"])
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(UserModel, user_id)
    if db_user is None:
        raise UserNotFound(status_code=404, detail=f"No user with id={user_id}")
    return db_user


@user.post("/user/{user_id}/shorten", tags=["users"])
async def shorten_link(
    url: URLBase, user_id: int, custom_key: str, db: Session = Depends(get_db)
):
    if not HttpUrl(url=url.target_url):
        raise URLNotValid(status_code=400, detail="Your provided URL is not valid")

    if db.get(UserModel, user_id) is None:
        raise UserNotFound(status_code=404, 
                detail=f"No user with id={user_id}. Cannot proceed with user_auth!")

    # set the characters to be used for tokenization
    key, secret_key = generate_keys(custom_key)
    now = datetime.now()

    # add the generated data to URL Model Table
    db_url = URLModel(target_url=url.target_url, custom_url=key, 
                      secret_key=secret_key, time_created=now)

    db_user_url = UserURL(user_id=user_id, link_created=key, link_time_created=now)

    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    db.add(db_user_url)
    db.commit()
    db.refresh(db_user_url)

    db_url.custom_url = key
    db_url.admin_url = secret_key

    return db_url


@user.get("/user/{custom_url}", tags=["users"])
async def forward(custom_url: str, db: Session = Depends(get_db)):
    query = (
            select(URLModel.target_url)
            .where(URLModel.custom_url == custom_url)
            .where(URLModel.is_active == True)
        )

    url = db.scalar(query)

    if url is not None:
        url.clicks += 1
        db.commit()
        db.refresh(url)
        
        return RedirectResponse(url.target_url, status_code=307)
    else:
        raise URLForwardError(status_code=404, 
                detail=f"Bad Request. {custom_url} not linked to any valid url!")


@user.get("/user/{user_id}/links", tags=["users"])
async def get_links(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(UserURL, user_id)
    
    if db_user is None:
        raise UserNotFound(status_code=404, detail=f"No user with id={user_id}!")

    return db.scalars(select(UserURL).where(UserURL.user_id == db_user.id)).all()