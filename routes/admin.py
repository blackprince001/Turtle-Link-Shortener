from fastapi import APIRouter, Depends
from schemas.user import AdminCreate
from utils.database_utils import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from turtle_link_shortener.models import User as UserModel, UserURL
from turtle_link_shortener.security import Password
from turtle_link_shortener.errors import UserNotFound

admin = APIRouter()


@admin.post("/admin/create", tags=["admins"])
async def create_admin(
    new_admin: AdminCreate, db: Session = Depends(get_db)
):
    db_admin = UserModel(**new_admin.dict())
    db_admin.password = Password.hash(db_admin.password)

    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)

    return db_admin


@admin.get("/admin/all_links", tags=["admins"])
async def get_all_links(db: Session = Depends(get_db)):
    return db.scalars(select(UserURL)).all()


@admin.get("/admin/{user_id}/links", tags=["admins"])
async def get_user_links(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(UserModel, user_id)

    if db_user is None:
        raise UserNotFound(status_code=404, detail=f"No user with id={user_id}")
        
    links = db.scalars(select(UserURL).where(UserURL.user_id == db_user.id)).all()

    return [link for link in links]
    