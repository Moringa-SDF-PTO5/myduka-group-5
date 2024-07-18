from flask import request, jsonify, make_response,current_app as app
from app.models import User



@app.route('/')
def home():
    welcome_message = {'message': 'Welcome to the myduka inventory db.'}
    return make_response(jsonify(welcome_message), 200)


@app.route('/users', methods=['GET'])
def list_user():
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    return jsonify({
        "status": "success",
        "message": "success",
        "data": users_data
    }), 201


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')
    role = data.get('role')
    is_active = data.get('is_active')
    confirmed_admin = data.get('confirmed_admin')

    if not (
        user_id and username and email and password_hash and role and
        is_active and confirmed_admin
    ):
        return jsonify({
            "status": "Failed",
            "message": "Please provide all required fields.",
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
            "is_active": is_active,
            "confirmed_admin": confirmed_admin
        }
    }), 201
