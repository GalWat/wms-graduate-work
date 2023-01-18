from .base_queries import BaseQueries


class UnitsQueries(BaseQueries):
    def insert_unit(self, barcode: str, type_id: int, current_location_id: int) -> dict:
        query = "INSERT INTO units VALUES (DEFAULT, %s, %s, %s) RETURNING id"
        return self.execute(query, (barcode, type_id, current_location_id))[0]

    def select_unit(self, unit_id: int) -> dict:
        query = "SELECT id, barcode, type_id, current_location_id, target_location_id FROM units WHERE id = %s"
        return self.execute(query, (unit_id,))[0]

    def update_unit_barcode(self, unit_id: int, barcode: str) -> dict:
        query = "UPDATE units SET barcode = %s WHERE id = %s"
        return self.execute(query, (barcode, unit_id))
