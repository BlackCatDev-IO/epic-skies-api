from models.user_model import UserModel


async def insert_user(user: UserModel) -> UserModel:
    try:
        new_user = await UserModel.insert_one(user)
        return new_user
    except Exception as e:
        print(e)


async def get_all_users() -> list[UserModel]:
    users = await UserModel.find_all().to_list()
    return users
