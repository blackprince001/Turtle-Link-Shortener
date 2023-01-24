from fastapi import APIRouter, Depends
from schemas.user import AdminCreate
from utils.database_utils import get_db
from sqlalchemy.orm import Session
from turtle_link_shortener.models import User as UserModel
from turtle_link_shortener.security import Password

admin = APIRouter()


@admin.post("/admin/create", tags=["admin"])
async def create_admin(
    new_admin: AdminCreate, db: Session = Depends(get_db)
):
    db_admin = UserModel(**new_admin.dict())
    db_admin.password = Password.hash(db_admin.password)

    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)

    return db_admin
