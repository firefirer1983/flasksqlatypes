from baseorm import BaseModel
from flasksqla.extensions import db

class User(BaseModel):
    __tablename__ = "user"
    username: str = db.Column(db.String(32), comment="用户名")
