import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api import epic_skies_api

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
async def startup_event():
    pass


if __name__ == '__main__':
    main()
else:
    configure_routing()
