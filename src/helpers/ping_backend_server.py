import requests
from core.config import settings

SERVER_URL = settings.SERVER_URL

def ping_backend_server():
    try: 
        response = requests.get(f"{SERVER_URL}/health")
        if response.status_code == 200:
            print('Server is healthy!')
        else:
            print(f'Server responded with status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error connecting to server: {e}')


