from dataclasses import dataclass
from typing import Dict, List

from hotel.domain.interfaces.hotel import Hotel, Level, Room, Row


@dataclass
class MultipleRows(Row):
    rooms: Dict[int, List[Room]]


@dataclass
class MultipleLevels(Level):
    rows: Row


@dataclass
class TiptonHotel(Hotel):
    levels: Level


def build_rooms(
    row: Row,
    rooms: Dict[int, List[Room]]
) -> Row:
    row.rooms = rooms


def build_hotel(
    hotel: Hotel,
    levels: Level,
    row: Row
) -> Hotel:
    hotel.levels = levels

