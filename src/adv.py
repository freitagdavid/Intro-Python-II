from room import Room
from player import Player
from item import Item
import types

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'sword': Item("Sword", "A nice shiny sword", "weapon", "10")
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms
room['foyer'].addItem(item['sword'])

#
# Main
#

player = Player(room=room['outside'])

# Make a new player object that is currently in the 'outside' room.
directions = ['north', 'east', 'south', 'west']
movement_verbs = ['go', 'walk']
interaction_verbs = ['open', 'close']
item_interaction_verbs = ['pickup', 'grab', 'take', 'get']
misc_commands = ['i', 'inventory']


def parse_command(command):
    split_command = command.lower().split()

    if len(split_command) > 2:
        print('You can enter at most two words.')
    elif len(split_command) == 1:
        if split_command[0] in directions:
            player.move(split_command[0])
        elif split_command[0] == 'quit':
            global running
            running = False
        elif split_command[0] in misc_commands:
            if split_command[0] == 'i' or split_command[0] == 'inventory':
                inventory = player.get_item_names()
                stringified_list = '\n'.join(inventory)
                print(f"Your inventory contains:\n{stringified_list}")
        else:
            print('Invalid command')
    else:
        verb = split_command[0]
        noun = split_command[1]

        if verb in movement_verbs:
            player.move(noun)
        elif verb in item_interaction_verbs:
            if player.room.check_item(item[noun]):
                player.pickup_item(item[noun])
                print(f'You {verb} {noun}')


def list_items():
    """List all items available in room."""
    if player.room.items:
        items = player.room.get_item_names()
        stringified_list = '\n'.join(items)
        print(
            f"In the room you see the following items: \n{stringified_list}\n")


def process_input():
    """Intake input and pass it to the parser."""
    player_input = input('What do you wish to do?: ')
    parse_command(player_input)


def update():
    """
    General cleaning up.

    Happens after handling commands and before updating screen.
    """
    player.map_directions()


def draw():
    """Handle all data output to screen."""
    print(player.room.name)
    print(player.room.description)
    list_items()


running = True


def main_loop():
    while running:
        process_input()
        update()
        draw()


def start():
    draw()
    main_loop()


start()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
