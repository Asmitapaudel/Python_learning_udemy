print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    pizza_price = 15
elif size == "M":
    pizza_price = 20
elif size == "L":
    pizza_price = 25

if pepperoni == "Y":
    if size == "S":
        pizza_price=pizza_price+2
    else:
        pizza_price=pizza_price+3
else:
    pizza_price =pizza_price

if extra_cheese=="Y":
    pizza_price = pizza_price + 1
else:
    pizza_price =pizza_price


print(f"Your final bill is: ${pizza_price}.")
