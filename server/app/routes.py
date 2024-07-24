# app/routes.py
from flask import request, jsonify, make_response, current_app as app
from app import db
from app.models import User, Invitation, Store, Product, Inventory, SupplyRequest
import uuid
from datetime import datetime, timedelta, timezone


@app.route('/')
def home():
    welcome_message = {'message': 'Welcome to the myduka inventory db.'}
    return make_response(jsonify(welcome_message), 200)

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

#Routes Kantai

# Inventory Routes

@app.route('/inventory', methods=['GET'])
def get_all_inventory():
    inventory = Inventory.query.all()
    result = []
    for item in inventory:
        result.append({
            'inventory_id': item.inventory_id,
            'product_id': item.product_id,
            'store_id': item.store_id,
            'quantity_received': item.quantity_received,
            'quantity_in_stock': item.quantity_in_stock,
            'quantity_spoilt': item.quantity_spoilt,
            'payment_status': item.payment_status,
            'created_at': item.created_at
        })
    return jsonify(result)

@app.route('/inventory/<int:inventory_id>', methods=['GET'])
def get_inventory(inventory_id):
    item = Inventory.query.get_or_404(inventory_id)
    result = {
        'inventory_id': item.inventory_id,
        'product_id': item.product_id,
        'store_id': item.store_id,
        'quantity_received': item.quantity_received,
        'quantity_in_stock': item.quantity_in_stock,
        'quantity_spoilt': item.quantity_spoilt,
        'payment_status': item.payment_status,
        'created_at': item.created_at
    }
    return jsonify(result)

@app.route('/inventory', methods=['POST'])
def create_inventory():
    data = request.get_json()
    new_inventory = Inventory(
        product_id=data['product_id'],
        store_id=data['store_id'],
        quantity_received=data['quantity_received'],
        quantity_in_stock=data['quantity_in_stock'],
        quantity_spoilt=data['quantity_spoilt'],
        payment_status=data['payment_status']
    )
    db.session.add(new_inventory)
    db.session.commit()
    return jsonify({'message': 'New inventory item created!'}), 201

@app.route('/inventory/<int:inventory_id>', methods=['PUT'])
def update_inventory(inventory_id):
    data = request.get_json()
    item = Inventory.query.get_or_404(inventory_id)
    item.product_id = data['product_id']
    item.store_id = data['store_id']
    item.quantity_received = data['quantity_received']
    item.quantity_in_stock = data['quantity_in_stock']
    item.quantity_spoilt = data['quantity_spoilt']
    item.payment_status = data['payment_status']
    db.session.commit()
    return jsonify({'message': 'Inventory item updated!'})

@app.route('/inventory/<int:inventory_id>', methods=['DELETE'])
def delete_inventory(inventory_id):
    item = Inventory.query.get_or_404(inventory_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Inventory item deleted!'})

# Supply Request Routes

@app.route('/supply_requests', methods=['GET'])
def get_all_supply_requests():
    requests = SupplyRequest.query.all()
    result = []
    for req in requests:
        result.append({
            'request_id': req.request_id,
            'inventory_id': req.inventory_id,
            'user_id': req.user_id,
            'request_date': req.request_date,
            'status': req.status
        })
    return jsonify(result)

@app.route('/supply_requests/<int:request_id>', methods=['GET'])
def get_supply_request(request_id):
    req = SupplyRequest.query.get_or_404(request_id)
    result = {
        'request_id': req.request_id,
        'inventory_id': req.inventory_id,
        'user_id': req.user_id,
        'request_date': req.request_date,
        'status': req.status
    }
    return jsonify(result)

@app.route('/supply_requests', methods=['POST'])
def create_supply_request():
    data = request.get_json()
    new_request = SupplyRequest(
        inventory_id=data['inventory_id'],
        user_id=data['user_id'],
        request_date=datetime.utcnow(),
        status=data['status']
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'message': 'New supply request created!'}), 201

@app.route('/supply_requests/<int:request_id>', methods=['PUT'])
def update_supply_request(request_id):
    data = request.get_json()
    req = SupplyRequest.query.get_or_404(request_id)
    req.inventory_id = data['inventory_id']
    req.user_id = data['user_id']
    req.request_date = data['request_date']
    req.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Supply request updated!'})

@app.route('/supply_requests/<int:request_id>', methods=['DELETE'])
def delete_supply_request(request_id):
    req = SupplyRequest.query.get_or_404(request_id)
    db.session.delete(req)
    db.session.commit()
    return jsonify({'message': 'Supply request deleted!'})
