from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    DEBUG: bool
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_PORT: int = 5432
    DB_HOST: str = "localhost"

    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent / ".env")

    @property
    def DB_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:"
            f"{self.DB_PASSWORD.get_secret_value()}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
