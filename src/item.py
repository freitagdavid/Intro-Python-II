class Item:
    def __init__(self, name, description, itemType, value):
        self.name = name
        self.itemType = itemType
        self.value = value
        self.description = description

    def __repr__(self):
        return f'Item: {self.name}'
