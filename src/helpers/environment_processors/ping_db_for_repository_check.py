import requests
from core.config import settings

LOCAL_SERVER_URL = settings.LOCAL_SERVER_URL

def ping_db_for_repository_check(repository: str):
    response = requests.get(f"{LOCAL_SERVER_URL}/env/{repository}")
    if response.status_code == 200:
        return False if len(response.json()) == 0 else True