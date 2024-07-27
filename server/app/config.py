import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    ENVIRONMENT = os.getenv('APP_ENV', 'development')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        print(
            f"Config: SQLALCHEMY_DATABASE_URI = {self.SQLALCHEMY_DATABASE_URI}")
        print(f"Config: ENVIRONMENT = {self.ENVIRONMENT}")


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    TESTING = True
    DEBUG = True

    def __init__(self):
        super().__init__()
        print(
            f"TestingConfig: SQLALCHEMY_DATABASE_URI = {self.SQLALCHEMY_DATABASE_URI}")
