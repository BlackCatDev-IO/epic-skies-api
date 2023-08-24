from config.config import settings
from models.config_model import ConfigModel
from services import sentry_service


async def get_config() -> ConfigModel:
    try:
        remote_config_id = settings.CONFIG_ID
        remote_config = await ConfigModel.get(remote_config_id)

        return remote_config
    except Exception as e:
        sentry_service.capture_exception(f'{e}')
