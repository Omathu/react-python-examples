from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from models import db, Login, Registration, HelloTable
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)


app.config.from_pyfile('config.py')
db.init_app(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate
bcrypt = Bcrypt(app)

# Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']
    role = data.get('role', 'user')  # Default role is 'user'

    # Check if the username already exists
    existing_user = Registration.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'})

    # Hash the password before storing it in the Login table
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user in the Login table
    new_login = Login(username=username, password=hashed_password)
    db.session.add(new_login)
    
    # Create a new user in the Registration table with the role
    new_user = Registration(username=username, role=role, email=email)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'Registration successful'})

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = Login.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        # Get the user's role from the Registration table
        registration_data = Registration.query.filter_by(username=username).first()
        role = registration_data.role if registration_data else 'user'
        return jsonify({'message': 'Login successful', 'role': role})

    return jsonify({'message': 'Login failed'})

# API endpoint to get a message from the "Hello" table
@app.route('/api/message', methods=['GET'])
def get_hello_message():
    hello = HelloTable.query.first()
    if hello:
        message = hello.message
    else:
        message = "No message found in the 'Hello' table."
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run()