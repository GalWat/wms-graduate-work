from .base_queries import BaseQueries


class LocationsQueries(BaseQueries):
    def insert_location(self, barcode: str, type_id: int, group_id: int, x: int, y: int, orientation: int) -> dict:
        query = "INSERT INTO locations VALUES (DEFAULT, %s, %s, %s, %s, %s, %s) RETURNING id"
        return self.execute(query, (barcode, type_id, group_id, x, y, orientation))[0]

    def select_location(self, location_id: int) -> dict:
        query = "SELECT id, barcode, type_id, group_id, x, y, orientation FROM locations WHERE id = %s"
        return self.execute(query, (location_id,))[0]

    def select_locations(self, location_ids: tuple[int]) -> dict:
        query = "SELECT id, barcode, type_id, group_id, x, y, orientation FROM locations WHERE id IN %s"
        return self.execute(query, (location_ids,))

    def update_location_barcode(self, location_id: int, barcode: str) -> None:
        query = "UPDATE locations SET barcode = %s WHERE id = %s"
        self.execute(query, (barcode, location_id))

    def select_locations_by_units(self, unit_barcodes: tuple[str]) -> list[dict]:
        query = """SELECT u.barcode as unit_barcode, u.current_location_id as location_id, l.x, l.y
                    FROM units as u
                    RIGHT JOIN locations l on l.id = u.current_location_id
                    WHERE u.type_id = 1
                    AND u.barcode IN %s"""
        return self.execute(query, (unit_barcodes,))

    def select_locations_by_type(self, type_id: int) -> list[dict]:
        query = "SELECT id, x, y, orientation FROM locations WHERE type_id = %s"
        return self.execute(query, (type_id,))
