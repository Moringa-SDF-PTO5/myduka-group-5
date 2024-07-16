from flask import make_response, current_app as app
from app import db

@app.route('/')
def home():
    welcome_message = {'message': 'Welcome to the myduka inventory db.'}
    return make_response(welcome_message, 200)