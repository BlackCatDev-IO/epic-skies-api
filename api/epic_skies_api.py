import fastapi

from models.user_model import UserModel
from services import user_service

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

