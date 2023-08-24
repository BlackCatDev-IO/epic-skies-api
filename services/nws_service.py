from typing import Optional

import httpx

from config.config import settings
from models.alert_model import AlertModel
from models.current_alerts_list_model import CurrentAlertsList
from services import config_service


async def fetch_alerts_from_api():
    async with httpx.AsyncClient() as client:
        url = "https://api.weather.gov/alerts/active"
        headers = {
            "User-Agent": "Epic Skies App"
        }
        response = await client.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        return response.json()['features']


async def update_current_alerts_in_db(current_alert, alerts_list):
    current_alert.alerts = alerts_list
    await current_alert.save()


async def query_alerts() -> Optional[CurrentAlertsList]:
    config = await config_service.get_config()
    if not config.interval_query_on:
        return None

    try:
        alerts = await fetch_alerts_from_api()
        alert_models = [AlertModel(**alert) for alert in alerts]
        current_alerts_list = CurrentAlertsList(alerts=alert_models)
        updated_alert_list_from_storage = await CurrentAlertsList.get(settings.CURRENT_ALERTS_LIST_ID)

        await update_current_alerts_in_db(updated_alert_list_from_storage, current_alerts_list.alerts)

        return updated_alert_list_from_storage

    except httpx.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"An error occurred: {e}")
