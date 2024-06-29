from typing import Dict
from hotel.app.hotel.rooms import DoubleRoom, IndividualRoom, LargeRoom
from users.app.guests.guests import CouplePeople, GroupPeople, SinglePerson


def get_type_guest(count_guest:int):
    return {
        1: SinglePerson,
        2: CouplePeople,
        3: GroupPeople,
    }.get(count_guest, GroupPeople)

def get_all_rooms(
    individual_rooms,
    double_rooms,
    large_rooms
) -> Dict:
    return {
    1: individual_rooms,
    2: double_rooms,
    3: large_rooms
}

def generate_rooms():
    individual_rooms = []
    double_rooms = []
    large_rooms = []

    for room in range(1, 16):
        individual_rooms.append(IndividualRoom(
            number_room=room,
        ))
    for room in range(17, 27):
        double_rooms.append(DoubleRoom(
            number_room=room,
        ))
    for room in range(28, 38):
        large_rooms.append(LargeRoom(
            number_room=room,
        ))
    return individual_rooms, double_rooms, large_rooms

