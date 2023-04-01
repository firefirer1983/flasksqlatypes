from flask import Flask
from dotenv import load_dotenv
load_dotenv(".env")

from flasksqla.extensions import create_app



app = create_app()
