# Hayden Gentry
# Show instructions function
def show_instructions():
    print("*************************************************************")
    print("***********  Basilisk Text Based Adventure Game  ************")
    print("[  Collect all six items, and make it to the Treasure Room  *")
    print("[   One item short... you will be eaten by the Basilisk!!   *")
    print("[                                                           *")
    print("***********************  How to play  ***********************")
    print("*               Move to Room: move 'Direction'              *")
    print("*            Add to Inventory: grab 'Item name'             *")
    print("*                      Exit Game: exit                      *")
    print("*                                                           *")
    print("**********************  Best of luck!  **********************")
    print("*          How quickly can you slay the Basilisk??          *")
    print("*************************************************************")


# Main function
def main():
    # Dictionary of rooms
    # Each room contains a dictionary of moves to other rooms
    # and all but two rooms (Ball Room and Treasure room)
    # contain a different item to be obtained to win the game
    rooms = {"Ball Room": {"North": "Library", "East": "Banquet Hall", "South": "Courtyard", "West": "Kitchen"},
             "Banquet Hall": {"North": "Treasure Room", "South": "Courtyard", "West": "Ball Room", "Item": "Slippers"},
             "Courtyard": {"North": "Ball Room", "East": "Banquet Hall", "West": "Kitchen", "Item": "Mask"},
             "Kitchen": {"North": "Library", "East": "Ball Room", "South": "Courtyard", "Item": "Knife"},
             "Library": {"North": "Armory", "South": "Ball Room", "West": "Kitchen", "Item": "Book"},
             "Armory": {"North": "Kings Quarters", "East": "Treasure Room", "South": "Library", "Item": "Crossbow"},
             "Kings Quarters": {"East": "Treasure Room", "South": "Armory", "Item": "Cape"},
             "Treasure Room": {"Basilisk": "Item"}}
    # Player begins the game in the Ball Room
    room = "Ball Room"
    inventory = []

    # Show current room function
    def show_current_room():
        print(" ")
        print("You are in the:", room)
        # Do not show the item if in the Ball Room or Treasure Room
        if (room == "Ball Room") or (room == "Treasure Room"):
            pass
        # Show the item if not in the inventory
        else:
            if rooms[room]["Item"] in inventory:
                pass
            else:
                print("You see a", rooms[room]["Item"])

    # Show option function
    def show_command_options():
        for i, j in rooms[room].items():
            # Show to grab the item if not in the inventory
            if i == "Item":
                if j in inventory:
                    pass
                else:
                    print("---> grab", j)
            # Show to move to a direction to go into a room
            else:
                print("---> move", i, "to go to the", j)

    # Show inventory function
    def show_current_inventory():
        print("Inventory:", str(inventory).replace("[", "").replace("]", "").replace("'", ""))

    # Main logic loop
    # Will continue playing the game until exit command
    while 1:
        show_current_room()
        show_command_options()
        show_current_inventory()
        # Get user input
        d = input("Enter a command: ")
        direction = [str(a) for a in d.split(" ")]
        options = rooms[room]
        # Execute command options
        # Move function
        if direction[0] == "move":
            # If direction is a valid direction
            if direction[1] in options:
                room = options[direction[1]]
                # Treasure room function
                if room == "Treasure Room":
                    # If gathered all the items, winner
                    if len(inventory) == 6:
                        print(" ")
                        print("!!!!!!!!!!!!!!!  YOU HAVE SLAIN THE BASILISK  !!!!!!!!!!!!!!!")
                        print("!!!!!!!!!!!!!!!!!!!!  YOU ARE A WINNER  !!!!!!!!!!!!!!!!!!!!!")
                        # Restart game
                        show_instructions()
                        room = "Ball Room"
                        inventory = []
                    # If not, loser
                    else:
                        print(" ")
                        print("!!!!!!!!!!!  YOU HAVE BEEN SLAIN BY THE BASILISK  !!!!!!!!!!!")
                        print("!!!!!!!!!!!!!!!!!!!!!  YOU ARE A LOSER  !!!!!!!!!!!!!!!!!!!!!")
                        # Restart game
                        show_instructions()
                        room = "Ball Room"
                        inventory = []
            # If direction is not a valid direction
            else:
                print(direction[1], "is not a direction to move in the room")
        # Grab function
        elif direction[0] == "grab":
            # If item is in the inventory
            if direction[1] in inventory:
                print(direction[1], "already in inventory")
            # If item is not in the inventory
            else:
                # If item is the item in the room
                if direction[1] == rooms[room]["Item"]:
                    inventory.append(direction[1])
                # If item is not the item in the room
                else:
                    print(direction[1], "is not the item in the room")
        # Exit function
        elif direction[0] == "exit":
            print("You are now exiting")
            break
        # Any other input is invalid
        else:
            print("Invalid Command")


# Run program
show_instructions()
main()
