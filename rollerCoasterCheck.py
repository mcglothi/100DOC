print("Welcome to the rollercoaster!")
h = int(input("What is your height? "))
if h >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age > 44 and age < 56:
        charge = 0
    else:
        charge = 1
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    pic = input ("Do you want a photo taken? Y or N: ")
    if pic == "Y":
        bill += 3
    total = bill * charge
    print(f"Your final bill is {total}")
else:
    print("Sorry, you have to grow taller before you can ride.")
