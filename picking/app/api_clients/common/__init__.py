from api_clients.base_client import BaseClient
from .locations import LocationsHandlers
from .routing import RoutingHandlers
from config import settings


class CommonClient(BaseClient):
    def __init__(self, **kwargs):
        super().__init__(service_url=settings.common_service.host, **kwargs)

        self.locations = LocationsHandlers(self)
        self.routing = RoutingHandlers(self)
