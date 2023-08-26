import datetime
from typing import Optional

from beanie import Document
from pydantic import Field
from models.alert_model import AlertModel


def default_notified_alerts():
    return []


class UserModel(Document):
    created_date: datetime.datetime = Field(
        default_factory=datetime.datetime.now)
    device_id: str
    purchase_id: Optional[str] = None
    operating_system: str
    is_trial: bool = Field(default=True)
    notified_alerts: list[AlertModel] = Field(default_factory=list)

    class Settings:
        name = 'users'
        index = []
