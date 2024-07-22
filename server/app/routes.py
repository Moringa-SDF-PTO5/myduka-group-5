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


@app.route('/api/users', methods=['GET'])
def list_users():
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    return jsonify({
        "status": "success",
        "message": "Listed all Users",
        "data": users_data
    }), 200


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):

    user = User.query.get(user_id)
    if not user:
        return jsonify({
            "status": "Failed",
            "message": "User not found.",
            "data": None
        }), 404

    return jsonify({
        "status": "Success",
        "message": "User retrieved successfully.",
        "data": user.to_dict()
    }), 200


@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not all(key in data for key in ['username', 'email']):
        return jsonify({
            'status': 'Failed',
            'message': 'Username and email are required.',
            'data': None
        }), 400

    try:
        new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password_hash=data.get('password_hash', None),
            role=data.get('role', 'user'),
            is_active=data.get('is_active', True),
            confirmed_admin=data.get('confirmed_admin', False)
        )

        db.session.add(new_user)
        db.session.commit()

        response_data = {
            'status': 'Success',
            'message': 'User created successfully.',
            'data': new_user.to_dict()
        }
        print(response_data)

        return jsonify(response_data), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'status': 'Failed',
            'message': 'An error occurred while creating the user.',
            'data': None
        }), 500


@app.route('/api/users/<int:user_id>', methods=['PUT'])
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


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
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


@app.route('/api/invitations', methods=['GET'])
def list_invitations():
    invitations = Invitation.query.all()
    invitations_data = [invitation.to_dict() for invitation in invitations]
    return jsonify({
        "status": "success",
        "message": "listed all invitations",
        "data": invitations_data
    }), 200


@app.route('/api/invitations/<int:invitation_id>', methods=['GET'])
def get_invitation(invitation_id):
    # Retrieve the invitation by ID
    invitation = Invitation.query.get(invitation_id)
    if not invitation:
        return jsonify({
            "status": "Failed",
            "message": "Invitation not found.",
            "data": None
        }), 404

    return jsonify({
        "status": "Success",
        "message": "Invitation retrieved successfully.",
        "data": invitation.to_dict()
    }), 200


def get_current_utc():
    return datetime.now(timezone.utc)


@app.route('/api/invitations', methods=['POST'])
def create_invitation():
    data = request.get_json()
    email = data.get('email')
    user_id = data.get('user_id')

    if not email or not user_id:
        return jsonify({
            'status': 'Failed',
            'message': 'Missing required fields.',
            'data': None
        }), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({
            'status': 'Failed',
            'message': 'User not found.',
            'data': None
        }), 404

    token = str(uuid.uuid4())
    expiry_date = get_current_utc() + timedelta(hours=72)

    invitation = Invitation(
        token=token,
        email=email,
        user_id=user_id,
        expiry_date=expiry_date
    )

    try:
        db.session.add(invitation)
        db.session.commit()
        return jsonify({
            'status': 'Success',
            'message': 'Invitation created successfully.',
            'data': invitation.to_dict()
        }), 201
    except Exception:
        db.session.rollback()
        return jsonify({
            'status': 'Failed',
            'message': 'An error occurred while adding the invitation.',
            'data': 'An error occurred.'
        }), 500


@app.route('/api/invitations/<int:invitation_id>', methods=['DELETE'])
def delete_invitation(invitation_id):
    invitation = Invitation.query.get(invitation_id)

    if not invitation:
        return jsonify({
            'status': 'Failed',
            'message': 'Invitation not found.',
            'data': None
        }), 404

    try:
        db.session.delete(invitation)
        db.session.commit()

        return jsonify({
            'status': 'Success',
            'message': 'Invitation deleted successfully.',
            'data': None
        }), 200
    except Exception as e:
        db.session.rollback()

        return jsonify({
            'status': 'Failed',
            'message': 'An error occurred while deleting the invitation.',
            'data': str(e)
        }), 500


@app.route('/api/invitations/<int:invitation_id>', methods=['PUT'])
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
