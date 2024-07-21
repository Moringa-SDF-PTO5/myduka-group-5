from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from datetime import datetime, timedelta
from app.models import User, Invitation, Store, Product  # , Inventory, Request
from app import db


# Create the Flask app
app = create_app()



def create_seed_data():
    with app.app_context():
        # Create users
        user1 = User(username='Winnie', email='winnie.abuor@student.moringaschool.com', password_hash='password123', role='admin')
        user2 = User(username='Frasia', email='frasia.nyakundi@student.moringaschool.com', password_hash='securepassword', role='user')
        user3 = User(username='Barbara', email='barbara.ndiba@student.moringaschool.com', password_hash='password123', role='admin')
        user4 = User(username='Josephine', email='josephine.nzioka1@student.moringaschool.com', password_hash='securepassword', role='user')
        user5 = User(username='Kantai', email='saiyalel.kantai@student.moringaschool.com', password_hash='securepassword', role='user')

        # Add Users 
        db.session.add_all([user1, user2, user3, user4, user5])
        db.session.commit()

        # Create invitations with calculated expiry_date
        now = datetime.utcnow()
        invitation1 = Invitation(token='token123', email='winnie.abuor@student.moringaschool.com', 
                                 expiry_date=now + timedelta(hours=72), user_id=user1.user_id)
        invitation2 = Invitation(token='token456', email='frasia.nyakundi@student.moringaschool.com', 
                                 expiry_date=now + timedelta(hours=72), user_id=user2.user_id)
        invitation3 = Invitation(token='token789', email='barbara.ndiba@student.moringaschool.com', 
                                 expiry_date=now + timedelta(hours=72), user_id=user3.user_id)
        invitation4 = Invitation(token='token101', email='josephine.nzioka1@student.moringaschool.com', 
                                 expiry_date=now + timedelta(hours=72), user_id=user4.user_id)
        invitation5 = Invitation(token='token132', email='saiyalel.kantai@student.moringaschool.com', 
                                 expiry_date=now + timedelta(hours=72), user_id=user5.user_id)

        # Add invitations
        db.session.add_all([invitation1, invitation2, invitation3, invitation4, invitation5])
        db.session.commit()

        # Create stores
        store1 = Store(store_name='Store A', location='Ngong Road')
        store2 = Store(store_name='Store B', location='Westlands')
        store3 = Store(store_name='Store C', location='Buruburu')
        store4 = Store(store_name='Store D', location='South B')
        store5 = Store(store_name='Store E', location='Thika Road')

        # Add stores to session to get store IDs after committing
        db.session.add_all([store1, store2, store3, store4, store5])
        db.session.commit()

        # Create products
        product1 = Product(product_name='Bravo Dog food', buying_price=600, selling_price=920, store_id=store1.store_id)
        product2 = Product(product_name='Basmati Rice', buying_price=210, selling_price=420, store_id=store2.store_id)
        product3 = Product(product_name='Ketepa Tea Bags', buying_price=100, selling_price=150, store_id=store3.store_id)
        product4 = Product(product_name='Java Esspresso Coffee', buying_price=480, selling_price=790, store_id=store4.store_id)
        product5 = Product(product_name='Skippy Peanut Butter', buying_price=1000, selling_price=1500, store_id=store5.store_id)

        # Add products to session
        db.session.add_all([product1, product2, product3, product4, product5])
        db.session.commit()

        # Code temporarily commented until the models are merged with other teams work
        # # Create inventory
        # inventory1 = Inventory(inventory_name='Bravo Dog food', store_id=store1.store_id, quantity_received=100, quantity_in_stock=80, quantity_spoilt=5, payment_status=1)
        # inventory2 = Inventory(inventory_name='Basmati Rice', store_id=store2.store_id, quantity_received=120, quantity_in_stock=100, quantity_spoilt=10, payment_status=1)
        # inventory3 = Inventory(inventory_name='Ketepa Tea Bags', store_id=store3.store_id, quantity_received=100, quantity_in_stock=80, quantity_spoilt=5, payment_status=1)
        # inventory4 = Inventory(inventory_name='Java Esspresso Coffee', store_id=store4.store_id, quantity_received=120, quantity_in_stock=100, quantity_spoilt=10, payment_status=1)
        # inventory5 = Inventory(inventory_name='Skippy Peanut Butter', store_id=store5.store_id, quantity_received=100, quantity_in_stock=80, quantity_spoilt=5, payment_status=1)

        # # Add products and inventory to session
        # db.session.add_all([product1, product2, product3, product4, product5,
        #                     inventory1, inventory2, inventory3, inventory4, inventory5])
        # db.session.commit()

        # # Create requests
        # request1 = Request(inventory_id=inventory1.inventory_id, user_id=user1.user_id, request_date=datetime.now(), status='Pending')
        # request2 = Request(inventory_id=inventory2.inventory_id, user_id=user2.user_id, request_date=datetime.now(), status='Approved')

        # Add requests to session and commit
        # db.session.add_all([request1, request2])
        # db.session.commit()

if __name__ == '__main__':
    create_seed_data()
