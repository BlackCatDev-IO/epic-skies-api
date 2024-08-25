from urllib.parse import urlencode

import beanie
import motor.motor_asyncio

from config.config import settings
from models.app_alert_notice import AppAlertNotice
from models.config_model import ConfigModel
from models.current_alerts_list_model import CurrentAlertsList
from models.log_model import LogModel
from models.mock_response_model import MockResponseModel
from models.user_model import UserModel
import socket


def is_local_host() -> bool:
    try:
        hostname = socket.gethostname()
        # gethostname returns computer name on Macs
        return "Loren" in hostname
    except Exception as e:
        print(e)
        return False


def get_connection_string() -> str:
    base_url = f'mongodb://{settings.DB_USER}:{settings.DB_PASS}'

    params = {
        "retryWrites": "true",
        "loadBalanced": "false",
        "serverSelectionTimeoutMS": "5000",
        "connectTimeoutMS": "10000",
        "authSource": settings.DB_NAME,
        "authMechanism": "SCRAM-SHA-256"
    }

    param_string = urlencode(params)

    if is_local_host():
        return f'{base_url}@{settings.SERVER_IP}:{settings.DB_PORT}/{settings.DB_NAME}?{param_string}'
    else:
        return f'{base_url}@mongodb:{settings.DB_PORT}/{settings.DB_NAME}?{param_string}'


async def init_connection():
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(get_connection_string())
        model_list = [UserModel, ConfigModel, CurrentAlertsList, AppAlertNotice, LogModel, MockResponseModel]

        await beanie.init_beanie(database=client[settings.DB_NAME], document_models=model_list)

        print(f'INFO: Connected to MongoDB')
    except Exception as e:
        print(f'Error: {e}')
        raise e
