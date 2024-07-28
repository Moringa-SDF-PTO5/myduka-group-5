from app import db
from datetime import datetime, timezone, timedelta
from sqlalchemy_serializer import SerializerMixin


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

    # Define the relationship with a unique backref name
    invitations = db.relationship('Invitation', backref='inviter', lazy=True)

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
    invitation_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=get_current_utc, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    is_used = db.Column(db.String(1), nullable=False, default='0')

    # Foreign key relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    # Set expiry date to 72 hours after date invitation was created
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
            'created_at': self.created_at,
            'expiry_date': self.expiry_date,
            'is_used': self.is_used,
            'user_id': self.user_id
        }


class Store(db.Model, SerializerMixin):
    __tablename__ = 'stores'

    serialize_rules = ('-products.store',)

    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)

    products = db.relationship('Product', back_populates='store')

    def __repr__(self):
        return f'Store(id={self.store_id}, name={self.store_name}, location={self.location})'


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    serialize_rules = ('-store.products', '-supply_requests.product',)

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    number_received = db.Column(db.Integer, default=0)
    number_dispatched = db.Column(db.Integer, default=0)
    is_paid = db.Column(db.Boolean, default=False)
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)

    store = db.relationship('Store', back_populates='products')
    supply_requests = db.relationship('SupplyRequest', back_populates='product')

    def __repr__(self):
        return f'Product(id={self.product_id}, product_name={self.product_name}, buying_price={self.buying_price}, selling_price={self.selling_price})'


class SupplyRequest(db.Model, SerializerMixin):
    __tablename__ = 'supply_requests'

    serialize_rules = ('-product.supply_requests',)

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    number_requested = db.Column(db.Integer, nullable=False, default=0)
    is_approved = db.Column(db.Boolean, default=False)

    product = db.relationship('Product', back_populates='supply_requests')

    def __repr__(self):
        return f'SupplyRequest(id={self.id}, product_id={self.product_id}, number_requested={self.number_requested}, is_approved={self.is_approved})'
