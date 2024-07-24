from flask import request, jsonify, make_response, current_app as app
from app import db
from app.models import User, Invitation, Store, Product
import uuid
from datetime import datetime, timedelta, timezone
from flask_cors import CORS
# Enable CORS
CORS(app)


@app.route('/')
def home():
    welcome_message = {'message': 'Welcome to the myduka inventory db.'}
    return make_response(jsonify(welcome_message), 200)

# User routes


@app.route('/api/users', methods=['GET'])
def list_users():
    users = User.query.all()

    users_data = [user.to_dict() for user in users]
    return jsonify({
        "status": "success",
        "message": "Listed all Users",
        "data": users_data
    }), 200


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({
            "status": "Failed",
            "message": "User not found.",
            "data": None
        }), 404
    return jsonify({
        "status": "Success",
        "message": "User retrieved successfully.",
        "data": user.to_dict()
    }), 200


@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not all(key in data for key in ['username', 'email']):
        return jsonify({
            'status': 'Failed',
            'message': 'Username and email are required.',
            'data': None
        }), 400

    try:
        new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password_hash=data.get('password_hash', None),
            role=data.get('role', 'user'),
            is_active=data.get('is_active', True),
            confirmed_admin=data.get('confirmed_admin', False)
        )
        db.session.add(new_user)
        db.session.commit()

        response_data = {
            'status': 'Success',
            'message': 'User created successfully.',
            'data': new_user.to_dict()
        }
        print(response_data)

        return jsonify(response_data), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'status': 'Failed',
            'message': 'An error occurred while creating the user.',
            'data': None
        }), 500


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({
            "status": "Failed",
            "message": "User not found.",
            "data": None
        }), 404

    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password_hash = data.get('password_hash', user.password_hash)
    user.role = data.get('role', user.role)
    user.is_active = data.get('is_active', user.is_active)
    user.confirmed_admin = data.get('confirmed_admin', user.confirmed_admin)

    db.session.commit()
    return jsonify({
        "status": "Success",
        "message": "User updated successfully.",
        "data": user.to_dict()
    }), 200


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({
            "status": "Failed",
            "message": "User not found.",
            "data": None
        }), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "User deleted successfully.",
        "data": None
    }), 200

# Routes for stores


@app.route('/api/stores', methods=['GET'])
def get_stores():
    stores = Store.query.all()
    stores_data = [store.to_dict() for store in stores]
    return jsonify({
        "status": "success",
        "message": "success",
        "data": stores_data
    }), 200


@app.route('/api/stores/<int:store_id>', methods=['GET'])
def get_store(store_id):
    store = Store.query.get(store_id)
    if not store:
        return jsonify({
            "status": "Failed",
            "message": "Store not found",
            "data": None
        }), 404
    return jsonify({
        "status": "success",
        "message": "success",
        "data": store.to_dict()
    }), 200


@app.route('/api/stores', methods=['POST'])
def create_store():
    data = request.get_json()
    if 'store_name' not in data or 'location' not in data:
        return jsonify({
            'status': 'Failed',
            'message': 'Store_name and location fields are required',
            'data': None
        }), 400

    new_store = Store(
        store_name=data['store_name'],
        location=data['location']
    )
    db.session.add(new_store)
    db.session.commit()
    return jsonify({
        "status": "success",
        "message": "Store added successfully",
        "data": new_store.to_dict()  # Fix data variable to the newly created store
    }), 201


@app.route('/api/stores/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    store = Store.query.get(store_id)
    if not store:
        return jsonify({
            'status': 'Failed',
            'message': 'Store not found',
            'data': None
        }), 404

    data = request.get_json()
    store.store_name = data.get('store_name', store.store_name)
    store.location = data.get('location', store.location)
    db.session.commit()
    return jsonify({
        "status": "success",
        "message": "Store updated successfully",
        "data": store.to_dict()  # Fix data variable to the updated store
    }), 200


@app.route('/api/stores/<int:store_id>', methods=['DELETE'])
def delete_store(store_id):
    store = Store.query.get(store_id)
    if not store:
        return jsonify({
            'status': 'Failed',
            'message': 'Store not found',
            'data': None
        }), 404

    db.session.delete(store)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "Store deleted successfully.",
        "data": None
    }), 200

# Routes for products


@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_data = [product.to_dict() for product in products]
    return jsonify({
        "status": "success",
        "message": "success",
        "data": products_data
    }), 200


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({
            'status': 'Failed',
            'message': 'Product not found',
            'data': None
        }), 404

    return jsonify({
        "status": "success",
        "message": "success",
        "data": product.to_dict()
    }), 200


