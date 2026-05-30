import requests
from core.config import settings

SERVER_URL = settings.SERVER_URL
LOCAL_SERVER_URL = settings.LOCAL_SERVER_URL

def push_env_to_backend(repository: str, payload: dict):
    response = requests.post(f"{SERVER_URL}/env-recieve", json = {"repository_name": repository, "envs": payload})
    if response.status_code == 200:
        print("Environment variables successfully pushed to the backend")
    else:
        print("Failed to push environment variables to backend with status code: ", response.status_code)
        print(response.text)
