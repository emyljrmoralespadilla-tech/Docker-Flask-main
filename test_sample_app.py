from sample_app import sample


def test_home():
    client = sample.test_client()

    response = client.get("/")

    assert response.status_code == 200


