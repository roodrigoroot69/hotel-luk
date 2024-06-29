from abc import ABC
from dataclasses import dataclass
from typing import List

from users.domain.interfaces.guests import Guest


@dataclass
class Room(ABC):
    guest: Guest
    room_number: int
    guest_allowed: int


@dataclass
class Row(ABC):
    rooms: List[Room]


@dataclass
class Level(ABC):
    rows: Row


@dataclass
class Hotel(ABC):
    levels: Level

