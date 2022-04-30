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
Jungle = Room("You are in the jungle, You have finally found the elusive temple and its entrance is beckoning you,clutching your torch your eager to make it in")

MainTempleRoom = Room("You are in the main temple room, It is nearly empty except for a large mysterious statue of what seems to be an ancient warrior.")

CornerRoom1 = Room("You are in a small corner room,there may be other rooms near by")

CornerRoom2 = Room("You are in a small corner room,there may be other rooms near by")

SwordRoom = Room("You are in an all but barren dark room, except for a gleaming sword providing the tiniest bit of light")

BurialTomb = Room("You are in the burial tomb, but it was waiting for you. It collapses suffocating you untill death")

TrapRoom = Room("You enter a room that is crowded in bushes, you hear a weird hissing sound.Darts start flying towards you.DO SOMETHING!")

BushRoom = Room("What was once a room is now overtaken by nature. To see more you may have to get to cutting trees.")

DeadEnd = Room("The room is a deadend, the only way back is the way you came. But there is a skeleton that searching may prove useful, unless you already have.")

HallwayRoom = Room("You enter an empty room. It has a statue of an angry man, perhaps telling you to go back")

StatueRoom = Room("You enter a barren room, it has a shining gold statue pointing to the east")

DeathRoom = Room("You enter an empty room, mechanical doors close on you, trapping you, you are left to die a slow painful death")

LockRoom = Room("You enter a tall room with almost with an almost deafining scilence, there is a locked door near the end of the room, you need a code to break through")

TreasureRoom = Room("You see the treasure lying in the center of the room, there is only one problem. Someone is guarding it. You will have to fight them")

#########################
#DEFINE CONNECTIONS
#########################
Jungle.north = MainTempleRoom
MainTempleRoom.east = CornerRoom2
MainTempleRoom.west = CornerRoom1
CornerRoom1.north = BurialTomb
CornerRoom2.north = SwordRoom
SwordRoom.west = TrapRoom
SwordRoom.north = DeathRoom
StatueRoom.east = DeathRoom
HallwayRoom.east = StatueRoom
HallwayRoom.west = BushRoom
HallwayRoom.north = LockRoom

#########################
#DEFINE ITEMS
#########################
Item.description = ""
sword = Item("sword","blade")
note = Item("note","A scribbled note","paper","code")

#########################
#DEFINE BAGS
#########################
sword.description = "This sword is sturdy and sharp and shall guide you through the quest for treasure"
note.description = "You look at the note. The numbers 3459 are scribbled"


#########################
#ADD ITEMS TO BAG
#########################
SwordRoom.item.add(sword)
#########################
#DEFINE ANY VARIABLES
#########################
current_room  = Jungle

inventory = Bag()

sword_block = False

cut_bush = False

bush_cut = False

skeleton_searched = False

lock_opened = False

trap_complete = False

bush_complete = False

game_start = True

boss = False

game_death = False

#########################
#BINDS
#########################



@when("easter egg")
def jump():
	print("Play the game you egg")


@when("enter temple")
@when("enter the temple")
@when("enter treasure site")
def enter_temple():
	global current_room
	if current_room == Jungle: #checks if user is outside temple to proceed into temple
		print("You enter the temple into the main room. You are ready to seek the treasure")
		current_room = MainTempleRoom
	else:
		print("You are already in the temple")
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
    if current_room == BurialTomb or current_room == DeathRoom:
        print("you have died!")
        quit()

	

#this code is for the word look, this code informs the user of their surroundings once they say look+ the room exits and items.
@when("look")
def look():
	print(current_room)
	print("There are exits to the ",current_room.exits())
	if len(current_room.item) > 0:
		print("You also see:")
		for item in current_room.item:
			print(item)

#This code is picking items and it makes sure the item is in the room and exists and if it does it informs the user they picked up the item while if it doesnt it says it doesnt see an item
@when("pick ITEM")
@when("pick up ITEM")
@when("get ITEM")
@when("take ITEM")
def get_item(item):
	#checked if item is in room
	#take it out of room
	#put into inventory
	#otherwise tell user there is no item
	if item in current_room.item:
		t = current_room.item.take(item)
		inventory.add(t)
		print(f"You picked up the {item}")
	else:
		print(f"You don't see a {item}")

@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)




#this code is too search the skeleton in the deadend room to get a note to break into the treasure room
@when("search skeleton")
@when("look through skeleton")
@when("search the skeleton")
def search_body(): #sets up variables for search
	global skeleton_searched
	if current_room == DeadEnd and skeleton_searched == False:
		print("you search the skeleton and find a note containing a code")
		current_room.item.add(note)
		skeleton_searched = True
	elif current_room == DeadEnd and skeleton_searched == True:
		print("You have already searched the skeleton")
	else:
		print("There is no skeleton here to search")


#the code below simply makes the item description print out when the user wants to see it
@when("look at note")
@when("look note")
@when("read note")
def look_note():
	print(note.description)

@when("look at sword")
@when("look sword")
@when("read sword")
def look_sword():
	print(sword.description)


#code below checks if the user has the note item in their inventory and if they are in the lock room to either let the user into the treasure room or deny their entry
@when("use ITEM")
def use(item):
	if item == note and current_room == LockRoom:
		print("You use the note which contains the code on the old locked door, it rumbles down revealing a chest with many treasures. ")
		LockRoom.east = TreasureRoom
	elif "note" not in inventory:
		print("You don't have a note")
	else:
		print("There is no where to use the note.")






#this code is for the trap room and makes the user cut the bushes with their sword to move onto new room
@when("cut bushes")
@when("cut through bushes")
def cut_bush():
	if current_room == TrapRoom and "sword" in inventory:
		print("You have cut through the bushes and revealed new paths on your quest to treasure.")
		TrapRoom.north = HallwayRoom
		TrapRoom.west = BurialTomb
		cut_bush == True
	elif "sword" not in inventory:
		print("You don't have a sword, search for it.")
	else:
		print("There are no bushes left")



#this code is for the bush room and makes the user cut the bushes with their sword to move onto new room
@when("cut trees")
def bush_cut():
	if current_room == BushRoom and "sword" in inventory:
		print("You have cut through the bushes and revealed new paths on your quest to treasure.")
		BushRoom.north = DeadEnd
		BushRoom.south = BurialTomb
		bush_cut == True
	elif "sword" not in inventory:
		print("You don't have a sword, search for it.")
	else:
		print("There are no bushes left")




#this code is for the game ending and it checks if the user has killed the boss before they do the final input which is open treasure which leads to game victory
@when("open treasure")
def treasureroom_win():
	if boss == True and current_room == TreasureRoom:
		print("The chest is opened revealing millions of dollars of jewels. You have evaded the death this elusive temple brings. You are now a rich man with a story to tell.")
		game_start = False
		quit()
	else:
		print("There is no treasure anywhere")

#BOSS FIGHT ########################################STILL TO BE WORKED ON################
if current_room == TreasureRoom and boss == False:
   print("You must fight the boss to take the treasure")
#defining health variables for the fight
player_health = 10
boss_health = 20




























#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
	#start the main loop

main()