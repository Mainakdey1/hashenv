from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV_STORE: str
    API_URL: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()