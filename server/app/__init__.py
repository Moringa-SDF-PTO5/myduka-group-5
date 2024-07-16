from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__)
    
    # Configure SQLAlchemy database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

        # Import and register blueprints
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
