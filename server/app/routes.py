# app/routes.py
from flask import request, jsonify, make_response, current_app as app
from app import db
from app.models import User, Invitation
import uuid
from datetime import datetime, timedelta, timezone


@app.route('/')
def home():
    welcome_message = {'message': 'Welcome to the myduka inventory db.'}
    return make_response(jsonify(welcome_message), 200)

# User routes


@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    return jsonify({
        "status": "success",
        "message": "success",
        "data": users_data
    }), 200


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')
    role = data.get('role')
    is_active = data.get('is_active')
    confirmed_admin = data.get('confirmed_admin')

    if not (
        username and email and password_hash and role and
        is_active is not None and confirmed_admin is not None
    ):
        return jsonify({
            "status": "Failed",
            "message": "Please provide all required fields.",
            "data": None
        }), 400

    new_user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role=role,
        is_active=is_active,
        confirmed_admin=confirmed_admin
    )

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "status": "Failed",
            "message": "An error occurred while adding the user.",
            "data": str(e)
        }), 500

    return jsonify({
        "status": "Success",
        "message": "User created successfully.",
        "data": new_user.to_dict()
    }), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({
            "status": "Failed",
            "message": "User not found.",
            "data": None
        }), 404

    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password_hash = data.get('password_hash', user.password_hash)
    user.role = data.get('role', user.role)
    user.is_active = data.get('is_active', user.is_active)
    user.confirmed_admin = data.get('confirmed_admin', user.confirmed_admin)

    db.session.commit()
    return jsonify({
        "status": "Success",
        "message": "User updated successfully.",
        "data": user.to_dict()
    }), 200


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({
            "status": "Failed",
            "message": "User not found.",
            "data": None
        }), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "User deleted successfully.",
        "data": None
    }), 200

# Invitation routes


@app.route('/invitations', methods=['GET'])
def get_invitations():
    invitations = Invitation.query.all()
    return jsonify([invitation.to_dict() for invitation in invitations])


@app.route('/invitations/<int:invitation_id>', methods=['GET'])
def get_invitation(invitation_id):
    invitation = Invitation.query.get_or_404(invitation_id)
    return jsonify(invitation.to_dict())


@app.route('/invitations', methods=['POST'])
def create_invitation():
    data = request.get_json()
    email = data.get('email')
    user_id = data.get('user_id')

    if not email or not user_id:
        return jsonify({
            "status": "Failed",
            "message": "Email and user_id are required.",
            "data": None
        }), 400

    token = str(uuid.uuid4())
    expiry_date = datetime.now(timezone.utc) + timedelta(days=7)

    new_invitation = Invitation(
        token=token,
        email=email,
        expiry_date=expiry_date,
        user_id=user_id
    )

    try:
        db.session.add(new_invitation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "status": "Failed",
            "message": "An error occurred while adding the invitation.",
            "data": str(e)
        }), 500

    return jsonify({
        "status": "Success",
        "message": "Invitation created successfully.",
        "data": new_invitation.to_dict()
    }), 201


@app.route('/invitations/<int:invitation_id>', methods=['PUT'])
def update_invitation(invitation_id):
    invitation = Invitation.query.get(invitation_id)
    if not invitation:
        return jsonify({
            "status": "Failed",
            "message": "Invitation not found.",
            "data": None
        }), 404

    data = request.get_json()
    invitation.token = data.get('token', invitation.token)
    invitation.email = data.get('email', invitation.email)
    invitation.expiry_date = data.get('expiry_date', invitation.expiry_date)
    invitation.is_used = data.get('is_used', invitation.is_used)

    db.session.commit()
    return jsonify({
        "status": "Success",
        "message": "Invitation updated successfully.",
        "data": invitation.to_dict()
    }), 200


@app.route('/invitations/<int:invitation_id>', methods=['DELETE'])
def delete_invitation(invitation_id):
    invitation = Invitation.query.get(invitation_id)
    if not invitation:
        return jsonify({
            "status": "Failed",
            "message": "Invitation not found.",
            "data": None
        }), 404

    db.session.delete(invitation)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "Invitation deleted successfully.",
        "data": None
    }), 200
