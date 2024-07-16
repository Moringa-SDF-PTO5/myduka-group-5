import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'default_url')
    ENVIRONMENT = os.getenv('APP_ENV', 'development')
    SECRET_KEY = os.getenv('SECRET_KEY')