import pytest
from app import create_app

@pytest.fixture(scope='session')
def client():
    app = create_app()
    
    with app.test_client() as client:
        yield client