from api_clients.base_handlers import BaseHandlers


class AggregatedInfoHandlers(BaseHandlers):
    def find_skus_in_units_v1(self, sku_ids: list[int]):
        handler = "aggregated-info/find-skus-in-units"
        json = sku_ids
        return self.client.post(handler, json)
