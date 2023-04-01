from datetime import datetime
from typing import TypeVar, Type, TYPE_CHECKING

from flask_sqlalchemy import BaseQuery
from flask_sqlalchemy.model import Model

from flasksqla.extensions import db

M = TypeVar("M", bound="CompletionModel")

__all__ = ["BaseModel"]


class CompletionModel(Model):
    @classmethod
    def queryset(cls: Type[M]) -> BaseQuery[M]:
        return cls.query


if TYPE_CHECKING:
    DeclarativeBase = db.make_declarative_base(CompletionModel)
else:
    DeclarativeBase


class BaseMixin(DeclarativeBase):  # type: ignore[valid-type,misc]
    __abstract__ = True

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time: datetime = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    update_time: datetime = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )  # 更新时间


class SoftDeleteMixin(DeclarativeBase):  # type: ignore[valid-type,misc]
    __abstract__ = True
    is_deleted = db.Column(
        db.Boolean, default=False, server_default="0", nullable=False
    )


class BaseModel(BaseMixin, SoftDeleteMixin):
    __abstract__ = True
