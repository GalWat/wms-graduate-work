from .base_queries import BaseQueries


class SettingsQueries(BaseQueries):
    def insert(self, key: str, value: dict):
        query = "INSERT INTO settings (key, value) VALUES (%s, %s)"
        self.execute(query, (key, value))

    def read(self, key: str, json_path: list[str]):
        query = "SELECT value #>> %s as value FROM settings WHERE key = %s"
        return self.execute(query, (json_path, key))[0]["value"]

    def update(self, key: str, json_path: list[str], value: str | int | float | bool):
        value = str(value)
        query = "update settings set value = jsonb_set(value, %s, %s) where key = %s"
        self.execute(query, (json_path, value, key))
