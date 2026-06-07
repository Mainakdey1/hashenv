from pathlib import Path
from dotenv import dotenv_values

def get_env_variables_from_local():
    env_path = Path.cwd() / ".env"
    env_data = dotenv_values(env_path)
    return env_data
