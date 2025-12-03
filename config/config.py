from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    CONFIG_ID: str
    CURRENT_ALERTS_LIST_ID: str
    SENTRY_URL: str
    MIX_PANEL_TOKEN: str
    APP_MAX: int = 100
    IS_PROD_ENV: bool
    ACCESS_TOKEN: str
    APP_PORT: int
    GITHUB_USER: str
    GITHUB_TOKEN: str
    LOCAL_DB: str
    PROD_DB: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra='ignore'
    )


settings = Settings()  # type: ignore[call-arg]
