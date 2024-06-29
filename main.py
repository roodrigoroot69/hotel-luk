from hotel.app.common.utils_rooms import generate_rooms, get_all_rooms
from hotel.app.hotel.hotel import MultipleLevels, MultipleRows, TiptonHotel
from hotel.infra.terminal.terminal import lodge_procces

individual_rooms, double_rooms, large_rooms = generate_rooms()
all_rooms = get_all_rooms(individual_rooms, double_rooms, large_rooms)


rows = MultipleRows(rooms=all_rooms)

levels = MultipleLevels(rows=rows)
tipton_hotel = TiptonHotel(levels=levels)

if __name__ == '__main__':
    lodge_procces(tipton_hotel)