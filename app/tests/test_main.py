import sys
import os
import pytest

# Add the src directory to the Python path
# This allows us to import the 'app' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_devsecops(client):
    """
    Test the / endpoint.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevSecOps!" in response.data
