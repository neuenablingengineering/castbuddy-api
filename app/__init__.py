from flask import Flask
from flask_pusher import Pusher
from app import config
from flask_cors import CORS


app = Flask(__name__)
# Database Config
app.config.from_object(config.Config)
app.config['SECRET_KEY'] = "IT'S A SECRET TO EVERYBODY"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Pusher Configs
import pusher

pusher_client = pusher.Pusher(
  app_id='500492',
  key='fa3a35c5896c472fb7e0',
  secret='df50b6b9c3cd59b66a87',
  cluster='us2',
  ssl=True
)
cors = CORS(app, resources={"/api/*": {"origins": "*"}})

from app import routes
from app.database import db

db.create_all()
