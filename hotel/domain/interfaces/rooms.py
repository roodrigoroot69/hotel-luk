from abc import ABC, abstractmethod
from dataclasses import dataclass

from users.domain.interfaces.guests import Guest


@dataclass
class Room(ABC):
    number_room: int
    guest: Guest
    guest_allowed:int
    is_busy: bool = False
