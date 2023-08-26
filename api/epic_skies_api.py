from typing import Optional

import fastapi

from models.config_model import ConfigModel
from models.current_alerts_list_model import CurrentAlertsList
from models.user_model import UserModel
from services import user_service
from services.config_service import get_config
from services import nws_service

router = fastapi.APIRouter()


@router.get('/')
async def root() -> dict:
    return {"status": "ok"}


@router.post('/adduser', status_code=201)
async def add_user(user: UserModel) -> UserModel:
    try:
        new_user = await user_service.insert_user(user)
        return new_user
    except Exception as e:
        print(e)


@router.get('/users')
async def get_all_users() -> list[UserModel]:
    try:
        new_user = await user_service.get_all_users()
        return new_user
    except Exception as e:
        print(e)


@router.get('/alerts')
async def get_alerts() -> Optional[CurrentAlertsList]:
    try:
        return await nws_service.query_alerts()
    except Exception as e:
        print(e)


@router.get('/config')
async def get_remote_config() -> ConfigModel:
    new_config = await get_config()

    return new_config
