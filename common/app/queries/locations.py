from .base_queries import BaseQueries


class LocationsQueries(BaseQueries):
    def insert_location(self, barcode: str, type_id: int, group_id: int, x: int, y: int) -> dict:
        query = "INSERT INTO locations VALUES (DEFAULT, %s, %s, %s, %s, %s) RETURNING id"
        return self.execute(query, (barcode, type_id, group_id, x, y))[0]

    def select_location(self, location_id: int) -> dict:
        query = "SELECT id, barcode, type_id, group_id, x, y FROM locations WHERE id = %s"
        return self.execute(query, (location_id,))[0]

    def update_location_barcode(self, location_id: int, barcode: str) -> None:
        query = "UPDATE locations SET barcode = %s WHERE id = %s"
        self.execute(query, (barcode, location_id))
