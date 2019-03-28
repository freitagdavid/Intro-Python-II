# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, name="Player", race="human", gender="male"):
        self.name = name
        self.room = room
        self.race = race
        self.gender = gender
        self.inventory = []
        self.map_directions()

    def map_directions(self):
        self.directions = {
            'north': self.room.n_to,
            'east': self.room.e_to,
            'south': self.room.s_to,
            'west': self.room.w_to
        }

    def addItem(self, item):
        self.inventory.append(item)

    def setRoom(self, room):
        self.room = room

    def move(self, direction):
        self.room.get_available_directions()
        if direction in self.room.available_directions:
            self.setRoom(self.directions[direction])
        else:
            print("That's not possible try again.")
