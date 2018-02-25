from flask import Flask
from app import config


app = Flask(__name__)
app.config.from_object(config.Config)
app.config['SECRET_KEY'] = "IT'S A SECRET TO EVERYBODY"

from app import routes
from app.database import db

db.create_all()
