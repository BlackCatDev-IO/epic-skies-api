from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_PORT: str
    DB_NAME: str
    SERVER_IP: str
    CONFIG_ID: str
    CURRENT_ALERTS_LIST_ID: str
    SENTRY_URL: str
    MIX_PANEL_TOKEN: str
    APP_MAX: int = 100
    IS_PROD_ENV: bool
    ACCESS_TOKEN: str

    class Config:
        env_file = ".env"
        extra = 'ignore'


settings = Settings()
