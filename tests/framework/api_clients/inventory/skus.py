from tests.framework.api_clients.base_handlers import BaseHandlers


class SkusHandlers(BaseHandlers):
    def create_v1(self, name: str):
        handler = "skus/create"
        json = {"name": name}
        return self.client.post(handler, json)

    def get_v1(self, sku_id):
        handler = f"skus/{sku_id}"
        return self.client.get(handler)
