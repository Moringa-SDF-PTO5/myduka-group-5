from flask import make_response, request, jsonify,current_app as app
# from .models import User
# from app import db





@app.route('/')
def home():
    welcome_message = {'message': 'Welcome to the myduka inventory db.'}
    return make_response(jsonify(welcome_message), 200)

