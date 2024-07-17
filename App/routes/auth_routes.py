from flask import Blueprint, request, jsonify
from ..models import User, Invitation
from .. import db

auth_bp = Blueprint('auth', __name__)

# authentication routes can be defined here
