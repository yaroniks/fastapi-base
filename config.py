from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(Path(__file__).parent) + '\.env', env_file_encoding='utf-8', extra='ignore')

    TITLE: str
    VERSION: str
    ROOT_PATH: str

    SQL_URL: str

    RABITMQ_HOST: str
    RABITMQ_PORT: int

    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_USER: str
    MONGODB_PASSWORD: str


settings = Settings()
