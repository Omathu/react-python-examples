# init_db.py

from app import app
from models import db

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
