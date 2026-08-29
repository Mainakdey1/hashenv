from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):

    SERVER_URL: str = "https://resign-model-server.onrender.com"
    LOCAL_SERVER_URL: str = "http://localhost:3000"
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )

settings = Settings()