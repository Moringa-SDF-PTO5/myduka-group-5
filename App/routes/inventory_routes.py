from flask import Blueprint, request, jsonify
from ..models import Inventory, Product, Store
from .. import db

inventory_bp = Blueprint('inventory', __name__)

# Define your inventory routes here
