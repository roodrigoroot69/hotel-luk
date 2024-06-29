### Structure of Project
For this project i'm using a implementation of Hexagonal Architecture

We have a two apps called Hotel and Users, and they have 3 modules:
- Domain
- App
- Infra

Domain: Here we have all the interfaces Hotel, Rooms, Rows, Levels, Guest
App: Here we have the adapters for each interface and its respective bussinec logic.
Infra: Here we have the interacion with the user, in this case is using terminal.


### How to execute this project?
`python main.py`

### Examples

**Individual Person**

![Individual Person](https://github.com/roodrigoroot69/hotel-luk/blob/main/docs/images/couple.png "Invidivual Person")

**Couple**

![Individual Person](https://github.com/roodrigoroot69/hotel-luk/blob/main/docs/images/couple.png "Invidivual Person")

**Group**

![Individual Person](https://github.com/roodrigoroot69/hotel-luk/blob/main/docs/images/large%20rooms.png "Invidivual Person")

**Couple not allowed to Individual Room**

![Individual Person](https://github.com/roodrigoroot69/hotel-luk/blob/main/docs/images/not%20allowed%20for%20couple.png "Invidivual Person")

**Group not allowed to Individual Room**

![Individual Person](https://github.com/roodrigoroot69/hotel-luk/blob/main/docs/images/no%20allowed%20room.png "Invidivual Person")
