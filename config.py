from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    TITLE: str
    VERSION: str
    ROOT_PATH: str

    SQL_URL: str

    RABITMQ_HOST: str
    RABITMQ_PORT: int


settings = Settings()
