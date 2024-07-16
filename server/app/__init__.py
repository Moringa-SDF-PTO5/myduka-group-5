import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app, send_wildcard=True)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

        # Import and register blueprints
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
