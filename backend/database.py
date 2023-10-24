# database.py

from models import db, Login, Registration

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()