from .base_queries import BaseQueries


class LocationGroupsQueries(BaseQueries):
    def insert_location_group(self, name: str) -> dict:
        query = "INSERT INTO location_groups VALUES (DEFAULT, %s) RETURNING id"
        return self.execute(query, (name,))[0]

    def select_location_group(self, location_group_id: int) -> dict:
        query = "SELECT id, name FROM location_groups WHERE id = %s"
        return self.execute(query, (location_group_id,))[0]
