from models.log_model import LogModel


async def insert_log(log: LogModel) -> LogModel:
    try:
        return await LogModel.insert(log)
    except Exception as e:
        print(e)
        raise e


async def get_all_logs() -> list[LogModel]:
    try:
        return await LogModel.find_all().to_list()
    except Exception as e:
        print(e)
        raise e