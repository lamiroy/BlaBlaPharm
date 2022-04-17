from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class VI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base_verbal = db.Column(db.String(128))
    preterit = db.Column(db.String(128))
    past_participle = db.Column(db.String(128))
    trad = db.Column(db.String(256))

class Expressions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anglais = db.Column(db.String(256))
    francais = db.Column(db.String(256))

class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anglais = db.Column(db.String(256))
    francais = db.Column(db.String(256))

class Invoicing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anglais = db.Column(db.String(256))
    francais = db.Column(db.String(256))
    
class Ordering(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anglais = db.Column(db.String(256))
    francais = db.Column(db.String(256))
    
class Remuneration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anglais = db.Column(db.String(256))
    francais = db.Column(db.String(256))
    
class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anglais = db.Column(db.String(256))
    francais = db.Column(db.String(256))
    
class WorkEvents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anglais = db.Column(db.String(256))
    francais = db.Column(db.String(256))