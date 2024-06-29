from abc import ABC, abstractmethod

from dataclasses import dataclass

from hotel.domain.interfaces.hotel import Row
from hotel.domain.interfaces.rooms import Room
from users.domain.interfaces.guests import Guest


@dataclass
class ILodgeRepository(ABC):
    row: Row

    def get_room(
        self,
        level_id: int,
        number_room: int,
    ) -> Room:
        raise NotImplementedError

    def lodge(
        self,
        room: Room,
        guest: Guest
    ):
        raise NotImplementedError

    def get_unoccupied_room(
        self,
        level_id: int
    ) -> Room:
        raise NotImplementedError

