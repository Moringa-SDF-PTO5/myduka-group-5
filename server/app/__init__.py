from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    print("Database URL:", app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app import models, routes
        db.create_all()

    return app
