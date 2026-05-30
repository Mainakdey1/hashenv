import requests
from core.config import settings

SERVER_URL = settings.SERVER_URL

def get_env_from_backend(repository: str):
    response = requests.get(f"{SERVER_URL}/env/{repository}")
    env_data = None
    if response.status_code == 200:
        env_data = response.json()
        return None if len(env_data) == 0 else env_data