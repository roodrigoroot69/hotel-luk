from dataclasses import dataclass

from hotel.domain.exceptions.lodge_exceptions import SurplusGuestsException
from hotel.domain.repositories.lodge import ILodgeRepository
from users.domain.interfaces.guests import Guest


@dataclass
class LodgeRoomService:
    guest: Guest
    level_id: int
    repository: ILodgeRepository

    def execute(self):
        room = self.repository.get_unoccupied_room(self.level_id)

        if not self.guest.number_guest <= room.guest_allowed:
            raise SurplusGuestsException('The room is very small for the number of guests')
        self.repository.lodge(
            room=room,
            guest=self.guest
        )

        occuped_room = self.repository.get_room(
            level_id=self.level_id,
            number_room=room.number_room,
        )
        print(occuped_room)
