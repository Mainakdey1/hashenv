#recieves env from endpoint. This function has already recieved what repository to target and what env file it needs to fetch
from core.config import settings

def env_recieve(env_data: dict):

    with open(".env", "w") as f:
        for key, value in env_data.items():
            f.write(f'{key}="{value}"\n')
    print("Environment variables have been written to local .env file")

    