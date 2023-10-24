# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Registration(db.Model):
    __tablename__ = 'registration'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False, default='default@example.com')
    role = db.Column(db.String(20), nullable=False)

class HelloTable(db.Model):
    __tablename__ = 'hello'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), unique=True, nullable=False)   

