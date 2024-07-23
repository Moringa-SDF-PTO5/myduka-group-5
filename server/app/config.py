import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    ENVIRONMENT = os.getenv('APP_ENV', 'development')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
