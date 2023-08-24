from models.user_model import UserModel
from services import sentry_service


async def insert_user(user: UserModel) -> UserModel:
    try:
        new_user = await UserModel.insert_one(user)
        return new_user
    except Exception as e:
        sentry_service.capture_exception(f'{e}')


async def get_all_users() -> list[UserModel]:
    try:
        users = await UserModel.find_all().to_list()
        return users
    except Exception as e:
        sentry_service.capture_exception(f'{e}')

