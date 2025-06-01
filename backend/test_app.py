from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/api')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello from backend!'}
