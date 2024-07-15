from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    

    from .config import Config
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
            
        db.create_all()

    
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
