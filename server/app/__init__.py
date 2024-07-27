from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Load configuration
    app.config.from_object(Config)

    # Set database URI (for local testing; use environment variables for production)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://josephine:root@localhost:5432/inventory_db1'

    # Print database URL for debugging (remove in production)
    print("Database URL:", app.config['SQLALCHEMY_DATABASE_URI'])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints/routes
    with app.app_context():
        from app import models, routes
        # In production, use migrations instead of db.create_all()
        db.create_all()

    return app
