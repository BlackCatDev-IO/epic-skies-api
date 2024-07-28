import uvicorn
from fastapi import FastAPI
from api import epic_skies_api
from config.config import settings
from infrastructure import mongo_setup
from services import config_service
from services import nws_service
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from services import sentry_service
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(fast_api: FastAPI):
    await mongo_setup.init_connection()
    sentry_service.init_sentry()
    await init_interval_calls()
    yield


app = FastAPI(lifespan=lifespan)


def main():
    configure_routing()
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)


def configure_routing():
    app.include_router(epic_skies_api.router)


async def init_interval_calls():
    config = await config_service.get_config()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(nws_service.query_alerts, 'interval', seconds=config.interval_in_sec)
    scheduler.start()


if __name__ == '__main__':
    main()
else:
    configure_routing()
