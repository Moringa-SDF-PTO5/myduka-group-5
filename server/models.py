from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
import re

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10))
    is_active = db.Column(db.Boolean(1), default=True)
    confirmed_admin = db.Column(db.Boolean(1), default=False) 
    
    def __repr__(self):
        return f'<User {self.username}>'
    
class Invitations(db.Model):
    __tablename__ = 'invitations'

    invitation_id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    expiry_at = db.Column(db.DateTime, onupdate=db.func.now())
    is_used = db.Column(db.Boolean(1), default=True)
    
    def __repr__(self):
        return f'<Invitation {self.invitation_id}>'

class Store(db.Model):
    __tablename__ = 'stores'

    store_id = db.Column(db.Integer, primary_key = True)
    store_name = db.Column(db.String(50), nullable = False)
    location = db.Column(db.String(50), nullable = False)
    
    # Relationship to access products associated with a store
    store = relationship('Store', backref='products')


def __repr__(self):
        return f'Store(id={self.store_id}, name={self.store_name}, name={self.location})'

class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(50), nullable = False)
    buying_price = db.Column(db.Integer, nullable = False)
    selling_price = db.Column(db.Integer, nullable = False)

def __repr__(self):
        return f'Product(id={self.product_id}, product_name={self.product_name} , buying_price={self.buying_price}, selling_price={self.selling_price})'


class Inventory(db.Model):
    __tablename__= 'inventory'

    inventory_id = db.Column(db.Integer, primary_key = True)
    inventory_name = db.Column(db.String(50), nullable = False)
    store_id = db.Column(db.Integer, nullable = False)
    quantity_received = db.Column(db.Integer, ForeignKey(Store.store_id))
    quantity_in_stock =  db.Column(db.Integer, nullable = False)
    quantity_spoilt =  db.Column(db.Integer, nullable = False)
    payment_status =  db.Column(db.Integer, nullable = False)
   
    # Relationship to access inventory associated with a store
    store = relationship('Store', backref='inventory')



def __repr__(self):
        return f'Inventory(inventory_id={self.inventory_id}, inventory_name={self.inventory_name}, store_id={self.store_id}, quantity_received={self.quantity_received}, quantity_in_stock={self.quantity_in_stock}, quantity_spoilt={self.quantity_spoilt}, payment_status={self.payment_status})'


class Request(db.Model):
    __tablename__ = 'requests'

    request_id = db.Column(db.Integer, primary_key = True)
    Inventory_id = db.Column(db.Integer, ForeignKey(Inventory.inventory_id))
    user_id = db.Column(db.Integer, ForeignKey(Store.store_id))
    request_date = db.Column(db.DateTime, onupdate=db.func.now())
    status = db.Column(db.String, nullable = False)

    inventory = relationship('Inventory', backref='requests')  # Relationship to access inventory associated with a request
    user = relationship('User', backref='requests')  # Relationship to access user associated with a request

def __repr__(self):
        return f'Store(request_id={self.request_id}, inventoryid={self.Inventory_id}, userid={self.user_id}, date_requested={self.request_date}, name={self.user_id}, status={self.status})'
