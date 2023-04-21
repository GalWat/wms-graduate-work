from api_clients.base_client import BaseClient
from config import settings
from .aggregated_info import AggregatedInfoHandlers


class InventoryClient(BaseClient):
    def __init__(self, **kwargs):
        super().__init__(service_url=settings.inventory_service.host, **kwargs)

        self.aggregated_info = AggregatedInfoHandlers(self)
