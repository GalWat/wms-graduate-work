from itertools import combinations

from api_clients.inventory import InventoryClient
from api_clients.common import CommonClient
from collections import Counter


def get_location_sets(counts_by_sku: dict[int, int]):
    common = CommonClient()
    distances = common.routing.all_distances_v1()

    count_by_locations = get_all_locations_with_skus(list(counts_by_sku.keys()))
    locations = list(count_by_locations.keys())
    locations_coordinates = common.routing.map_locations_into_floor_coordinates_v1(locations)
    result = find_best_locations_set(count_by_locations, counts_by_sku, distances, locations_coordinates)
    return result


def get_all_locations_with_skus(sku_ids: list[int]):
    inventory = InventoryClient()
    common = CommonClient()

    units_resp = inventory.aggregated_info.find_skus_in_units_v1(sku_ids)
    unit_barcodes = [unit["unit_barcode"] for unit in units_resp]
    locations_resp = common.locations.group_units_into_locations_v1(unit_barcodes)

    counts_by_units = {
        unit["unit_barcode"]: {sku["sku_id"]: sku["count"] for sku in unit["skus"]}
        for unit in units_resp
    }

    count_by_locations = {}
    for location in locations_resp:
        count = Counter()
        for unit_barcode in location["unit_barcodes"]:
            count.update(counts_by_units[unit_barcode])

        count_by_locations[location["location_id"]] = count

    return count_by_locations


def find_best_locations_set(count_by_locations, counts_by_sku: dict[int, int], distances, location_coords):
    needed_sku_counts = Counter(counts_by_sku)
    locations = list(count_by_locations.keys())
    locations_len = len(locations)

    c_min = float("inf")
    min_locations_set = set()

    current_layer = [[(set(), Counter())]]
    for i in range(locations_len):
        next_layer = []

        for j, group in enumerate(current_layer):
            for k, locations_value in enumerate(group):
                locs_set, counter = locations_value
                if locs_set is None:
                    continue
                if i + j + k >= locations_len:
                    break

                new_group = []
                for loc in locations[i+j+k:]:
                    new_locs_set = locs_set | {loc}
                    new_counter = counter + count_by_locations[loc]
                    c = criteria_func(new_locs_set, distances, location_coords)
                    if c >= c_min:
                        new_group.append((None, None))
                    elif new_counter >= needed_sku_counts:
                        c_min = c
                        min_locations_set = new_locs_set
                        new_group.append((None, None))
                    else:
                        new_group.append((new_locs_set, new_counter))

                next_layer.append(new_group)

        current_layer = next_layer

    return min_locations_set


def criteria_func(locations: set, distances, location_coords):
    distances_between_locations = []
    for loc1, loc2 in combinations(locations, 2):
        loc1_coords = location_coords[loc1]
        loc2_coords = location_coords[loc2]
        distances_between_locations.append(distances[loc1_coords][loc2_coords])

    return sum(sorted(distances_between_locations, reverse=True)[:len(locations)-1])
