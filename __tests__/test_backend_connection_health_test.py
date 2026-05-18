from src.core.config import settings
import requests


SERVER_URL = settings.SERVER_URL

def test_backend_connection_health():
    response = requests.get(f"{SERVER_URL}/health")
    assert response.status_code == 200
