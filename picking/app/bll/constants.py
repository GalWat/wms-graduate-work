from enum import Enum


class TaskStatus(Enum):
    Created = 1
    InProgress = 2
    Finished = 3
    Cancelled = 4
