from room import Room
from player import Player
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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

player = Player(room=room['outside'])

# Make a new player object that is currently in the 'outside' room.
directions = ['north', 'east', 'south', 'west']


def parse_command(command):
    split_command = command.lower().split()

    if len(split_command) > 2:
        print('You can enter at most two words.')
    elif len(split_command) == 1:
        if split_command[0] in directions:
            player.move(split_command[0])
        else:
            print('Invalid command')


def list_items():
    """List all items available in room."""
    if not player.room.items:
        stringified_list = '\n'.join(player.room.items)
        print(f"In the room you see the following items: \n{stringified_list}")


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
