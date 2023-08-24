from __future__ import annotations
from beanie import Document


from models.alert_model import AlertModel


class CurrentAlertsList(Document):
    alerts: list[AlertModel]

    class Settings:
        name = 'current-alerts-list'
