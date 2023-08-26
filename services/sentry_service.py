import sentry_sdk
from config.config import settings
from sentry_sdk import capture_message


def init_sentry():
    if settings.IS_PROD_ENV:

        sentry_sdk.init(
            dsn=settings.SENTRY_URL,

            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production,
            traces_sample_rate=1.0,
        )
        print('Sentry Initialized')


def capture_exception(message: str):
    if settings.IS_PROD_ENV:
        print(message)
        capture_message(message)
