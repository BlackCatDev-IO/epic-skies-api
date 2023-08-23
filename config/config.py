from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str
    APP_MAX: int = 100

    class Config:
        env_file = ".env"


settings = Settings()
