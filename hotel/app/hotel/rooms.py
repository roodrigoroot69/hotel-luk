from dataclasses import dataclass
from typing import Optional

from hotel.domain.interfaces.rooms import Room
from users.domain.interfaces.guests import Guest


@dataclass
class IndividualRoom(Room):
    number_room: int
    is_busy: bool = False
    guest: Optional[Guest] = None
    guest_allowed:int = 1

    def __str__(self) -> str:
        return f'Number room: {self.number_room}\nIs Busy: {self.is_busy}\nType: Individual Room\nGuest: {self.guest}'


@dataclass
class DoubleRoom(Room):
    number_room: int
    is_busy: bool = False
    guest: Optional[Guest] = None
    guest_allowed:int = 2

    def __str__(self) -> str:
        return f'Number room: {self.number_room}\nIs Busy: {self.is_busy}\nType: Double Room\nGuests: {self.guest}'


@dataclass
class LargeRoom(Room):
    number_room: int
    is_busy: bool = False
    guest: Optional[Guest] = None
    guest_allowed: int = 3

    def __str__(self) -> str:
        return f'Number room: {self.number_room}\nIs Busy: {self.is_busy}\nType: Large Room\nGuests: {self.guest}'
