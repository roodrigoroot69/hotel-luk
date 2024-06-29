from dataclasses import dataclass

from users.domain.interfaces.guests import Guest


@dataclass
class SinglePerson(Guest):
    name: str = ''
    number_guest:int = 1

    def get_guests(self):
        print(''.join(self.name))

    def __str__(self) -> str:
        return ''.join(self.name)

@dataclass
class GroupPeople(Guest):
    name: str = ''
    number_guest:int = 3

    def get_guests(self):
        for guest in self.name.split(","):
            print(guest)

    def __str__(self) -> str:
        return self.name


@dataclass
class CouplePeople(Guest):
    name: str = ''
    number_guest:int = 2

    def get_guests(self):
        for guest in self.name.split(","):
            print(guest)

    def __str__(self) -> str:
        return self.name