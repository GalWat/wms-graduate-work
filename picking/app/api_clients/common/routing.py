from api_clients.base_handlers import BaseHandlers


class RoutingHandlers(BaseHandlers):
    def all_distances_v1(self):
        handler = "routing/all-distances"
        return eval(self.client.get(handler))

    def map_locations_into_floor_coordinates_v1(self, location_ids: list[int]):
        handler = "routing/map-locations-into-floor-coordinates"
        return eval(self.client.post(handler, json=location_ids))

    def post_warehouse_plan_v1(self, location_ids: list[int]):
        handler = "routing/warehouse-plan"
        return self.client.post(handler, json=location_ids)
