import os


class Config:
    SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL','postgresql://josephine:root@localhost:5432/inventory_db1')
    ENVIROMENT=os.getenv('APP_ENV','development')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    