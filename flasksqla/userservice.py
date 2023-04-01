from typing_extensions import reveal_type
from flasksqla.baseorm import User
from flasksqla.extensions import db


def create_user(username: str):
    db.session.add(User(username=username))
    me = db.session.query(User).filter_by(username="xy").first()
    reveal_type(me)
    db.session.commit()
    
