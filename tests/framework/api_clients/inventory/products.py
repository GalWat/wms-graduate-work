from tests.framework.api_clients.base_handlers import BaseHandlers


class ProductsHandlers(BaseHandlers):
    def create_v1(self, sku_id: int, unit_barcode: str):
        handler = "products/create"
        json = {"sku_id": sku_id, "unit_barcode": unit_barcode}
        return self.client.post(handler, json)

    def get_v1(self, product_id):
        handler = f"products/{product_id}"
        return self.client.get(handler)
