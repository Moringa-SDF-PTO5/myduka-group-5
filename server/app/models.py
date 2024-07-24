from app import db
from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import relationship


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
    # Changed to lowercase to match the convention
    invitation_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=get_current_utc, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    is_used = db.Column(db.String(1), nullable=False, default='0')
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def calculate_expiry_date(self):
        # Calculate expiry date as 72 hours after created_at
        self.expiry_date = self.created_at + timedelta(hours=72)

    def __init__(self, token, email, expiry_date, user_id, is_used='0'):
        self.token = token
        self.email = email
        self.expiry_date = expiry_date
        self.user_id = user_id
        self.is_used = is_used

    def __repr__(self):
        return f'<Invitation {self.invitation_id}>'

    def to_dict(self):
        return {
            'invitation_id': self.invitation_id,
            'token': self.token,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'expiry_date': self.expiry_date.isoformat() if self.expiry_date else None,
            'is_used': self.is_used,
            'user_id': self.user_id
        }


class Store(db.Model):
    __tablename__ = 'stores'

    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)

    # Converting store object to dictionary
    def to_dict(self):
        return {
            'store_id': self.store_id,
            'store_name': self.store_name,
            'location': self.location
        }

    products = relationship('Product', backref='store')

    # temporarily commented out until inventory table merged by other team member
    # inventory = relationship('Inventory', backref='store')

    def __repr__(self):
        return f'Store(id={self.store_id}, name={self.store_name}, location={self.location})'


class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)

    # Converting product object to dictionary
    def to_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'buying_price': self.buying_price,
            'selling_price': self.selling_price,
            'store_id': self.store_id
        }

    def __repr__(self):
        return f'Product(id={self.product_id}, product_name={self.product_name}, buying_price={self.buying_price}, selling_price={self.selling_price})'
