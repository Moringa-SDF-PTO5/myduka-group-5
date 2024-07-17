from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='clerk')
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    confirmed_admin = db.Column(db.Boolean, nullable=False, default=False)

class Invitation(db.Model):
    __tablename__ = 'invitations'
    invitation_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expiry_date = db.Column(db.DateTime, nullable=False)
    is_used = db.Column(db.Boolean, default=False)

class Store(db.Model):
    __tablename__ = 'stores'
    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(25), nullable=False)
    location = db.Column(db.String(50), nullable=False)

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(25), nullable=False)
    buying_price = db.Column(db.String(10), nullable=False)
    selling_price = db.Column(db.String(10), nullable=False)

class Inventory(db.Model):
    __tablename__ = 'inventory'
    inventory_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)
    quantity_received = db.Column(db.Integer, nullable=False)
    quantity_in_stock = db.Column(db.Integer, nullable=False)
    quantity_spoilt = db.Column(db.Integer, nullable=False)
    payment_status = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SupplyRequest(db.Model):
    __tablename__ = 'supply_requests'
    request_id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.inventory_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10), default='pending')

class Payment(db.Model):
    __tablename__ = 'payments'
    payment_id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(25), nullable=False)
    invoice_number = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.String(150), nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_status = db.Column(db.String(1), default='0')  # 0 for not paid, 1 for paid
