from models.app_alert_notice import AppAlertNotice


async def insert_app_alert_notice(alert_notice: AppAlertNotice) -> AppAlertNotice:
    try:
        return await AppAlertNotice.insert(alert_notice)
    except Exception as e:
        print(e)
        raise e
