from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import User, Invitation, Store, Product, Inventory, Request

app = create_app()


def create_seed_data():
    with app.app_context():
        try:
            # Seed Users
            seed_users()

            # Seed Invitations
            seed_invitations()

            # Seed Stores
            seed_stores()

            # Seed Products
            seed_products()

            # Seed Inventory
            seed_inventory()

            # Seed Requests
            seed_requests()

        except Exception as e:
            db.session.rollback()
            print(f"An error occurred: {e}")


def seed_users():
    users = [
        {'username': 'Winnie', 'email': 'winnie.abuor@student.moringaschool.com',
            'password': 'password123', 'role': 'admin'},
        {'username': 'Frasia', 'email': 'frasia.nyakundi@student.moringaschool.com',
            'password': 'securepassword', 'role': 'user'},
        {'username': 'Barbara', 'email': 'barbara.ndiba@student.moringaschool.com',
            'password': 'password123', 'role': 'admin'},
        {'username': 'Josephine', 'email': 'josephine.nzioka1@student.moringaschool.com',
            'password': 'securepassword', 'role': 'user'},
        {'username': 'Kantai', 'email': 'saiyalel.kantai@student.moringaschool.com',
            'password': 'securepassword', 'role': 'user'}
    ]

    for user_data in users:
        if User.query.filter_by(username=user_data['username']).first() is None:
            user = User(
                username=user_data['username'],
                email=user_data['email'],
                password_hash=generate_password_hash(user_data['password']),
                role=user_data['role']
            )
            db.session.add(user)
    db.session.commit()


def seed_invitations():
    now = datetime.utcnow()
    invitations = [
        {'token': 'token123', 'email': 'winnie.abuor@student.moringaschool.com', 'username': 'Winnie'},
        {'token': 'token456', 'email': 'frasia.nyakundi@student.moringaschool.com',
            'username': 'Frasia'},
        {'token': 'token789', 'email': 'barbara.ndiba@student.moringaschool.com',
            'username': 'Barbara'},
        {'token': 'token101', 'email': 'josephine.nzioka1@student.moringaschool.com',
            'username': 'Josephine'},
        {'token': 'token132', 'email': 'saiyalel.kantai@student.moringaschool.com',
            'username': 'Kantai'}
    ]

    for invitation_data in invitations:
        user = User.query.filter_by(username=invitation_data['username']).first()
        if user:
            invitation = Invitation(
                token=invitation_data['token'],
                email=invitation_data['email'],
                expiry_date=now + timedelta(hours=72),
                user_id=user.user_id
            )
            db.session.add(invitation)
    db.session.commit()


def seed_stores():
    stores = [
        {'store_name': 'Store A', 'location': 'Ngong Road'},
        {'store_name': 'Store B', 'location': 'Westlands'},
        {'store_name': 'Store C', 'location': 'Buruburu'},
        {'store_name': 'Store D', 'location': 'South B'},
        {'store_name': 'Store E', 'location': 'Thika Road'}
    ]

    for store_data in stores:
        if Store.query.filter_by(store_name=store_data['store_name']).first() is None:
            store = Store(
                store_name=store_data['store_name'],
                location=store_data['location']
            )
            db.session.add(store)
    db.session.commit()


def seed_products():
    products = [
        {'product_name': 'Bravo Dog food', 'buying_price': 600,
            'selling_price': 920, 'store_name': 'Store A'},
        {'product_name': 'Basmati Rice', 'buying_price': 210,
            'selling_price': 420, 'store_name': 'Store B'},
        {'product_name': 'Ketepa Tea Bags', 'buying_price': 100,
            'selling_price': 150, 'store_name': 'Store C'},
        {'product_name': 'Java Espresso Coffee', 'buying_price': 480,
            'selling_price': 790, 'store_name': 'Store D'},
        {'product_name': 'Skippy Peanut Butter', 'buying_price': 1000,
            'selling_price': 1500, 'store_name': 'Store E'}
    ]

    for product_data in products:
        store = Store.query.filter_by(store_name=product_data['store_name']).first()
        if store:
            product = Product(
                product_name=product_data['product_name'],
                buying_price=product_data['buying_price'],
                selling_price=product_data['selling_price'],
                store_id=store.store_id
            )
            db.session.add(product)
    db.session.commit()


def seed_inventory():
    inventories = [
        {'inventory_name': 'Bravo Dog food', 'store_name': 'Store A', 'quantity_received': 100,
            'quantity_in_stock': 80, 'quantity_spoilt': 5, 'payment_status': 1},
        {'inventory_name': 'Basmati Rice', 'store_name': 'Store B', 'quantity_received': 120,
            'quantity_in_stock': 100, 'quantity_spoilt': 10, 'payment_status': 1},
        {'inventory_name': 'Ketepa Tea Bags', 'store_name': 'Store C', 'quantity_received': 100,
            'quantity_in_stock': 80, 'quantity_spoilt': 5, 'payment_status': 1},
        {'inventory_name': 'Java Espresso Coffee', 'store_name': 'Store D', 'quantity_received': 120,
            'quantity_in_stock': 100, 'quantity_spoilt': 10, 'payment_status': 1},
        {'inventory_name': 'Skippy Peanut Butter', 'store_name': 'Store E', 'quantity_received': 100,
            'quantity_in_stock': 80, 'quantity_spoilt': 5, 'payment_status': 1}
    ]

    for inventory_data in inventories:
        store = Store.query.filter_by(store_name=inventory_data['store_name']).first()
        if store:
            inventory = Inventory(
                inventory_name=inventory_data['inventory_name'],
                store_id=store.store_id,
                quantity_received=inventory_data['quantity_received'],
                quantity_in_stock=inventory_data['quantity_in_stock'],
                quantity_spoilt=inventory_data['quantity_spoilt'],
                payment_status=inventory_data['payment_status']
            )
            db.session.add(inventory)
    db.session.commit()


def seed_requests():
    requests = [
        {'inventory_name': 'Bravo Dog food', 'username': 'Winnie', 'status': 'Pending'},
        {'inventory_name': 'Basmati Rice', 'username': 'Frasia', 'status': 'Approved'}
    ]

    for request_data in requests:
        user = User.query.filter_by(username=request_data['username']).first()
        inventory = Inventory.query.filter_by(
            inventory_name=request_data['inventory_name']).first()
        if user and inventory:
            request = Request(
                inventory_id=inventory.inventory_id,
                user_id=user.user_id,
                request_date=datetime.now(),
                status=request_data['status']
            )
            db.session.add(request)
    db.session.commit()


if __name__ == '__main__':
    create_seed_data()
