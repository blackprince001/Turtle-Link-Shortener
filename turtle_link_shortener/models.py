from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base


class UserURL(Base):
    __tablename__ = "user_url"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True, nullable=False)
    link_created = Column(
        String, ForeignKey("url.custom_url"), primary_key=True, nullable=False
    )

    link_time_created = Column(DateTime, nullable=False)

    link_creator = relationship(
        "User", back_populates="links", lazy="selectin"
    )

    created_links = relationship(
        "URLS", back_populates="links_created", lazy="selectin"
    )


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, autoincrement=True)

    custom_url = Column(String, unique=True, nullable=False, index=True)
    secret_key = Column(String, unique=True, nullable=False, index=True)
    target_url = Column(String, nullable=False, index=True)

    is_active = Column(Boolean, default=True)
    time_created = Column(DateTime, nullable=False)
    clicks = Column(Integer, default=0)

    links_created: list[UserURL] = relationship(
        "UserURL", back_populates="created_links", lazy="selectin"
    )


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)

    links: list[UserURL] = relationship(
        "UserURL", back_populates="link_creator", lazy="selectin"
    )
