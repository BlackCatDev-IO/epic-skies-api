import httpx

from typing import Optional
from config.config import settings
from models.alert_model import AlertModel
from models.current_alerts_list_model import CurrentAlertsList
from services import config_service, analytics_service
from services import sentry_service
from enum import Enum


class AnalyticsEvents(Enum):
    ALERTS_SUCCESS = 'alerts_updated_successfully'
    ALERTS_ERROR = 'alerts_error'


async def fetch_alerts_from_api() -> Optional[CurrentAlertsList]:
    try:
        async with httpx.AsyncClient() as client:
            url = "https://api.weather.gov/alerts/active"
            headers = {
                "User-Agent": "Epic Skies App"
            }
            response = await client.get(url, headers=headers)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            alerts = response.json()['features']
            if alerts is None:
                return None
            alert_models = [AlertModel(**alert) for alert in alerts]
            return CurrentAlertsList(alerts=alert_models)
    except Exception as e:
        exception_string = repr(e)
        error = f"An error occurred: {exception_string}"
        analytics_service.report_analytics_event(f'alerts_update_error {error}')
        sentry_service.capture_exception(error)


async def query_alerts() -> Optional[CurrentAlertsList]:
    config = await config_service.get_config()
    if not config.interval_query_on:
        return None

    try:
        latest_alerts = await fetch_alerts_from_api()
        print(latest_alerts)

        if latest_alerts is None:
            return None

        updated_alert_list_from_storage = await CurrentAlertsList.get(settings.CURRENT_ALERTS_LIST_ID)

        if updated_alert_list_from_storage.alerts is not None:
            updated_alert_list_from_storage.alerts = latest_alerts.alerts

        await updated_alert_list_from_storage.save()

        analytics_service.report_analytics_event(AnalyticsEvents.ALERTS_SUCCESS.value)

        return updated_alert_list_from_storage

    except httpx.HTTPError as http_err:
        error = f"HTTP error occurred: {repr(http_err)}"
        sentry_service.capture_exception(error)
        analytics_service.report_analytics_event(f'alerts_update_error {error}')

    except Exception as e:
        error = f"An error occurred: {repr(e)}"
        analytics_service.report_analytics_event(f'alerts_update_error {error}')
        sentry_service.capture_exception(error)
