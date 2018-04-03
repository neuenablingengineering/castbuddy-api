from flask import Flask
from app import config
from flask_cors import CORS

app = Flask(__name__)

# Database Config
app.config.from_object(config.Config)
app.config['SECRET_KEY'] = "IT'S A SECRET TO EVERYBODY"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, resources={"/api/*": {"origins": "*"}})

from app import routes
from app.database import db

db.create_all()
