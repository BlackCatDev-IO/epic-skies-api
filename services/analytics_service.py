from typing import Optional

from mixpanel import Mixpanel

from config.config import settings

mixpanel = Mixpanel(settings.MIX_PANEL_TOKEN)


def report_analytics_event(event: str, props: Optional[dict] = None):
    if settings.IS_PROD_ENV:
        mixpanel.track(distinct_id='epic-skies-api', event_name=event, properties=props)
        print(f'analytics: {event}')
