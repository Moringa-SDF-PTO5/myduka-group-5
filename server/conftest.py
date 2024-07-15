import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            yield client



# @pytest.fixture
# def client():
#     with app.test_client() as client:
#         yield client
