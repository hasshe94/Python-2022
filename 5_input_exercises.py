#1
input("Press any key.\n")
#2
input("What is your name?\n")
#3
input("What is your age?\n")
#4
user_name = input("What is your name?\n")
#5
user_age = int(input("What is your age?\n"))
#6
fave_movie = input("What is your favorutie movie?\n")
#7
book_name = input("Name a book.\n")
#8
adjective_name = input("Give an adjective.\n")
#9
noun_name = input("Give a noun.\n")
#10
verb_name = input("Give a verb.\n")
#11
print(f"Hello {user_name} welcome to my program.\n")
print(f"You are {user_age} years old which means in 10 years you will be {user_age + 10} years old!\n")
print(f"Your favourite movie which is {fave_movie} is a pretty decent movie and a good choice!\n")
print(f"{book_name} is a pretty bad book not gonna lie.\n")
print(f"The adjective you chose, {adjective_name} perfectly describes you!!!!\n")
print(f" {noun_name} is a pretty weird thing.\n")
print(f"The verb you chose, {verb_name} is exactly what im doing right now.\n")
#12
user_age1 = int(input("What is your age?\n"))
#13
print(f"In 10 years you will be {user_age1+10} years old.\n")
#14
print(f"You were born in {2022 - user_age1}.\n")
#15
user_apples = int(input("How many apples do you have?\n"))
#16
user_friends = int(input("How many friends do you have?\n"))
#17
print(f"You can share this many apples with each friend: {int(user_apples/user_friends)}. And you will have {user_apples%user_friends} left over")
#18
user_pizza = int(input("How many pizzas do you want?\n"))
#19
user_feed = int(input("How many people are you feeding?\n"))
#20
print(f"You can share this many pizza slices with each friend: {int(user_pizza/user_feed * 8)}. And you will have {user_pizza%user_feed} left over")
#21
user_money = int(input("How much money do you have?\n"))
#22
user_tv = int(input("How much does a tv cost?\n"))
#23
print(f"you will have {user_money - user_tv} dollars after buying the TV")
#24
print(f"The tv will cost {user_tv * 0.8} if you wait for a %20 sale")
#25
user_bitcoin = int(input("How much bitcoin do you have?\n"))

