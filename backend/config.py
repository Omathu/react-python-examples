import os
import secrets

SECRET_KEY = secrets.token_hex(16)  # Generate a secure random secret key
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:omkar@localhost/testdb'
