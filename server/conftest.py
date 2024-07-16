import pytest
from app import create_app
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    """Load .env file before running tests."""
    load_dotenv()


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            yield client
