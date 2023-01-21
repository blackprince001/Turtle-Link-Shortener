from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from . import database


class UserURLS(database.Base):
    __tablename__ = "user_url"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    link_created = Column(String, ForeignKey("url.key"), nullable=False)
    link_time_created = Column(DateTime, nullable=False)

    link_creator = database.relationship(
        "User", back_populates="links", lazy="selectin"
    )

    created_links = database.relationship(
        "URLS", back_populates="links_created", lazy="selectin"
    )


class URLS(database.Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True)

    key = Column(String, unique=True, nullable=False, index=True)
    secret_key = Column(String, unique=True, nullable=False, index=True)
    target_url = Column(String, nullable=False, index=True)

    is_active = Column(Boolean, default=True)
    time_created = Column(DateTime, nullable=False)
    clicks = Column(Integer, default=0)

    links_created: list[UserURLS] = database.relationship(
        "UserURLS", back_populates="created_links", lazy="selectin"
    )


class User(database.Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    links: list[UserURLS] = database.relationship(
        "UserURLS", back_populates="link_creator", lazy="selectin"
    )
