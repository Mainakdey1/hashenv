#recieves env from endpoint. This function has already recieved what repository to target and what env file it needs to fetch
import os
from core.config import settings

def env_recieve(repository_name):
    ENV_STORE = settings.ENV_STORE

    path = os.path.join(ENV_STORE, f"{repository_name}")
    if not os.path.exists(path):
        print("Env file not found")
        return

    env_data = {}

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)

            env_data[key] = value


    with open(".env", "w") as f:
        for key, value in env_data.items():
            f.write(f"{key}={value}\n")

    