from flask import make_response, request, jsonify, current_app as app
from .models import User
from app import db


@app.route('/')
def home():
    welcome_message = {'message': 'Welcome to the myduka inventory db.'}
    return make_response(jsonify(welcome_message), 200)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json('data')
    user_id = data.get_json('user_id')
    username = data.get_json('username')
    email = data.get_json('email')
    password_hash = data.get_json('password_hash')
    role = data.get_json('role')
    is_active = data.get_json('is_active')
    confirmed_admin = data.get_json('confirmed_admin')
    if not (data and user_id and username and email and password_hash and role and is_active
            and confirmed_admin):
        return jsonify({
            "status": "failed",
            "message": "all fields required",
            "data": "None"

        }), 403
    return jsonify({
        'status': 'success',
        'message': 'user created successfully',
        'data': {
            'user_id': user_id,
            'username': username,
            'email': email,
            'password_hash': password_hash,
            'role': role,
            'is_active': is_active,
            'confirmed_admin': confirmed_admin

        }
    }), 200
