from flask import request, jsonify, make_response, current_app as app
from app import db
from app.models import User, Invitation, Store, Product, Inventory, SupplyRequest
import uuid
from datetime import datetime, timedelta, timezone
from app.utils import format_response

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
        "data": new_store.to_dict()
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
        "data": store.to_dict()
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
    products = Product.query.order_by(Product.product_id).all()
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
    if 'product_name' not in data or 'buying_price' not in data or 'selling_price' not in data or 'store_id' not in data:
        return jsonify({
            'status': 'Failed',
            'message': 'product_name, buying_price, selling_price, and store_id are required',
            'data': None
        }), 400

    new_product = Product(
        product_name=data['product_name'],
        number_received=data['number_received'],
        number_dispatched=data['number_dispatched'],
        buying_price=data['buying_price'],
        selling_price=data['selling_price'],
        store_id=data['store_id']
    )
    db.session.add(new_product)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Product added successfully",
        "data": new_product.to_dict()
    }), 201

@app.route('/api/products/<int:product_id>', methods=['PATCH'])
def update_product(product_id):
    product = Product.query.get(product_id)
    data = request.get_json()
    if not product:
        return jsonify({
            'status': 'Failed',
            'message': 'Product not found',
            'data': None
        }), 404
    else:
        for key in data:
            setattr(product, key, data[key])

        db.session.add(product)
        db.session.commit()

        updated_product = product.to_dict()

        response = {
            'message': 'Product updated successfully.',
            'status': 'success',
            'data': updated_product
        }

        return make_response(response, 200)

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

@app.route('/api/products/filter', methods=['GET'])
def filter_products():
    product_name = request.args.get('product_name')
    buying_price = request.args.get('buying_price')
    selling_price = request.args.get('selling_price')
    store_id = request.args.get('store_id')

    query = Product.query

    if product_name:
        query = query.filter(Product.product_name.like(f'%{product_name}%'))
    if buying_price:
        query = query.filter_by(buying_price=buying_price)
    if selling_price:
        query = query.filter_by(selling_price=selling_price)
    if store_id:
        query = query.filter_by(store_id=store_id)

    products = query.all()
    products_data = [product.to_dict() for product in products]

    return jsonify({
        "status": "success",
        "message": "success",
        "data": products_data
    }), 200

# Inventory Routes
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    inventory_items = Inventory.query.all()
    inventory_data = [item.to_dict() for item in inventory_items]

    return jsonify({
        "status": "success",
        "message": "success",
        "data": inventory_data
    }), 200

@app.route('/api/inventory/<int:inventory_id>', methods=['GET'])
def get_inventory_item(inventory_id):
    inventory_item = Inventory.query.get(inventory_id)
    if not inventory_item:
        return jsonify({
            "status": "Failed",
            "message": "Inventory item not found",
            "data": None
        }), 404

    return jsonify({
        "status": "success",
        "message": "success",
        "data": inventory_item.to_dict()
    }), 200


@app.route('/api/inventory', methods=['POST'])
def create_inventory_item():
    data = request.get_json()
    if 'product_id' not in data or 'quantity' not in data:
        return jsonify({
            'status': 'Failed',
            'message': 'product_id and quantity are required',
            'data': None
        }), 400

    new_inventory_item = Inventory(
        product_id=data['product_id'],
        quantity=data['quantity']
    )
    db.session.add(new_inventory_item)
    db.session.commit()


    return jsonify({
        "status": "success",
        "message": "Inventory item added successfully",
        "data": new_inventory_item.to_dict()
    }), 201

@app.route('/api/inventory/<int:inventory_id>', methods=['PATCH'])
def update_inventory_item(inventory_id):
    inventory_item = Inventory.query.get(inventory_id)
    data = request.get_json()
    if not inventory_item:
        return jsonify({
            'status': 'Failed',
            'message': 'Inventory item not found',
            'data': None
        }), 404

    if 'product_id' in data:
        inventory_item.product_id = data['product_id']
    if 'quantity' in data:
        inventory_item.quantity = data['quantity']

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Inventory item updated successfully",
        "data": inventory_item.to_dict()
    }), 200

@app.route('/api/inventory/<int:inventory_id>', methods=['DELETE'])
def delete_inventory_item(inventory_id):
    inventory_item = Inventory.query.get(inventory_id)
    if not inventory_item:
        return jsonify({
            'status': 'Failed',
            'message': 'Inventory item not found',
            'data': None
        }), 404

    db.session.delete(inventory_item)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "Inventory item deleted successfully.",
        "data": None
    }), 200

# Supply Request Routes
@app.route('/api/supply-requests', methods=['GET'])
def get_supply_requests():
    supply_requests = SupplyRequest.query.all()
    supply_requests_data = [request.to_dict() for request in supply_requests]

    return jsonify({
        "status": "success",
        "message": "success",
        "data": supply_requests_data
    }), 200

@app.route('/api/supply-requests/<int:supply_request_id>', methods=['GET'])
def get_supply_request(supply_request_id):
    supply_request = SupplyRequest.query.get(supply_request_id)
    if not supply_request:
        return jsonify({
            "status": "Failed",
            "message": "Supply request not found",
            "data": None
        }), 404

    return jsonify({
        "status": "success",
        "message": "success",
        "data": supply_request.to_dict()
    }), 200

@app.route('/api/supply-requests', methods=['POST'])
def create_supply_request():
    data = request.get_json()
    if 'product_id' not in data or 'quantity' not in data or 'request_date' not in data:
        return jsonify({
            'status': 'Failed',
            'message': 'product_id, quantity, and request_date are required',
            'data': None
        }), 400

    new_supply_request = SupplyRequest(
        product_id=data['product_id'],
        quantity=data['quantity'],
        request_date=datetime.strptime(data['request_date'], '%Y-%m-%d')
    )
    db.session.add(new_supply_request)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Supply request added successfully",
        "data": new_supply_request.to_dict()
    }), 201

@app.route('/api/supply-requests/<int:supply_request_id>', methods=['PATCH'])
def update_supply_request(supply_request_id):
    supply_request = SupplyRequest.query.get(supply_request_id)
    data = request.get_json()
    if not supply_request:
        return jsonify({
            'status': 'Failed',
            'message': 'Supply request not found',
            'data': None
        }), 404

    if 'product_id' in data:
        supply_request.product_id = data['product_id']
    if 'quantity' in data:
        supply_request.quantity = data['quantity']
    if 'request_date' in data:
        supply_request.request_date = datetime.strptime(data['request_date'], '%Y-%m-%d')

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Supply request updated successfully",
        "data": supply_request.to_dict()
    }), 200

@app.route('/api/supply-requests/<int:supply_request_id>', methods=['DELETE'])
def delete_supply_request(supply_request_id):
    supply_request = SupplyRequest.query.get(supply_request_id)
    if not supply_request:
        return jsonify({
            'status': 'Failed',
            'message': 'Supply request not found',
            'data': None
        }), 404

    db.session.delete(supply_request)
    db.session.commit()

    return jsonify({
        "status": "Success",
        "message": "Supply request deleted successfully.",
        "data": None
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
