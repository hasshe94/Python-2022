#1
fibonnaci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonnaci)
#2
fav_fruits = ["apple", "banana", "pear", "blueberry", "mango"]
print(fav_fruits)
#3
yt_watch = ["Ali Dawah", "sciencephile the ai", "vsauce", "Mohammed Hijab" ]
print(yt_watch)
#4
empty_list = []
empty_list.insert(0,"Runaway")
empty_list.insert(1,"Gorgeous")
empty_list.insert(2,"Off The Grid")
empty_list.insert(3,"All Falls Down")
empty_list.insert(4,"Champion")
print(empty_list)
#5
books_books = []
input_book1 = input("What is your most favourite book?\n")
input_book2 = input("What is your 2nd favourite book?\n")
input_book3 = input("What is your 3rd favourite book?\n")
input_book4 = input("What is your 4th favourite book?\n")
input_book5 = input("What is your 5th favourite book?\n")
books_books.insert(0,input_book1)
books_books.insert(1,input_book2)
books_books.insert(2,input_book3)
books_books.insert(3,input_book4)
books_books.insert(4,input_book5)
print(books_books)
#6
pizza_toppings = []
input_pizza1 = input("Give me a pizza topping.\n")
input_pizza2 = input("Give me another pizza topping.\n")
input_pizza3 = input("Give me another pizza topping.\n")
input_pizza4 = input("Give me another pizza topping.\n")
input_pizza5 = input("Give me another pizza topping.\n")
pizza_toppings.insert(0,input_pizza1)
pizza_toppings.insert(1,input_pizza2)
pizza_toppings.insert(2,input_pizza3)
pizza_toppings.insert(3,input_pizza4)
pizza_toppings.insert(4,input_pizza5)
print(f"this is your final list of pizza toppings {pizza_toppings}.\n")
#7
fruit_list = ["apples", "plums", "peaches", "pears", "apricots"]
input_fruit = input("Give me a fruit.\n")
if input_fruit == fruit_list:
	print("The fruit is in the list and therefore will not be added")
else:
	input_fruit.insert(5,fruit_list)

