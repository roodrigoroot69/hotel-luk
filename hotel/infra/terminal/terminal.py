from hotel.app.common.utils_rooms import get_type_guest
from hotel.app.lodge_processor import LodgeRoomProcessor
from hotel.domain.interfaces.hotel import Hotel
from hotel.domain.services.lodge import LodgeRoomService
from hotel.infra.repositories.lodge_repository import LodgeRepository


COUNT_GUEST_MESSAGE = """
How many people are there?
"""
SELECT_ROOM_STAGE = """
What kind of room do you want?
1.- Individual Room
2.- Double Room
3.- Large Room
"""
NAME_GUEST_MESSAGE = """
Please enter the name of Guest separeted by commas:
"""


def lodge_procces(hotel: Hotel):
    count_guest = int(input(COUNT_GUEST_MESSAGE))
    guest = get_type_guest(count_guest)

    names_guest = input(NAME_GUEST_MESSAGE)
    guest = guest(name=names_guest)

    selected_room = int(input(SELECT_ROOM_STAGE))

    repository = LodgeRepository(
        row=hotel.levels.rows
    )

    lodge_service = LodgeRoomService(
        guest=guest,
        level_id=selected_room,
        repository=repository,
    )
    LodgeRoomProcessor(
        lodge_service=lodge_service,
    ).execute()
