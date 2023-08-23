from models.user_model import UserModel


async def insert_user(user: UserModel) -> UserModel:
    try:
        new_user = await UserModel.insert_one(user)
        return new_user
    except Exception as e:
        print(e)
