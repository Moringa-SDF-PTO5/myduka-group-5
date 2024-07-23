# app/models.py
from app import db
from datetime import datetime, timezone


def get_current_utc():
    return datetime.now(timezone.utc)


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True)
    confirmed_admin = db.Column(db.Boolean, default=False)

    # Define the relationship
    invitations = db.relationship('Invitation', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'role': self.role,
            'is_active': self.is_active,
            'confirmed_admin': self.confirmed_admin
        }


class Invitation(db.Model):
    __tablename__ = 'invitations'
    Invitation_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=get_current_utc, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    is_used = db.Column(db.String(1), nullable=False, default='0')

    # Foreign key relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __init__(self, token, email, expiry_date, user_id, is_used='0'):
        self.token = token
        self.email = email
        self.expiry_date = expiry_date
        self.user_id = user_id
        self.is_used = is_used

    def __repr__(self):
        return f'<Invitation {self.Invitation_id}>'

    def to_dict(self):
        return {
            'Invitation_id': self.Invitation_id,
            'token': self.token,
            'email': self.email,
            'created_at': self.created_at,
            'expiry_date': self.expiry_date,
            'is_used': self.is_used,
            'user_id': self.user_id
        }
