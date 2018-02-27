#from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+app.config['DB_USERNAME']+':'+\
    app.config['DB_PASSWORD']+'@'+app.config['DB_ENDPOINT']+':'+\
    app.config['DB_PORT']+'/'+app.config['DB_NAME']

db = SQLAlchemy(app)

# A user is generally a physician who will be viewing the data of their patients
class Chip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chip_name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Chip %r>' % self.chip_name

class DataEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chip_id = db.Column(db.String(45), nullable=False)
    timestamp = db.Column(db.String(45), nullable=False)

    s0 = db.Column(db.Integer, nullable=False)
    s1 = db.Column(db.Integer, nullable=False)
    s2 = db.Column(db.Integer, nullable=False)
    s3 = db.Column(db.Integer, nullable=False)
    s4 = db.Column(db.Integer, nullable=False)
    s5 = db.Column(db.Integer, nullable=False)
    s6 = db.Column(db.Integer, nullable=False)
    s7 = db.Column(db.Integer, nullable=False)
    s8 = db.Column(db.Integer, nullable=False)
    s9 = db.Column(db.Integer, nullable=False)
    s10 = db.Column(db.Integer, nullable=False)
    s11 = db.Column(db.Integer, nullable=False)
    s12 = db.Column(db.Integer, nullable=False)
    s13 = db.Column(db.Integer, nullable=False)
    s14 = db.Column(db.Integer, nullable=False)
    s15 = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<{}:{}>'.format(self.chip_id, self.timestamp)

    def toJson(self):
        import json
        return json.dumps(self.toDict())
    
    def toDict(self):
        return {"t":self.timestamp,"v":[self.s0, self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, self.s8, self.s9, self.s10, self.s11, self.s12, self.s13, self.s14, self.s15]}
