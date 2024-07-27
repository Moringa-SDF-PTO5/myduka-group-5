from datetime import datetime, timezone, timedelta
from app import db
from sqlalchemy.orm import relationship


def get_current_utc():
    return datetime.now(timezone.utc)


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(36), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    is_used = db.Column(db.String(1), default='0', nullable=False)

    # Define the relationship
    user = db.relationship(
        'User', backref=db.backref('invitations', lazy=True))

    def __init__(self, token, email, expiry_date, user_id, is_used='0'):
        self.token = token
        self.email = email
        self.expiry_date = expiry_date
        self.user_id = user_id
        self.is_used = is_used

    def calculate_expiry_date(self):
        # Calculate expiry date as 72 hours after created_at
        if not self.expiry_date:
            self.expiry_date = datetime.now(timezone.utc) + timedelta(hours=72)

    def __repr__(self):
        return f'<Invitation {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'token': self.token,
            'email': self.email,
            'expiry_date': self.expiry_date.isoformat(),
            'user_id': self.user_id,
            'is_used': self.is_used
        }


class Store(db.Model):
    __tablename__ = 'stores'
    store_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)

    products = relationship('Product', backref='store')
    # Temporarily commented out until inventory table merged by another team member
    # inventory = relationship('Inventory', backref='store')

    def to_dict(self):
        return {
            'store_id': self.store_id,
            'store_name': self.store_name,
            'location': self.location
        }

    def __repr__(self):
        return f'Store(id={self.store_id}, name={self.store_name}, location={self.location})'


class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(50), nullable=False)
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey(
        'stores.store_id'), nullable=False)

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


class Inventory(db.Model):
    __tablename__ = 'inventory'
    inventory_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    inventory_name = db.Column(db.String(100), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey(
        'stores.store_id'), nullable=False)
    quantity_received = db.Column(db.Integer, nullable=False)
    quantity_in_stock = db.Column(db.Integer, nullable=False)
    quantity_spoilt = db.Column(db.Integer, nullable=False)
    payment_status = db.Column(db.Integer, nullable=False)

    store = db.relationship(
        'Store', backref=db.backref('inventories', lazy=True))

    def __repr__(self):
        return f'<Inventory {self.inventory_name}>'


class Request(db.Model):
    __tablename__ = 'requests'
    request_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    inventory_id = db.Column(db.Integer, db.ForeignKey(
        'inventory.inventory_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False)

    inventory = db.relationship(
        'Inventory', backref=db.backref('requests', lazy=True))
    user = db.relationship('User', backref=db.backref('requests', lazy=True))

    def __repr__(self):
        return f'<Request {self.request_id}>'
