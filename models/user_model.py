import datetime

from beanie import Document
from pydantic import Field


class UserModel(Document):
    created_date: datetime.datetime = Field(
        default_factory=datetime.datetime.now)
    device_id: str
    operating_system: str

    class Settings:
        name = 'users'
        index = []
