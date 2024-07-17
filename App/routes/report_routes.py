from flask import Blueprint, jsonify
from ..models import Inventory, Product, Store
from .. import db
from datetime import datetime, timedelta

report_bp = Blueprint('report', __name__)

@report_bp.route('/report/weekly', methods=['GET'])
def weekly_report():
    today = datetime.utcnow()
    week_ago = today - timedelta(days=7)
    
    inventory = db.session.query(
        Inventory.store_id,
        Store.store_name,
        Product.product_name,
        db.func.sum(Inventory.quantity_received).label('total_received'),
        db.func.sum(Inventory.quantity_in_stock).label('total_in_stock'),
        db.func.sum(Inventory.quantity_spoilt).label('total_spoilt')
    ).join(Store, Inventory.store_id == Store.store_id
    ).join(Product, Inventory.product_id == Product.product_id
    ).filter(Inventory.created_at.between(week_ago, today)
    ).group_by(Inventory.store_id, Store.store_name, Product.product_name).all()

    result = []
    for inv in inventory:
        result.append({
            'store_id': inv.store_id,
            'store_name': inv.store_name,
            'product_name': inv.product_name,
            'total_received': inv.total_received,
            'total_in_stock': inv.total_in_stock,
            'total_spoilt': inv.total_spoilt
        })

    return jsonify(result)

@report_bp.route('/report/monthly', methods=['GET'])
def monthly_report():
    today = datetime.utcnow()
    month_ago = today - timedelta(days=30)
    
    inventory = db.session.query(
        Inventory.store_id,
        Store.store_name,
        Product.product_name,
        db.func.sum(Inventory.quantity_received).label('total_received'),
        db.func.sum(Inventory.quantity_in_stock).label('total_in_stock'),
        db.func.sum(Inventory.quantity_spoilt).label('total_spoilt')
    ).join(Store, Inventory.store_id == Store.store_id
    ).join(Product, Inventory.product_id == Product.product_id
    ).filter(Inventory.created_at.between(month_ago, today)
    ).group_by(Inventory.store_id, Store.store_name, Product.product_name).all()

    result = []
    for inv in inventory:
        result.append({
            'store_id': inv.store_id,
            'store_name': inv.store_name,
            'product_name': inv.product_name,
            'total_received': inv.total_received,
            'total_in_stock': inv.total_in_stock,
            'total_spoilt': inv.total_spoilt
        })

    return jsonify(result)

@report_bp.route('/report/annual', methods=['GET'])
def annual_report():
    today = datetime.utcnow()
    year_ago = today - timedelta(days=365)
    
    inventory = db.session.query(
        Inventory.store_id,
        Store.store_name,
        Product.product_name,
        db.func.sum(Inventory.quantity_received).label('total_received'),
        db.func.sum(Inventory.quantity_in_stock).label('total_in_stock'),
        db.func.sum(Inventory.quantity_spoilt).label('total_spoilt')
    ).join(Store, Inventory.store_id == Store.store_id
    ).join(Product, Inventory.product_id == Product.product_id
    ).filter(Inventory.created_at.between(year_ago, today)
    ).group_by(Inventory.store_id, Store.store_name, Product.product_name).all()

    result = []
    for inv in inventory:
        result.append({
            'store_id': inv.store_id,
            'store_name': inv.store_name,
            'product_name': inv.product_name,
            'total_received': inv.total_received,
            'total_in_stock': inv.total_in_stock,
            'total_spoilt': inv.total_spoilt
        })

    return jsonify(result)
