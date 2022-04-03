#########################
#IMPORTS
#########################
#import all functions from adventurelib
from adventurelib import*
import time

#rooms
Room.item = Bag()

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
item.description = ""
sword = Item("blade","SwordRoom")
note = Item("A scribbled note","note","paper","code")
torch = Item("A light","A torch","torch","light")

#########################
#DEFINE BAGS
#########################
sword.description = "This sword shall guide you through the quest for treasure"
note.description = "You look at the note. The numbers 3459 are scribbled"
torch.description = "the torch is "

#########################
#ADD ITEMS TO BAG
#########################
DeadEnd.add(note)
SwordRoom.add(sword)

#########################
#DEFINE ANY VARIABLES
#########################
current_room  = Jungle
inventory = Bag()
door_opened = False
used_keycard = False

#########################
#BINDS
#########################
@when("jump")
def jump():
	print("You jump")

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("You haul yourself into the airlock")
		current_room = airlock
	else:
		print("There is no airlock here")
	print(current_room)

@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#checks if the current room list of exits
		#the direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You can't go that way")

@when("look")
def look():
	print(current_room)
	print("There are exits to the ",current_room.exits())
	if len(current_rooms.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)


@when("get ITEM")
@when("take ITEM")
def get_item(item):
	#checked if item is in room
	#take it out of room
	#put into inventory
	#otherwise tell user there is no item
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You picked up the {item}")
	else:
		print(f"You don't see a {item}")

@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)

@when("search body")
@when("look at body")
@when("search man")
def search_body():
	global body_searched
	if current_room == bridge and body_searched == False:
		print("you search the body and a red keycard falls to the floor")
		current_room.items.add(keycard)
		body_searched = True
	elif current_room == bridge and body_searched == True:
		print("You have already searched the body")
	else:
		print("There is no body here to search")

@when("use ITEM")
def use(item):
	if item == keycard and current_room == bridge:
		print("You use the keycard and the escape pod slides open")
		print("The escape pod stands open to the south")
		bridge.south = escape
	else:
		print("You can't use that here")



@when("type code")
def escape_pod_win():
	if note in inventory:
		if current_room == escape:
			print("You enter the code and escape. You win")
		else:
			print("There is no where to enter the code")
	else:
		print("You don't have the code. You can't just guess it.")

#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
	#start the main loop

main()