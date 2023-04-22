from enum import Enum


class TaskStatus(Enum):
    Created = 1
    RouteAwaiting = 2
    InProgress = 3
    Finished = 4
    Cancelled = 5
