from flask import request, jsonify, make_response, current_app as app
from app import db
from app.models import User, Store, Product

@app.route('/')
def home():
    welcome_message = {'message': 'Welcome to the myduka inventory db.'}
    return make_response(jsonify(welcome_message), 200)


@app.route('/users', methods=['GET'])
def list_user():
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    return jsonify({
        "status": "success",
        "message": "success",
        "data": users_data
    }), 201


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')
    role = data.get('role')
    is_active = data.get('is_active')
    confirmed_admin = data.get('confirmed_admin')

    if not (
        user_id and username and email and password_hash and role and
        is_active and confirmed_admin
    ):
        return jsonify({
            "status": "Failed",
            "message": "Please provide all required fields.",
            "data": None
        }), 400

    new_user = User(
        user_id=user_id,
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
            "message": "User not found",
            "data": None
        }), 404

    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password_hash = data.get('password_hash', user.password_hash)
    user.role = data.get('is_active', user.is_active)
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
@app.route('/stores', methods=['GET'])
def get_stores():
    stores = Store.query.all()
    stores_data = [store.to_dict() for store in stores]  # Serialize each Store object
    return jsonify({
        "status": "success",
        "message": "success",
        "data": stores_data
    }), 200

@app.route('/stores/<int:store_id>', methods=['GET'])
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
    }), 201
    

@app.route('/stores', methods=['POST'])
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
    return jsonify(new_store.to_dict()), 201

@app.route('/stores/<int:store_id>', methods=['PUT'])
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
    return jsonify(store.to_dict()), 200

@app.route('/stores/<int:store_id>', methods=['DELETE'])
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
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_data = [product.to_dict() for product in products]
    return jsonify(products_data), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({
            'status': 'Failed',
            'message': 'Product not found',
            'data': None
        }), 404
    
    return jsonify(product.to_dict()), 200

@app.route('/products', methods=['POST'])
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
    return jsonify(new_product.to_dict()), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
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
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
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