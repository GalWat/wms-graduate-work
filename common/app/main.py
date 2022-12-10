
from fastapi import FastAPI
from schemas.locations import CreateLocationGroupRequest, GetLocationGroupResponse, CreateLocationGroupResponse
from queries.location_groups import LocationGroupsQueries

app = FastAPI()


@app.post("/location_groups/create", tags=["LocationGroups"], response_model=CreateLocationGroupResponse)
async def create_location_group(location_group: CreateLocationGroupRequest):
    """Create a location group"""
    return LocationGroupsQueries().insert_location_group(location_group.name)


@app.get("/location_groups/{location_group_id}", tags=["LocationGroups"], response_model=GetLocationGroupResponse)
async def get_location_group(location_group_id: int):
    """Get a location group"""
    query_result = LocationGroupsQueries().select_location_group(location_group_id)
    return GetLocationGroupResponse(**query_result)
