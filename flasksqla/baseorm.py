from datetime import datetime
from typing import TypeVar, Type, TYPE_CHECKING
from typing_extensions import reveal_type

# from flask_sqlalchemy import BaseQuery
from flask_sqlalchemy.model import Model
from sqlalchemy.orm import declarative_base, sessionmaker, Session
# from flasksqla.extensions import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer
# M = TypeVar("M", bound="CompletionModel")

# __all__ = ["BaseModel"]

engine = create_engine("")
Session = sessionmaker(engine)
session = Session()
Model = declarative_base()

# class CompletionModel(Model):
#     @classmethod
#     def queryset(cls: Type[M]) -> BaseQuery[M]:
#         return cls.query


# if TYPE_CHECKING:
#     DeclarativeBase = declarative_base(CompletionModel)
# else:
#     DeclarativeBase


# class BaseMixin(Model):  # type: ignore[valid-type,misc]
#     __abstract__ = True

#     id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     create_time: datetime = db.Column(db.DateTime, default=datetime.now)  # 创建时间
#     update_time: datetime = db.Column(
#         db.DateTime, default=datetime.now, onupdate=datetime.now
#     )  # 更新时间


# class SoftDeleteMixin(Model):  # type: ignore[valid-type,misc]
#     __abstract__ = True
#     is_deleted = db.Column(
#         db.Boolean, default=False, server_default="0", nullable=False
#     )


# class BaseModel(BaseMixin, SoftDeleteMixin):
#     __abstract__ = True

    
class User(Model):
    __tablename__ = "user"
    id: int = Column(Integer, comment="主键")
    username: str = Column(String(32), comment="用户名")


user = session.query(User).filter(User.username == "xy").first()
reveal_type(user)
