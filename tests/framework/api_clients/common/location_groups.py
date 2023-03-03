from tests.framework.api_clients.base_handlers import BaseHandlers


class LocationGroupsHandlers(BaseHandlers):
    def create_v1(self, name: str):
        handler = "location_groups/create"
        json = {"name": name}
        return self.client.post(handler, json)

    def get_v1(self, location_group_id):
        handler = f"location_groups/{location_group_id}"
        return self.client.get(handler)
