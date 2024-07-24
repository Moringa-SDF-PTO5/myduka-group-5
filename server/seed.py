from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from datetime import datetime
from app.models import User, Invitations, Store, Product, Inventory, Request
from dotenv import load_dotenv
from datetime import datetime, timedelta
from app.models import User, Invitation, Store, Product  # , Inventory, Request
from app import db


# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize SQLAlchemy
db = SQLAlchemy(app)

# Create the Flask app
app = create_app()


def create_seed_data():
    with app.app_context():
        # Create users

        user4 = User(username='Josephine', email='josephine.nzioka1@student.moringaschool.com',
                     password_hash='securepassword', role='user')
        user5 = User(username='Kantai', email='saiyalel.kantai@student.moringaschool.com',
                     password_hash='securepassword', role='user')

        # Create invitations
        invitation1 = Invitations(
            token='token123', email='winnie.abuor@student.moringaschool.com')
        invitation2 = Invitations(
            token='token456', email='frasia.nyakundi@student.moringaschool.com')
        invitation3 = Invitations(
            token='token789', email='barbara.ndiba@student.moringaschool.com')
        invitation4 = Invitations(
            token='token101', email='josephine.nzioka1@student.moringaschool.com')
        invitation5 = Invitations(
            token='token132', email='saiyalel.kantai@student.moringaschool.com')
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
        db.session.add_all(
            [invitation1, invitation2, invitation3, invitation4, invitation5])
        db.session.commit()

        # Create stores
        store1 = Store(store_name='Store A', location='Ngong Road')

    product4 = Product(product_name='Java Esspresso Coffee',
                       buying_price=480, selling_price=790, store_id=store4.store_id)
    product5 = Product(product_name='Skippy Peanut Butter',
                       buying_price=1000, selling_price=1500, store_id=store5.store_id)

    # Create inventory
    inventory1 = Inventory(inventory_name='Bravo Dog food', store_id=store1.store_id,
                           quantity_received=100, quantity_in_stock=80, quantity_spoilt=5, payment_status=1)
    inventory2 = Inventory(inventory_name='Basmati Rice', store_id=store2.store_id,
                           quantity_received=120, quantity_in_stock=100, quantity_spoilt=10, payment_status=1)
    inventory3 = Inventory(inventory_name='Ketepa Tea Bags', store_id=store3.store_id,
                           quantity_received=100, quantity_in_stock=80, quantity_spoilt=5, payment_status=1)
    inventory4 = Inventory(inventory_name='Java Esspresso Coffee', store_id=store4.store_id,
                           quantity_received=120, quantity_in_stock=100, quantity_spoilt=10, payment_status=1)
    inventory5 = Inventory(inventory_name='Skippy Peanut Butter', store_id=store5.store_id,
                           quantity_received=100, quantity_in_stock=80, quantity_spoilt=5, payment_status=1)

    # Add products and inventory to session
    db.session.add_all([product1, product2, product3, product4, product5,
                        inventory1, inventory2, inventory3, inventory4, inventory5])
    # Add products to session
    db.session.add_all([product1, product2, product3, product4, product5])
    db.session.commit()

    # Create requests
    request1 = Request(inventory_id=inventory1.inventory_id,
                       user_id=user1.user_id, request_date=datetime.now(), status='Pending')
    request2 = Request(inventory_id=inventory2.inventory_id,
                       user_id=user2.user_id, request_date=datetime.now(), status='Approved')
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
    db.session.add_all([request1, request2])
    db.session.commit()
    # db.session.add_all([request1, request2])
    # db.session.commit()


if __name__ == '__main__':
    create_seed_data()
