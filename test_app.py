# test_app.py

import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello(client):
    """Test the root endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask API!" in response.data


def test_get_users(client):
    """Test the /users endpoint"""
    response = client.get('/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, dict)  # Data should be a dictionary


def test_get_user(client):
    """Test the /user/<id> endpoint with an existing user"""
    response = client.get('/user/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Alice'
    assert data['age'] == 30


def test_get_user_not_found(client):
    """Test the /user/<id> endpoint with a non-existing user"""
    response = client.get('/user/99')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error'] == 'User not found'


def test_create_user(client):
    """Test the /user POST endpoint"""
    new_user = {"name": "Charlie", "age": 35}
    response = client.post('/user', json=new_user)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == "Charlie"
    assert data['age'] == 35


def test_create_user_bad_request(client):
    """Test the /user POST endpoint with missing fields"""
    new_user = {"name": "Charlie"}  # Missing 'age'
    response = client.post('/user', json=new_user)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error'] == "Bad request, 'name' and 'age' required"
