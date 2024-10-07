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


async def add_mock_response(key: str, mock: dict) -> MockResponseModel:
    try:
        default_location_ny = {
            "localCoordinates": {
                "lat": 40.826,
                "long": -73.925
            }
        }

        new_mock = MockResponseModel(weather_kit=mock, key=key, location=default_location_ny)

        return await MockResponseModel.insert(new_mock)
    except Exception as e:
        print(e)
        raise e
