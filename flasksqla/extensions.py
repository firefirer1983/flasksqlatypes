from flask_sqlalchemy import SQLAlchemy
from flask import Flask
db = SQLAlchemy()


def create_app() -> Flask:
    flsk = Flask(__name__)
    db.init_app(flsk)
    return flsk
