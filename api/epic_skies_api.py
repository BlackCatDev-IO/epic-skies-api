import fastapi

from models.alert_model import AlertModel
from models.user_model import UserModel
from services import user_service
from services.config_service import get_config
from services.nws_service import query_alerts

router = fastapi.APIRouter()


@router.get('/')
async def root():
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
async def get_alerts() -> AlertModel:
    response = await query_alerts()
    features = response['features']
    alert_model = AlertModel(**features[100])

    size = len(features)
    print(size)

    return alert_model


@router.get('/config')
async def get_remote_config():
    new_config = await get_config()

    return new_config
