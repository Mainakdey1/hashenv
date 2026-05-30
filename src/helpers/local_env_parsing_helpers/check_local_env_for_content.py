from pathlib import Path
from dotenv import dotenv_values

def check_local_env_for_content():
    env_data = dotenv_values(Path(__file__).resolve().parent.parent.parent.parent / ".env")

    return bool(env_data)