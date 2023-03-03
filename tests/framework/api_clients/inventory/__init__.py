from tests.framework.api_clients.base_client import BaseClient
from .skus import SkusHandlers
from .products import ProductsHandlers


class InventoryClient(BaseClient):
    def __init__(self, **kwargs):
        super().__init__(service_url="galwat-remote.ydns.eu/inventory", **kwargs)

        self.skus = SkusHandlers(self)
        self.products = ProductsHandlers(self)

