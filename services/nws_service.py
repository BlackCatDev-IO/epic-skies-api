import httpx

from services import config_service


async def query_alerts():
    config = await config_service.get_config()
    if not config.interval_query_on:
        return

    try:
        url = "https://api.weather.gov/alerts/active"
        headers = {
            "User-Agent": "Epic Skies App"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            return response.json()

    except Exception as e:
        print(e)

