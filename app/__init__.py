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
app.config['PUSHER_APP_ID'] = '500492'
app.config['PUSHER_KEY'] = 'fa3a35c5896c472fb7e0'
app.config['PUSHER_SECRET'] = 'df50b6b9c3cd59b66a87'
app.config['PUSHER_CLUSTER'] = 'us2'
app.config['PUSHER_SSL'] = True


pusher = Pusher(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from app import routes
from app.database import db

db.create_all()
