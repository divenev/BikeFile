from enum import Enum


class ChoicesEnum(Enum):

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]
