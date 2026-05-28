import requests
from core.config import settings

SERVER_URL = settings.SERVER_URL

def get_env_from_backend(repository: str):
    response = requests.get(f"{SERVER_URL}/env/{repository}")
    if response.status_code == 200:
        env_data = response.json()
        return env_data
    else:
        return 'Error fetching env data from backend'