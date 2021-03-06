import time
from enum import Enum

from dataclasses import dataclass
from typing import Dict

from figgy.constants.data import *


class ConfigState(Enum):
    DELETED = 0
    ACTIVE = 1


@dataclass(eq=True, frozen=True)
class ConfigItem:
    name: str
    state: str
    last_updated: int

    @staticmethod
    def from_dict(obj: Dict) -> "ConfigItem":
        name = obj.get(CACHE_PARAMETER_KEY_NAME, None)
        last_updated = obj.get(CACHE_LAST_UPDATED_KEY_NAME, time.time())
        state = obj.get(CACHE_STATE_ATTR_NAME, None)

        return ConfigItem(name=name, last_updated=last_updated, state=ConfigState[state])

