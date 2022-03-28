#1
user_icecream = int(input("How many ice creams do you need?\n"))
if user_icecream >18:
  print("There isn't enough ice cream in stock.\n")
#2
user_travel = int(input("How far do you intend to travel?\n"))
if user_travel >200:
  print("Remember to fill up with petrol before you leave.\n")
#3
user_age = int(input("How old are you?\n"))
if user_age >=18:
  print("You are now considered an adult.\n")
elif user_age <18:
  print("You are a minor.\n")
#4
user_movie = input("What is your favourite movie?\n")
if user_movie == "Lord of the Rings":
  print("You have an excellent taste in film.\n")
else:
    print("Lord of the Rings is clearly a superior film\n.")
#5 
user_plagueis = input("Have you heard of the tale of Darth Plagueis the wise?\n")
if user_plagueis == "No" or "no":
  print("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.\n")
else:
    print("You must be a fan?\n.")
#6
passion_movie = input("Who directed the Passion Of Christ?\n")
if passion_movie == "MEL GIBSON" or "mel gibson" or "Mel Gibson":
  print("correct")
else:print("Mel Gibson did\n")
#7
user_score = 0
point_score = 1
score_1 = int(input("What is 9+10?\n"))
if score_1 == 21:
  print(f"correct you have {user_score + 1} points.\n")
  user_score = user_score +1
else:
  print(f"incorrect you have {user_score} points.\n")
score_2 = int(input("What is 9+10?\n"))
if score_2 == 19:
  print(f"correct you have {user_score + 1} points.\n")
  user_score = user_score +1
else:
  print(f"incorrect you have {user_score} points.\n")
score_3 = int(input("What is 9*10?\n"))
if score_3 == 90:
  print(f"correct you have {user_score + 1} points.\n")
  user_score = user_score +1
else:
  print(f"incorrect you have {user_score} points.\n")
score_4 = int(input("What is 9+1?\n"))
if score_4 == 10:
  print(f"correct you have {user_score + 1} points.\n")
  user_score = user_score +1
else: