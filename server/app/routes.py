from flask import Blueprint, request, jsonify
from .models import Inventory, SupplyRequest 
from ...server.app.extensions import db
from datetime import datetime

inventory_bp = Blueprint('inventory', __name__)

# Inventory Routes

@inventory_bp.route('/inventory', methods=['GET'])
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

@inventory_bp.route('/inventory/<int:inventory_id>', methods=['GET'])
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

@inventory_bp.route('/inventory', methods=['POST'])
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

@inventory_bp.route('/inventory/<int:inventory_id>', methods=['PUT'])
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

@inventory_bp.route('/inventory/<int:inventory_id>', methods=['DELETE'])
def delete_inventory(inventory_id):
    item = Inventory.query.get_or_404(inventory_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Inventory item deleted!'})

# Supply Request Routes

@inventory_bp.route('/supply_requests', methods=['GET'])
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

@inventory_bp.route('/supply_requests/<int:request_id>', methods=['GET'])
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

@inventory_bp.route('/supply_requests', methods=['POST'])
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

@inventory_bp.route('/supply_requests/<int:request_id>', methods=['PUT'])
def update_supply_request(request_id):
    data = request.get_json()
    req = SupplyRequest.query.get_or_404(request_id)
    req.inventory_id = data['inventory_id']
    req.user_id = data['user_id']
    req.request_date = data['request_date']
    req.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Supply request updated!'})

@inventory_bp.route('/supply_requests/<int:request_id>', methods=['DELETE'])
def delete_supply_request(request_id):
    req = SupplyRequest.query.get_or_404(request_id)
    db.session.delete(req)
    db.session.commit()
    return jsonify({'message': 'Supply request deleted!'})
