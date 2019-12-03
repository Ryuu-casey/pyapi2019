#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showinstructions():
    # print a main menu and the commands
    print('''
RPG Game
=================================================
Get to the Garden with a key and a potion to win!
Avoid the monsters! 
=================================================
Commands:
    go [north, east, south, west]
    get [item]
''')


def showstatus():
    # Print the player's current status
    print('----------------------------------')
    print('You are in the ' + currentRoom)
    # Print the current inventory
    print('Inventory : ' + str(inventory))
    # Print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("-----------------------------------")


# An inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'north': 'Living Room',
        'east': 'Dining Room',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
    },
    'Dining Room': {
        'west': 'Hall',
        'north': 'Foyer',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Living Room': {
        'south': 'Hall',
        'east': 'Foyer'
    },
    'Foyer': {
        'south': 'Dining Room',
        'west': 'Living Room',
        'item': 'monster'
    }
}

# Start the player in the Hall
currentRoom = 'Hall'

showinstructions()

# Loop forever
while True:

    showstatus()

    # Get the player's next 'move'
    # .split() breaks it up into an list array
    # Eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # Split allows an items to have a space on them
    # Get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # If they type 'go' first
    if move[0] == 'go':
        # Check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # Set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # There is no door (link) to the new roomget
        else:
            print('You can\'t go that way!')

    # If they type 'get' first
    if move[0] == 'get':
        # If the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # Add the item to their inventory
            inventory += [move[1]]
            # Display a helpful message
            print(move[1] + ' got!')
            # Delete the item from the room
            del rooms[currentRoom]['item']
        # Otherwise, if the item isn't there to get
        else:
            # Tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
