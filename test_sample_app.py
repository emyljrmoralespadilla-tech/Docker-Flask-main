import pytest
from sample_app import sample

@pytest.fixture
def client():
    sample.config['TESTING'] = True
    with sample.test_client() as client:
        yield client

def test_main(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"OK" in rv.data