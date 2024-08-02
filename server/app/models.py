# app/models.py
from app import db
from datetime import datetime, timezone,timedelta
# from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin


def get_current_utc():
    return datetime.now(timezone.utc)

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

    # Set expiry date to 72 hours after date invitation was created : Winnie
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


# Models : Winnie
# Edits to Store and Product classes by Barbara - Addition of serialized relationships
    
class Store(db.Model, SerializerMixin):
    __tablename__ = 'stores'

    serialize_rules = ('-products.store',)

    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)

    # I've commented this section out since the return of this instance is now being handled by
        # SerializerMixin
    # Converting store object to dictionary
    # def to_dict(self):
    #     return {
    #         'store_id': self.store_id,
    #         'store_name': self.store_name,
    #         'location': self.location
    #     }

    products = db.relationship('Product', back_populates='store')
    
    # temporarily commented out until inventory table merged by other team member
    # inventory = relationship('Inventory', backref='store')

    def __repr__(self):
        return f'Store(id={self.store_id}, name={self.store_name}, name={self.location})'

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

    # One store can have many products so the product keeps the relationship
    # This is a more user friendly way of populating the store id part
    store = db.relationship('Store', back_populates='products')

    # Get the supply requests that this product is a part of
    supply_requests = db.relationship('SupplyRequest', back_populates='product')

    # I've commented this section out since the return of this instance is now being handled by
        # SerializerMixin
    # Converting product object to dictionary
    # def to_dict(self):
    #     return {
    #         'product_id': self.product_id,
    #         'product_name': self.product_name,
    #         'number_received': self.number_received,
    #         'number_dispatched': self.number_dispatched,
    #         'buying_price': self.buying_price,
    #         'selling_price': self.selling_price,
    #         'store_id': self.store_id
    #     }

    def __repr__(self):
        return f'Product(id={self.product_id}, product_name={self.product_name} , buying_price={self.buying_price}, selling_price={self.selling_price})'

# Add supply request model - Barbara
class SupplyRequest(db.Model, SerializerMixin):
    __tablename__ = 'supply_requests'

    serialize_rules = ('-product.supply_requests',)

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    number_requested = db.Column(db.Integer, nullable=False, default=0)
    is_approved = db.Column(db.Boolean, default=False)

    # One product, can be in many supply requests, thus this table stores the relationship
    product = db.relationship('Product', back_populates='supply_requests')




#Models: Kantai 

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
    
    def to_dict(self):
        return {
            'inventory_id': self.inventory_id,
            'product_id': self.product_id,
            'store_id': self.store_id,
            'quantity_received': self.quantity_received,
            'quantity_in_stock': self.quantity_in_stock,
            'quantity_spoilt': self.quantity_spoilt,
            'payment_status': self.payment_status,
            'created_at': self.created_at
        }
    
    def __repr__(self):
        return f'<Inventory {self.inventory_id}>'