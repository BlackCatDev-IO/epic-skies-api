from beanie import Document


class ConfigModel(Document):
    interval_query_on: bool
    interval_in_sec: int

    class Settings:
        name = 'remote-config'
        index = []
