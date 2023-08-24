import beanie
import motor.motor_asyncio

from config.config import settings
from models.config_model import ConfigModel
from models.current_alerts_list_model import CurrentAlertsList
from models.user_model import UserModel


async def init_connection(db_name: str):
    mongo_conn_str = f'{settings.MONGO_URL}{db_name}?retryWrites=true&w=majority'

    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(mongo_conn_str)
        model_list = [UserModel, ConfigModel, CurrentAlertsList]
        await beanie.init_beanie(database=client[db_name], document_models=model_list)
        print(f"Connected to db")
    except Exception as e:
        print(f'Error: {e}')
        raise Exception(e)
