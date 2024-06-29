from hotel.app.adapters.rooms import DoubleRoom, IndividualRoom, LargeRoom



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