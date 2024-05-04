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


async def init_connection(db_name: str):
    try:
        connection_string = settings.MONGO_URL_LOCAL if is_local_host() else settings.MONGO_URL
        client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
        model_list = [UserModel, ConfigModel, CurrentAlertsList, AppAlertNotice, LogModel, MockResponseModel]

        await beanie.init_beanie(database=client[db_name], document_models=model_list)

        print("Connected to db")
    except Exception as e:
        print(f'Error: {e}')
        raise Exception(e)
