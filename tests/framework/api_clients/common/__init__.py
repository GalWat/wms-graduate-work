from tests.framework.api_clients.base_client import BaseClient
from .location_groups import LocationGroupsHandlers
from .locations import LocationsHandlers
from .units import UnitsHandlers


class CommonClient(BaseClient):
    def __init__(self, **kwargs):
        super().__init__(service_url="galwat-remote.ydns.eu/common", **kwargs)

        self.location_groups = LocationGroupsHandlers(self)
        self.locations = LocationsHandlers(self)
        self.units = UnitsHandlers(self)

