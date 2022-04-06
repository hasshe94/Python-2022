#########################
#IMPORTS
#########################
from adventurelib import*
import time

#########################
#DEFINE ROOMS
#########################
Jungle = Room("You are in the jungle, You have finally found the elusive temple and its entrance is beckoning you")
MainTempleRoom = Room("You are in the main temple room, It is nearly completely dark except for a large mysterious statue of what seems to be an ancient warrior, lit up by a small torch laying on its side")
CornerRoom1 = Room("You are in a small corner room,there may be other rooms near by")
CornerRoom2 = Room("You are in a small corner room,there may be other rooms near by")
SwordRoom = Room("You are in an all but barren dark room, except for a gleaming sword providing the tiniest bit of light")
BurialTomb = Room("You are in the burial tomb, but it was waiting for you. It collapses suffocating you untill death")
TrapRoom = Room("You enter a room that is crowded in bushes, you hear a weird hissing sound. Perhaps there are traps?")
BushRoom = Room("What was once a room is now overtaken by nature. To see more you may have to get to cutting")
DeadEnd = Room("The room is a deadend, the only way back is the way you came. But there is a note that may help along the journey.")
HallwayRoom = Room("You enter an empty room. It has a statue of an angry man, perhaps telling you to go back")
StatueRoom = Room("You enter a barren room, it has a shining gold statue pointing to the east")
DeathRoom = Room("You enter an empty room, mechanical doors close on you, you are left to die a slow painful death")
LockRoom = Room("You enter a tall room with almost with an almost deafining scilence, there is a locked door near the end of the room, you need a code to break through")
TreasureRoom = Room("You see the treasure lying in the center of the room, there is only one problem. Someone is guarding it. You will have to fight them")
#########################
#DEFINE CONNECTIONS
#########################
Jungle.north = MainTempleRoom
MainTempleRoom.east = CornerRoom1
MainTempleRoom.west = CornerRoom2
CornerRoom1.north = BurialTomb
CornerRoom2.north = SwordRoom
SwordRoom.west = TrapRoom
SwordRoom.north = DeathRoom
TrapRoom.west = BurialTomb
TrapRoom.north = HallwayRoom
StatueRoom.east = DeathRoom
HallwayRoom.east = StatueRoom
HallwayRoom.west = BushRoom
HallwayRoom.north = LockRoom
LockRoom.east = TreasureRoom
BushRoom.north = DeadEnd


#########################
#DEFINE ITEMS
#########################

#########################
#DEFINE BAGS
#########################

#########################
#ADD ITEMS TO BAG
#########################

#########################
#DEFINE ANY VARIABLES
#########################
game_start == True
current_room = Jungle
#########################
#BINDS
#########################
if game_start == True:
	print("You are in the jungle and have finally found the elusive temple. You are closer then ever to finding the treasure.")
    game_start = False

#########################
#MAIN FUNCTION
#########################
def main():
	start()
	#start the main loop

main()







#test code this document isnt meant to be used for final code

@when("look")
def look():
	print(current_room)
	exits_amount = int(len(current_room.exits()))
    if exits_amount == 1:
        #grammatically correct way of saying there is one exit
        print(f"There is a visible exit to the {', '.join(current_room.exits())}")
    elif exits_amount > 1:
        #grammatically correct way of saying there is more than one exit
        print(f"There are visible exits to the {', '.join(current_room.exits()[:-1]) + ' and ' + current_room.exits()[-1]}")
    else:
        print("There are no visible exits")
	if len(current_rooms.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)
