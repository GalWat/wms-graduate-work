from api_clients.base_handlers import BaseHandlers


class LocationsHandlers(BaseHandlers):
    def group_units_into_locations_v1(self, unit_barcodes: list[str]):
        handler = "locations/group-units-into-locations"
        json = unit_barcodes
        return self.client.post(handler, json)
