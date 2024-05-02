from fastapi import HTTPException

from models.mock_response_model import MockResponseModel


async def get_mock_response(key: str) -> MockResponseModel:
    try:
        mock = await MockResponseModel.find(MockResponseModel.key == key).first_or_none()

        if mock is None:
            raise HTTPException(status_code=404, detail="Mock not found")

        return mock
    except Exception as e:
        print(e)
        raise e
