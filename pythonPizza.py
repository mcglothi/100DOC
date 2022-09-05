print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0
if extra_cheese == "Y":
    price += 1
if size == "S":
    if add_pepperoni == "Y":
        price += 17
    else:
        price += 15
elif size == "M": 
    if add_pepperoni == "Y":
        price += 23
    else:
        price += 20
else: 
    if add_pepperoni == "Y":
        price += 28
    else:
        price += 25
print (f"Your final bill is: ${price}.")