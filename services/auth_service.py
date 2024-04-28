from fastapi import HTTPException

from config.config import settings


def validate_token(token: str) -> dict:
    if token != settings.ACCESS_TOKEN:
        raise HTTPException(status_code=401, detail="Not Authorized")

    return {"token": token}

