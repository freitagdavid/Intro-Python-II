from copy import copy


class Item:
    def __init__(self, name, description, itemType, value):
        self.name = name
        self.itemType = itemType
        self.value = value
        self.description = description
        self.normalized_name = ''
        self.normalize_name()

    def __repr__(self):
        return f'Item: {self.name}'

    def normalize_name(self):
        working = copy(self.name)
        working = working.lower()
        working = working.replace(" ", "")
        self.normalized_name = copy(working)

    def on_take(self, player):
        return
