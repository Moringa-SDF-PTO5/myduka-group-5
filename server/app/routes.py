# app/routes.py
from flask import request, jsonify, make_response, current_app as app
from app import db
from app.models import User, Invitation, Store, Product, SupplyRequest
import uuid
from datetime import datetime, timedelta, timezone
from werkzeug.security import check_password_hash

@app.route('/')
def home():
    welcome_message = {'message': 'Welcome to the myduka inventory db.'}
    return make_response(jsonify(welcome_message), 200)


# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user is None or not check_password_hash(user.password_hash, password):
        return jsonify({"message": "Invalid email or password"}), 401

    return jsonify({"message": "Login successful", "user": user.username}), 200


# User routes
@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    return jsonify({
        "status": "success",
        "message": "Listed all Users",
        "data": users_data
    }), 200


@app.route('/users/<int:user_id>', methods=['GET'])
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


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')
    role = data.get('role')
    is_active = data.get('is_active')
    confirmed_admin = data.get('confirmed_admin')

    if not (
        username and email and password_hash and role and
        is_active is not None and confirmed_admin is not None
    ):
        return jsonify({
            "status": "Failed",
            "message": "Please provide all required fields.",
            "data": None
        }), 400

    new_user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role=role,
        is_active=is_active,
        confirmed_admin=confirmed_admin
    )

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "status": "Failed",
            "message": "An error occurred while adding the user.",
            "data": str(e)
        }), 500

    return jsonify({
        "status": "Success",
        "message": "User created successfully.",
        "data": new_user.to_dict()
    }), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
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


@app.route('/users/<int:user_id>', methods=['DELETE'])
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


# Routes:: Winnie

# Routes for stores
@app.route('/api/stores', methods=['GET'])
def get_stores():
    stores = Store.query.all()
    stores_data = [store.to_dict() for store in stores]  # Serialize each Store object
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
    
    new_store = Store(store_name=data['store_name'], location=data['location'])
    db.session.add(new_store)
    db.session.commit()
    return jsonify({
        "status": "success",
        "message": "Store added successfully",
        "data": data.to_dict()
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
        "data": data.to_dict()
    }), 201

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
    }), 201

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
    if 'product_name' not in data or 'buying_price' not in data or 'selling_price' not in data or 'store_id' not in data:
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
        "data": data.to_dict()
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
        "data": data.to_dict()
    }), 201

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
    }), 201
# Invitation routes


@app.route('/invitations', methods=['GET'])
def list_invitations():
    invitations = Invitation.query.all()
    invitations_data = [invitation.to_dict() for invitation in invitations]
    return jsonify({
        "status": "success",
        "message": "listed all invitations",
        "data": invitations_data
    }), 200


@app.route('/invitations/<int:invitation_id>', methods=['GET'])
def get_invitation(invitation_id):
    # Retrieve the invitation by ID
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


@app.route('/invitations', methods=['POST'])
def create_invitation():
    data = request.get_json()
    email = data.get('email')
    user_id = data.get('user_id')

    if not email or not user_id:
        return jsonify({
            "status": "Failed",
            "message": "Email and user_id are required.",
            "data": None
        }), 400

    token = str(uuid.uuid4())
    expiry_date = datetime.now(timezone.utc) + timedelta(days=7)

    new_invitation = Invitation(
        token=token,
        email=email,
        expiry_date=expiry_date,
        user_id=user_id
    )

    try:
        db.session.add(new_invitation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "status": "Failed",
            "message": "An error occurred while adding the invitation.",
            "data": str(e)
        }), 500

    return jsonify({
        "status": "Success",
        "message": "Invitation created successfully.",
        "data": new_invitation.to_dict()
    }), 201


@app.route('/invitations/<int:invitation_id>', methods=['PUT'])
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


@app.route('/invitations/<int:invitation_id>', methods=['DELETE'])
def delete_invitation(invitation_id):
    invitation = Invitation.query.get(invitation_id)
    if not invitation:
        return jsonify({
            "status": "Failed",
            "message": "Invitation not found.",
            "data": None
        }), 404

    db.session.delete(invitation)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "Invitation deleted successfully.",
        "data": None
    }), 200

# Supply request routes
@app.route('/api/supply_requests', methods=['GET', 'POST'])
def supply_requests():
    if request.method == 'GET':
        supply_requests = SupplyRequest.query.order_by(SupplyRequest.id).all()
        requests_data = [supply_request.to_dict() for supply_request in supply_requests]

        response = {
            'message': 'Supply requests retrieved successfully.',
            'status': 'success',
            'data': requests_data
        }

        return make_response(response, 200)
    elif request.method == 'POST':
        try:
            data = request.get_json()

            new_request = SupplyRequest(
                product_id=data['product_id'],
                number_requested=data['number_requested']
            )

            db.session.add(new_request)
            db.session.commit()

            response = {
                'message': 'Supply request added successfully.',
                'status': 'success',
                'data': new_request.to_dict()
            }

            return make_response(response, 201)
        except Exception as error:
            response = {
                'message': 'Request not added.',
                'status': 'error',
                'data': error
            }

            return make_response(response, 500)
        
@app.route('/api/supply_requests/<int:id>', methods=['GET', 'PATCH'])
def one_supply_request(id):
    supply_request = SupplyRequest.query.filter_by(id = id).first()
    if supply_request:
        if request.method == 'GET':
            response = {
                'message': 'Supply request retreived succeddfully.',
                'status': 'success',
                'data': supply_request.to_dict()
            }

            return make_response(response, 200)
        elif request.method == 'PATCH':
            try:
                data = request.get_json()

                for key in data:
                    setattr(supply_request, key, data[key])

                db.session.add(supply_request)
                db.session.commit()

                updated_supply_request = supply_request.to_dict()

                response = {
                    'message': 'Supply request updated successfully.',
                    'status': 'success',
                    'data': updated_supply_request
                }
                return make_response(response, 200)
            except Exception as error:
                response = {
                    'message': 'Supply request approval not edited.',
                    'status': 'error',
                    'data': error
                }

                return make_response(response, 400)
    else:
        response = {
            'message': 'Supply request not found.',
            'status': 'error',
            'data': None
        }

        return make_response(response, 404)
