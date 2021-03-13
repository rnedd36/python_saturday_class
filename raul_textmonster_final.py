# import operating system
from os import system, name
# screen clear function


def clear():
    # for windows operating system
    if name == 'nt':
        _ = system('cls')
    # for mac and linux operating system
    else:
        _ = system('clear')


clear()

floor_1 = ['nothing', 'stairs up', 'sword', 'monster', 'magic stones']
floor_2 = ['stairs up', 'sword', 'sword', 'stairs down', 'monster']
floor_3 = ['stairs down', 'sword', 'magic stones', 'monster', 'boss']

player_room = 0
player_floor = floor_1
current_floor = 'floor 1'
current_turn = 'straight'

player_won = False
player_alive = True
flag = ""
bookbag = []

while player_alive and player_won == False:
    prev_turn = "unknown"
    if (current_turn in ('grab', 'fight')):
        current_turn = 'remain'

        print("You {0} inside the room {3} on {2}. Inside the room is {1}.".format(current_turn,
                                                                                   player_floor[player_room], current_floor, player_room))
    elif (current_turn == 'straight'):
        print("You go {0} inside the room {3} on {2}. Inside the room is {1}.".format(current_turn,
                                                                                      player_floor[player_room], current_floor, player_room))
    else:
        #print("You are on {}".format(current_floor))
        print("You go {0} into room {3} on {2}. Inside the room is a {1}.".format(current_turn,
                                                                                  player_floor[player_room], current_floor, player_room))

    if player_floor[player_room] in ('monster', 'boss'):
        print("You {0} inside the room {3} on {2}. Inside the room is {1}.".format(current_turn,
                                                                                   player_floor[player_room], current_floor, player_room))

        while current_turn not in ('back', 'fight', 'quit'):
            print("You can't go past you must back out or fight")
            prev_turn = current_turn
            current_turn = input(
                'What would you like to do? (back, fight or quit) ').lower()

    else:
        current_turn = input(
            'What would you like to do? (right, left, up, down, grab, fight or quit) ').lower()
    clear()

    if current_turn == 'left':
        if player_room == 0:
            print("Can't move left. There is a wall there. ")

        else:
            player_room = player_room - 1
    elif current_turn == 'right':
        if player_room == len(player_floor) - 1:
            print("Can't move right. There is a wall there. ")
        else:
            player_room = player_room + 1
    elif current_turn == 'down':
        if (player_floor[player_room] != 'stairs down'):
            print("You can't go down, there are no stairs going down. ")
        else:
            if player_floor == floor_2:
                player_floor = floor_1
                current_floor = 'floor 1'
            elif player_floor == floor_3:
                player_floor = floor_2
                current_floor = 'floor 2'
    elif current_turn == 'up':
        if (player_floor[player_room] != 'stairs up'):
            print("You can't go up, there are no stairs going up. ")
        else:
            if player_floor == floor_1:
                player_floor = floor_2
                current_floor = 'floor 2'
            elif player_floor == floor_2:
                player_floor = floor_3
                current_floor = 'floor 3'
    elif current_turn == 'grab':
        if len(bookbag) >= 3:
            print("Sorry your bookbag is full, you can't carry anymore items")
        else:
            if (player_floor[player_room] == 'sword') or (player_floor[player_room] == 'magic stones'):
                bookbag.append(player_floor[player_room])
                print("You performed a {0} and picked up a...{1}.".format(current_turn,
                                                                          player_floor[player_room]))
                print("You have in your bookbag {}.".format(bookbag))
                player_floor[player_room] = "nothing"
            else:
                print("There is nothing to pick up")

    elif current_turn == "fight":
        if (player_floor[player_room] == "monster"):
            if 'sword' in bookbag:

                print("You killed the monster")
                player_floor[player_room] = "nothing"
                bookbag.remove("sword")
                print("You have in your bookbag {}.".format(bookbag))

            else:
                print("The monster killed you")
                player_alive = False
        elif (player_floor[player_room] == "boss"):
            if ('sword' in bookbag) and ('magic stones' in bookbag):
                print("You killed the boss")

                bookbag.remove("sword")
                bookbag.remove("magic stones")
                player_won = True
            else:
                print("The boss killed you")

                player_alive = False

        else:
            print("Sorry, there is no monster in the room.")

    elif current_turn == "back":
        # print(prev_turn)
        if prev_turn == "down":
            if player_floor == floor_1:
                player_floor = floor_2
                current_floor = 'floor 2'
            elif player_floor == floor_2:
                player_floor = floor_3
                current_floor = 'floor 3'
        elif prev_turn == "up":
            if player_floor == floor_2:
                player_floor = floor_1
                current_floor = 'floor 1'
            elif player_floor == floor_3:
                player_floor = floor_2
                current_floor = 'floor 2'
        elif prev_turn == "right":
            player_room -= 1
        elif prev_turn == "left":
            player_room += 1
        else:
            print("Sorry that is not a valid move.")
    elif current_turn == "quit" or current_turn == "q":
        player_alive = False
    else:
        print("Sorry that is not a valid move.")


if (player_won):
    print("You did it. You won!!")

#print("The player is currently in room... {}".format(player_floor[player_room]))
