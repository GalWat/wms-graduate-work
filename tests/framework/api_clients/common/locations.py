from tests.framework.api_clients.base_handlers import BaseHandlers


class LocationsHandlers(BaseHandlers):
    def create_v1(self, type_id: int, group_id: int, x: int, y: int):
        handler = "locations/create"
        json = {"type_id": type_id, "group_id": group_id, "x": x, "y": y}
        return self.client.post(handler, json)

    def get_v1(self, location_id):
        handler = f"locations/{location_id}"
        return self.client.get(handler)
