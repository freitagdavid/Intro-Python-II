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

    def add_item(self, item):
        self.inventory.append(item)

    def set_room(self, room):
        self.room = room

    def pickup_item(self, item):
        self.add_item(item)
        self.room.remove_item(item)
        item.on_take(self)


# TODO Test

    def remove_item(self, item):
        self.inventory.remove(item)

# TODO Test and finish it off
# It should remove the items from the players inventory then add it to the room
# the player is currently in

    def drop_item(self, item):
        if item in self.inventory:
            self.remove_item(item)
            # self.room.add_

    def get_item_names(self):
        working = []
        for i in self.inventory:
            working.append(i.name)
        return working

    def move(self, direction):
        self.room.get_available_directions()
        if direction in self.room.available_directions:
            self.set_room(self.directions[direction])
        else:
            print("That's not possible try again.")
