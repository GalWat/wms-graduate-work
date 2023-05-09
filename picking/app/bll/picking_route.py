from api_clients.inventory import InventoryClient
from api_clients.common import CommonClient
from collections import Counter


def get_location_sets(counts_by_sku: dict[int, int]):
    common = CommonClient()
    distances = common.routing.all_distances_v1()

    count_by_locations = get_all_locations_with_skus(list(counts_by_sku.keys()))
    locations = list(count_by_locations.keys())
    locations_coordinates = common.routing.map_locations_into_floor_coordinates_v1(locations)

    count_by_floor = map_counts_to_floor_coords(count_by_locations, locations_coordinates)

    result = find_best_locations_set(count_by_floor, counts_by_sku, distances)
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


def map_counts_to_floor_coords(count_by_locations, locations_coordinates):
    count_by_floor = {}
    for location, count in count_by_locations.items():
        coords = locations_coordinates[location]
        if coords not in count_by_floor:
            count_by_floor[coords] = count
        else:
            count_by_floor[coords] += count

    return count_by_floor


def find_best_locations_set(count_by_locations, counts_by_sku: dict[int, int], distances):
    needed_sku_counts = Counter(counts_by_sku)
    locations = list(count_by_locations.keys())
    locations_len = len(locations)

    global_c_max = float("inf")
    locations_sets = []
    events = []

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
                    c_min = mst_length(new_locs_set, distances)

                    if c_min > global_c_max:
                        new_group.append((None, None))
                    elif new_counter >= needed_sku_counts:
                        new_group.append((None, None))
                        index = len(locations_sets)
                        locations_sets.append(new_locs_set)
                        c_max = closest_neighbour_path(new_locs_set, distances)
                        global_c_max = min(c_max, global_c_max)
                        events.append((c_min, 0, index))
                        events.append((c_max, 1, index))
                    else:
                        new_group.append((new_locs_set, new_counter))

                next_layer.append(new_group)

        current_layer = next_layer

    events.sort()
    result = []
    for c_val, event_type, index in events:
        if event_type == 1:
            break

        result.append(locations_sets[index])

    return result[0]


def mst_length(locations: set, distances):
    res = 0
    unvisited = locations.copy()
    visited = [unvisited.pop()]

    while len(unvisited) > 0:
        new_v = None
        new_dist = float("inf")

        for v in visited:
            for possible_v in unvisited:
                dist = distances[v][possible_v]
                if dist < new_dist:
                    new_dist = dist
                    new_v = possible_v

        unvisited.remove(new_v)
        visited.append(new_v)
        res += new_dist

    return res


def closest_neighbour_path(locations: set, distances):
    res = 0
    unvisited = locations.copy()
    v = unvisited.pop()

    while len(unvisited) > 0:
        new_v = None
        new_dist = float("inf")

        for possible_v in unvisited:
            dist = distances[v][possible_v]
            if dist < new_dist:
                new_dist = dist
                new_v = possible_v

        unvisited.remove(new_v)
        v = new_v
        res += new_dist

    return res


def ga_shortest_path():
    pass
