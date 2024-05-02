from beanie import Document


class MockResponseModel(Document):
    key: str
    location: dict
    weather_kit: dict

    class Settings:
        name = 'mocks'
        index = []
