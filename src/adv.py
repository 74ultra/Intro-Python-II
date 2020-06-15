import sys
from room import Room
from player import Player
from item import rake, knife, hammer, book, flashlight, rat

# Rooms

outside = Room("Outside Cave Entrance",
               "North of you, the cave mouth beckons", [rake])
foyer = Room(
    "Foyer", "Dim light filters in from the south. Dusty passages run north and east.", [knife, hammer])
overlook = Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.")
narrow = Room("Narrow Passage",
              "The narrow passage bends here from west to north. The smell of gold permeates the air.", [rat])
treasure = Room("Treasure Chamber",
                "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", [book, flashlight])

# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#
command_list = '*********\nCommands:\nn --> move north\ns --> move south\ne --> move east\nw --> move west\nl --> look around the room to search for items\ni --> show list of items carried\nget [item name] --> add item to your inventory\ntake [item name] --> add item to your inventory\ndrop [item name] --> remove item from your inventory\nh --> display the command list again\nq --> quit the game\n*********'

player_name = input(
    "Welcome to whatever this game is. Please enter your name: ")
player = Player(player_name, current_room=outside)
print(f'Welcome, {player.name}. Let\'s begin the journey.\n')
print(command_list)

while True:
    try:
        print(player.current_room.desc())
        action = input('Please enter a command: ')
        cmd_list = action.split(' ')
        if action.lower() == 'q':
            print(f'Thank you for playing, {player_name}')
            break
        if len(cmd_list) == 1:
            if action.lower() == 'n':
                print(action)
                player.current_room = player.current_room.n_to
            elif action.lower() == 's':
                print(action)
                player.current_room = player.current_room.s_to
                # continue
            elif action.lower() == 'e':
                print(action)
                player.current_room = player.current_room.e_to

            elif action.lower() == 'w':
                print(action)
                player.current_room = player.current_room.w_to

            elif action.lower() == 'h':
                print(command_list)
            elif action.lower() == 'l':
                print(player.current_room.room_inv())
            elif action.lower() == 'i':
                print(player.player_inv())
            else:
                print('That is not a valid command\n')
                continue
        elif len(cmd_list) == 2:
            if cmd_list[0].lower() == 'get' or cmd_list[0].lower() == 'take':
                if player.current_room.inventory:
                    for item in player.current_room.inventory:
                        if cmd_list[1].lower() == item.name:
                            player.current_room.inventory.remove(item)
                            player.inventory.append(item)

                else:
                    print("There is nothing here you can take with you")
            elif cmd_list[0].lower() == 'drop':
                if player.inventory:
                    for item in player.inventory:
                        if cmd_list[1].lower() == item.name:
                            player.inventory.remove(item)
                            player.current_room.inventory.append(item)

                else:
                    print("You don't have anything to drop.")
    except AttributeError as err:
        print("\nThere is no room in that direction")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Make a new player object that is currently in the 'outside' room.
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
