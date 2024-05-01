import socket
import beanie
import motor.motor_asyncio

from config.config import settings
from models.app_alert_notice import AppAlertNotice
from models.config_model import ConfigModel
from models.current_alerts_list_model import CurrentAlertsList
from models.log_model import LogModel
from models.user_model import UserModel


async def init_connection(db_name: str):
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URL)
        model_list = [UserModel, ConfigModel, CurrentAlertsList, AppAlertNotice, LogModel]

        await beanie.init_beanie(database=client[db_name], document_models=model_list)

        print("Connected to db")
    except Exception as e:
        print(f'Error: {e}')
        raise Exception(e)
