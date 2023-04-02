import random

from framework.api_clients.common import CommonClient
from framework.api_clients.inventory import InventoryClient
from itertools import product

from tests.framework.constants import LocationTypes, UnitTypes

common_client = CommonClient()
inventory_client = InventoryClient()

# Create SKUs
sku_ids = [inventory_client.skus.create_v1("Big Red Button")["id"],
           inventory_client.skus.create_v1("Big Blue Button")["id"],
           inventory_client.skus.create_v1("Big Green Button")["id"]]

# Create sector
location_group_id = common_client.location_groups.create_v1("Sector 1")["id"]

# Create racks
for x, y in product([1, 2, 3], [1, 2, 3]):
    location_id = common_client.locations.create_v1(LocationTypes.Rack, location_group_id, x, y)["id"]

    # Create cells
    for _ in range(10):
        cell_id = common_client.units.create_v1(UnitTypes.Cell, location_id)["id"]
        cell_barcode = common_client.units.get_v1(cell_id)["barcode"]

        # Create products in cells
        for _ in range(random.randint(1, 5)):
            inventory_client.products.create_v1(random.choice(sku_ids), cell_barcode)
