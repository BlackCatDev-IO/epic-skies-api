import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api import epic_skies_api
from infrastructure import mongo_setup
from services import config_service
from services import nws_service
from apscheduler.schedulers.asyncio import AsyncIOScheduler


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def main():
    configure_routing()
    uvicorn.run(app)


def configure_routing():
    app.include_router(epic_skies_api.router)


@app.on_event("startup")
async def configure_db():
    await mongo_setup.init_connection('epic-skies-db')
    await init_interval_calls()


async def init_interval_calls():
    config = await config_service.get_config()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(nws_service.query_alerts, 'interval', seconds=config.interval_in_sec)
    scheduler.start()


if __name__ == '__main__':
    main()
else:
    configure_routing()
