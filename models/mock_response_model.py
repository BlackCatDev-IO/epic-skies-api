from typing import Optional

from beanie import Document


class MockResponseModel(Document):
    key: str
    location: dict
    weather_kit: dict
    visualCrossing: Optional[dict] = None

    class Settings:
        name = 'mocks'
        index = []
