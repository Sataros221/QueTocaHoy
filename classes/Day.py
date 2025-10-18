from enum import Enum

import helpers


class Day(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        schedule = {}

    def setSchedule(self):
        self._schedule = helpers.parse()

    def __getattribute__(self, name):
        return super().__getattribute__(name)
