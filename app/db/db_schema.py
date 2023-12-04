from db_base import Base

from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pydantic import HttpUrl

pkint = Annotated[int, mapped_column(primary_key=True)]

class ProductORM(Base):
    __tablename__ = "products"

    id: Mapped[pkint]
    title: Mapped[str]
    owner_id: Mapped[int]

    owner: Mapped["UserORM"] = relationship(back_populates="products")


class LessonORM(Base):

    __tablename__ = "lessons"

    id: Mapped[pkint]
    title: Mapped[str]
    lesson_url: Mapped[HttpUrl]
    viewing_time: Mapped[int]  # in seconds
    product_id: Mapped[int]


class UserORM(Base):

    __tablename__ = "users"

    id: Mapped[pkint]
    username: Mapped[str]

    products: Mapped[list['ProductORM']] = relationship(back_populates="owner")

