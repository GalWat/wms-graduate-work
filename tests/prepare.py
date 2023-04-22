import random

from framework.api_clients.common import CommonClient
from framework.api_clients.inventory import InventoryClient
from multiprocessing import Pool

from tests.framework.constants import LocationTypes, UnitTypes

common_client = CommonClient()
inventory_client = InventoryClient()

# # Create SKUs
sku_ids = [inventory_client.skus.create_v1("Big Red Button")["id"],
           inventory_client.skus.create_v1("Big Blue Button")["id"],
           inventory_client.skus.create_v1("Big Green Button")["id"]]

# Create sector
location_group_id = common_client.location_groups.create_v1("Sector 1")["id"]


def create_rack_and_content(x, y, orientation):
    # Create racks
    location_id = common_client.locations.create_v1(LocationTypes.Rack, location_group_id, x, y, orientation)["id"]

    # Create cells
    for _ in range(2):
        cell_id = common_client.units.create_v1(UnitTypes.Cell, location_id)["id"]
        cell_barcode = common_client.units.get_v1(cell_id)["barcode"]

        # Create products in cells
        for _ in range(random.randint(1, 5)):
            inventory_client.products.create_v1(random.choice(sku_ids), cell_barcode)


def value_gen(width, height):
    orientation = 2
    for x in range(1, width):
        if x % 3 == 0:
            continue
        orientation = 0 if orientation == 2 else 2

        for y in range(1, height):
            if y % 5 == 0:
                continue

            yield x, y, orientation


with Pool(8) as p:
    p.starmap(create_rack_and_content, value_gen(9, 6))
