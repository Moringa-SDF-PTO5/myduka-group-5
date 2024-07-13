from flask import request, jsonify
from app import db
from app.models import User
from flask import current_app as app

@app.route('/users', methods=['GET'])
def list_user():
    users = User.query.all()
    users_data=[user.to_dict()for user in users]    
    return jsonify({
        "status":"success",
        "message":"success",
        "data":users_data
        
    }),201
    
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')
    role = data.get('role')
    confirmed_admin = data.get('confirmed_admin')
    
    if not (user_id and username and email and password_hash and role and confirmed_admin):
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
            "confirmed_admin": confirmed_admin
        }
    }), 201