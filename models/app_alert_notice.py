from datetime import datetime
from typing import Optional

from beanie import Document
from pydantic import Field


class AppAlertNotice(Document):
    created_date: datetime = Field(
        default_factory=datetime.now)
    precip_notice: Optional[str] = None
    alert: Optional[str] = None
    weather_kit_response: dict

    class Settings:
        name = "app_alert_notices"
        index = []
