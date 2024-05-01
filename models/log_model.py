from datetime import datetime
from typing import Optional

from beanie import Document
from pydantic import Field


class LogModel(Document):
    created_date: datetime = Field(
        default_factory=datetime.now)
    log: str
    data: Optional[dict] = None

    class Settings:
        name = "logs"
        index = []
