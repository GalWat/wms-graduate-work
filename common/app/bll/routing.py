from queries.locations import LocationsQueries
from queries.settings import SettingsQueries
from copy import deepcopy
from itertools import product

diff_by_orientation = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}


def calculate_distance_between_all():
    query_result = LocationsQueries().select_locations_by_type(type_id=2)  # Rack
    warehouse_width = int(SettingsQueries().read("warehouse_size", ["width"]))
    warehouse_height = int(SettingsQueries().read("warehouse_size", ["height"]))

    waypoints = {}
    floor_map = [[0 for _ in range(warehouse_height)] for _ in range(warehouse_width)]

    unreachable_val = warehouse_width * warehouse_height

    for location in query_result:
        x, y = location["x"], location["y"]
        floor_map[x][y] = unreachable_val

        x_diff, y_diff = diff_by_orientation[location["orientation"]]
        waypoint_coordinates = (location["x"] + x_diff, location["y"] + y_diff)

        waypoints.setdefault(waypoint_coordinates, set())
        waypoints[waypoint_coordinates].add(location["id"])

    distances = {}
    for waypoint in waypoints:
        distances[waypoint] = calculate_distances_from_waypoint(
            waypoint, waypoints.keys(), floor_map, warehouse_width-1, warehouse_height-1
        )
    return distances


def calculate_distances_from_waypoint(start: tuple[int, int], destinations, floor_map, width, height):
    floor_map = deepcopy(floor_map)
    next_cells = [start]

    for x, y in next_cells:
        for x_diff, y_diff in product([0, 1, -1], [0, 1, -1]):
            if x_diff == 0 and y_diff == 0:
                continue

            new_x, new_y = x + x_diff, y + y_diff
            if new_x < 0 or new_x > width or new_y < 0 or new_y > height or floor_map[new_x][new_y] != 0:
                continue

            floor_map[new_x][new_y] = floor_map[x][y] + 1
            next_cells.append((new_x, new_y))

    result = {}
    for destination in destinations:
        result[destination] = floor_map[destination[0]][destination[1]]

    result[start] = 0
    return result


def map_locations_into_floor_coordinates(location_ids: list[int]):
    query_result = LocationsQueries().select_locations(tuple(location_ids))
    mapping = {}

    for location in query_result:
        x_diff, y_diff = diff_by_orientation[location["orientation"]]
        mapping[location["id"]] = (location["x"] + x_diff, location["y"] + y_diff)

    return mapping