@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if (
        'product_name' not in data or
        'buying_price' not in data or
        'selling_price' not in data or
        'store_id' not in data
    ):
        return jsonify({
            'status': 'Failed',
            'message': 'product_name, buying_price, selling_price, and store_id are required',
            'data': None
        }), 400

    new_product = Product(
        product_name=data['product_name'],
        buying_price=data['buying_price'],
        selling_price=data['selling_price'],
        store_id=data['store_id']
    )
    db.session.add(new_product)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Product added successfully",
        "data": new_product.to_dict()  # Fix data variable to the newly created product
    }), 201


@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({
            'status': 'Failed',
            'message': 'Product not found',
            'data': None
        }), 404

    data = request.get_json()
    product.product_name = data.get('product_name', product.product_name)
    product.buying_price = data.get('buying_price', product.buying_price)
    product.selling_price = data.get('selling_price', product.selling_price)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Product updated successfully",
        "data": product.to_dict()  # Fix data variable to the updated product
    }), 200


@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({
            'status': 'Failed',
            'message': 'Product not found',
            'data': None
        }), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "Product deleted successfully.",
        "data": None
    }), 200

# Invitation routes


@app.route('/api/invitations', methods=['GET'])
def list_invitations():
    invitations = Invitation.query.all()
    invitations_data = [invitation.to_dict() for invitation in invitations]
    return jsonify({
        "status": "success",
        "message": "listed all invitations",
        "data": invitations_data
    }), 200


@app.route('/api/invitations/<int:invitation_id>', methods=['GET'])
def get_invitation(invitation_id):
    invitation = Invitation.query.get(invitation_id)
    if not invitation:
        return jsonify({
            "status": "Failed",
            "message": "Invitation not found.",
            "data": None
        }), 404

    return jsonify({
        "status": "Success",
        "message": "Invitation retrieved successfully.",
        "data": invitation.to_dict()
    }), 200


def get_current_utc():
    return datetime.now(timezone.utc)


@app.route('/api/invitations', methods=['POST'])
def create_invitation():
    data = request.get_json()
    email = data.get('email')
    user_id = data.get('user_id')

    if not email or not user_id:
        return jsonify({
            'status': 'Failed',
            'message': 'Missing required fields.',
            'data': None
        }), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({
            'status': 'Failed',
            'message': 'User not found.',
            'data': None
        }), 404

    token = str(uuid.uuid4())
    expiry_date = get_current_utc() + timedelta(hours=72)

    invitation = Invitation(
        token=token,
        email=email,
        user_id=user_id,
        expiry_date=expiry_date
    )

    try:
        db.session.add(invitation)
        db.session.commit()
        return jsonify({
            'status': 'Success',
            'message': 'Invitation created successfully.',
            'data': invitation.to_dict()
        }), 201
    except Exception:
        db.session.rollback()
        return jsonify({
            'status': 'Failed',
            'message': 'An error occurred while adding the invitation.',
            'data': 'An error occurred.'
        }), 500


@app.route('/api/invitations/<int:invitation_id>', methods=['DELETE'])
def delete_invitation(invitation_id):
    invitation = Invitation.query.get(invitation_id)
    if not invitation:
        return jsonify({
            'status': 'Failed',
            'message': 'Invitation not found.',
            'data': None
        }), 404

    try:
        db.session.delete(invitation)
        db.session.commit()
        return jsonify({
            'status': 'Success',
            'message': 'Invitation deleted successfully.',
            'data': None
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'Failed',
            'message': 'An error occurred while deleting the invitation.',
            'data': str(e)
        }), 500


@app.route('/api/invitations/<int:invitation_id>', methods=['PUT'])
def update_invitation(invitation_id):
    invitation = Invitation.query.get(invitation_id)
    if not invitation:
        return jsonify({
            "status": "Failed",
            "message": "Invitation not found.",
            "data": None
        }), 404

    data = request.get_json()
    invitation.token = data.get('token', invitation.token)
    invitation.email = data.get('email', invitation.email)
    invitation.expiry_date = data.get('expiry_date', invitation.expiry_date)
    invitation.is_used = data.get('is_used', invitation.is_used)

    db.session.commit()
    return jsonify({
        "status": "Success",
        "message": "Invitation updated successfully.",
        "data": invitation.to_dict()
    }), 200
