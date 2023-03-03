from tests.framework.api_clients.base_handlers import BaseHandlers


class UnitsHandlers(BaseHandlers):
    def create_v1(self, type_id: int, location_id: int):
        handler = "units/create"
        json = {"type_id": type_id, "location_id": location_id}
        return self.client.post(handler, json)

    def get_v1(self, unit_id):
        handler = f"units/{unit_id}"
        return self.client.get(handler)
