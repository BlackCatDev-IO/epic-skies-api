from typing import Optional, Annotated

import fastapi

from models.app_alert_notice import AppAlertNotice
from models.config_model import ConfigModel
from models.current_alerts_list_model import CurrentAlertsList
from models.user_model import UserModel
from services import user_service
from services.app_alert_notice_service import insert_app_alert_notice
from services.auth_service import validate_token
from services.config_service import get_config
from services import nws_service
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

router = fastapi.APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get('/')
async def root() -> dict:
    return {"status": "ok"}


@router.post('/adduser', status_code=201)
async def add_user(user: UserModel,token: Annotated[str, Depends(oauth2_scheme)]) -> UserModel:
    try:
        validate_token(token)
        new_user = await user_service.insert_user(user)
        return new_user
    except Exception as e:
        print(e)
        raise e


@router.get('/users')
async def get_all_users(token: Annotated[str, Depends(oauth2_scheme)]) -> list[UserModel]:
    try:
        validate_token(token)
        new_user = await user_service.get_all_users()
        return new_user
    except Exception as e:
        print(e)
        raise e


@router.get('/alerts')
async def get_alerts(token: Annotated[str, Depends(oauth2_scheme)]) -> Optional[CurrentAlertsList]:
    try:
        validate_token(token)
        return await nws_service.query_alerts()
    except Exception as e:
        print(e)
        raise e


@router.post('/app-alert-notice', status_code=201)
async def log_app_alert(alert_notice: AppAlertNotice, token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    try:
        validate_token(token)
        alert = await insert_app_alert_notice(alert_notice)

        return {
            "id": str(alert.id),
            "created_at": alert.created_date,
            "precip_notice": alert.precip_notice,
            "alert_notice": alert.alert
        }
    except Exception as e:
        print(e)
        raise e


@router.get('/config')
async def get_remote_config() -> ConfigModel:
    new_config = await get_config()

    return new_config
