from pathlib import Path
from dotenv import dotenv_values

def get_env_variables_from_local():
    env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"
    env_data = dotenv_values(env_path)
    return env_data
