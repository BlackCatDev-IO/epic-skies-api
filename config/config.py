from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str
    MONGO_URL_LOCAL: str
    CONFIG_ID: str
    CURRENT_ALERTS_LIST_ID: str
    SENTRY_URL: str
    MIX_PANEL_TOKEN: str
    APP_MAX: int = 100
    IS_PROD_ENV: bool

    class Config:
        env_file = ".env"


settings = Settings()
