import pytest
from sample_app import sample

@pytest.fixture
def client():
    with sample.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200  # nosec