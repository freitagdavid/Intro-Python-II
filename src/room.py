# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
        self.available_directions = None

    def addItem(self, item):
        """Add and item to the room.

        Arguments:
            item {[object]} -- [item instance]
        """
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def check_item(self, item):
        return item in self.items

    def get_item_names(self):
        working = []
        for i in self.items:
            working.append(i.name)
        return working

    def get_available_directions(self):
        working_list = []
        if self.n_to is not None:
            working_list.append('north')
        if self.e_to is not None:
            working_list.append('east')
        if self.s_to is not None:
            working_list.append('south')
        if self.e_to is not None:
            working_list.append('east')
        self.available_directions = working_list
