from flask import request, jsonify, Blueprint
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

@main.route('/users', methods=['GET'])
def list_user():
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    return jsonify({
        "status": "ok",
        "message": "ok",
        "data": users_data
    }), 201

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')
    role = data.get('role')
    confirmed_admin = data.get('confirmed_admin')
    
    if not (user_id and username and email and password_hash and role and 
            confirmed_admin):
        return jsonify({
            "status": "Failed",
            "message": "All fields required.",
            "data": None
        }), 400

    return jsonify({
        "status": "Success",
        "message": "User created successfully.",
        "data": {
            "user_id": user_id,
            "username": username,
            "email": email,
            "role": role,
            "confirmed_admin": confirmed_admin
        }
    }), 201
