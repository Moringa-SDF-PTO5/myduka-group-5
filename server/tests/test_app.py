import pytest
from app import create_app, db
from flask_cors import CORS


@pytest.fixture(scope='module')
def test_client():
    app = create_app('app.config.TestingConfig')
    CORS(app)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_index(test_client):
    rv = test_client.get('/')
    json_data = rv.get_json()
    assert json_data == {'message': 'Welcome to the myduka inventory db.'}


def test_user_creation(test_client):
    user_data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password_hash': 'hashedpassword',
        'role': 'admin',
        'is_active': True,
        'confirmed_admin': False
    }

    response = test_client.post('/api/users', json=user_data)
    assert response.status_code == 201
    response_data = response.get_json()
    assert response_data['status'] == 'Success'
    assert 'user_id' in response_data['data']


def test_user_retrieval(test_client):
    user_data = {
        'username': 'retrievaluser',
        'email': 'retrievaluser@example.com',
        'password_hash': 'hashedpassword',
        'role': 'user',
        'is_active': True,
        'confirmed_admin': False
    }
    response = test_client.post('/api/users', json=user_data)
    user_id = response.get_json()['data']['user_id']

    response = test_client.get(f'/api/users/{user_id}')
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['status'] == 'Success'
    assert response_json['data']['username'] == user_data['username']
    assert response_json['data']['email'] == user_data['email']


def test_user_update(test_client):
    user_data = {
        'username': 'updateuser',
        'email': 'updateuser@example.com',
        'password_hash': 'hashedpassword',
        'role': 'user',
        'is_active': True,
        'confirmed_admin': False
    }
    response = test_client.post('/api/users', json=user_data)
    user_id = response.get_json()['data']['user_id']

    updated_data = {
        'username': 'updateduser',
        'email': 'updateduser@example.com',
        'password_hash': 'newhashedpassword',
        'role': 'admin',
        'is_active': False,
        'confirmed_admin': True
    }
    response = test_client.put(f'/api/users/{user_id}', json=updated_data)
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['status'] == 'Success'
    assert response_json['data']['username'] == updated_data['username']
    assert response_json['data']['email'] == updated_data['email']

    response = test_client.delete(f'/api/users/{user_id}')
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['status'] == 'Success'

    response = test_client.get(f'/api/users/{user_id}')
    assert response.status_code == 404
    response_json = response.get_json()
    assert response_json['status'] == 'Failed'
