from api_clients.inventory import InventoryClient
from api_clients.common import CommonClient
from collections import Counter


def get_location_sets(counts_by_sku: dict[int, int]):
    count_by_locations = get_all_locations_with_skus(list(counts_by_sku.keys()))
    result = generate_suitable_location_sets(count_by_locations, counts_by_sku)
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

        count_by_locations[location["location_id"]] = dict(count)

    return count_by_locations


def generate_suitable_location_sets(count_by_locations, counts_by_sku: dict[int, int]):
    needed_sku_counts = Counter(counts_by_sku)

    suitable_sets = []

    all_sets = [(set(), Counter())]
    for location_id, loc_counts in count_by_locations.items():
        current_len = len(all_sets)
        for locs_set, counter in all_sets[:current_len]:
            new_locs_set = locs_set | {location_id}
            if any([suitable.issubset(new_locs_set) for suitable in suitable_sets]):
                continue

            new_counter = counter + Counter(loc_counts)
            if new_counter >= needed_sku_counts:
                suitable_sets.append(new_locs_set)
                continue

            all_sets.append((new_locs_set, new_counter))

    filtered_suitable_sets = []
    for i, suitable_set in enumerate(suitable_sets):
        if any([suitable.issubset(suitable_set) for suitable in suitable_sets[:i]]):
            continue
        filtered_suitable_sets.append(suitable_set)

    return filtered_suitable_sets
