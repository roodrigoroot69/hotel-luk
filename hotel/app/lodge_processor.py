from dataclasses import dataclass

from hotel.domain.exceptions.lodge_exceptions import SurplusGuestsException
from hotel.domain.services.lodge import LodgeRoomService



@dataclass
class LodgeRoomProcessor:
    lodge_service: LodgeRoomService

    def execute(self):
        try:
            self.lodge_service.execute()
        except SurplusGuestsException as sge:
            print(sge)