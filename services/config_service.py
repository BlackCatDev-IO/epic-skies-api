from config.config import settings
from models.config_model import ConfigModel
from services import sentry_service


async def get_config() -> ConfigModel:
    try:
        return await ConfigModel.get(settings.CONFIG_ID)
    except Exception as e:
        sentry_service.capture_exception(repr(e))
