from dataclasses import dataclass

from hotel.domain.interfaces.hotel import Row
from hotel.domain.interfaces.rooms import Room
from hotel.domain.repositories.lodge import ILodgeRepository
from users.domain.interfaces.guests import Guest


@dataclass
class LodgeRepository(ILodgeRepository):
    row: Row

    def get_room(
        self,
        level_id: int,
        number_room: int,
    ) -> Room:
        rooms_level = self.row.rooms[level_id]
        found_room = None
        for room in rooms_level:
            if room.number_room == number_room:
                found_room = room
                break
        return found_room

    def lodge(self, room: Room, guest: Guest):
        room.is_busy = True
        room.guest = guest

    def get_unoccupied_room(
        self,
        level_id: int
    ) -> Room:
        room_to_occupy = None
        rooms: Room = self.row.rooms[level_id]
        for room in rooms:
            if not room.is_busy:
                room_to_occupy = room
                break
        return room_to_occupy

