print ("Welcome to Tim's stupid simple Zork rip-off")
print ("Try to find the treasure, it's not too hard")
print ("-------------------------------------------")
s1 = input("You're standing in a field like an idiot. You can go [L]eft or [R]right? ").lower()
if s1 == "l":
    s2 = input("Seems to lead to a lake. Should you try to [S]wim or [W]alk around it? ").lower()
    if s2 == "w":
        s3 = input("There's a house here with three doors, do you try the [R]ed, [B]lue, or [Y]ellow door? ").lower()
        if s3 == "r":
            print ("Well, that was unfortunate. You died. Badly. Can't even say why.")
        elif s3 == "b":
            print("Nothing in here but Gypsies. And death.")
        else:
            print("You found it. Great. Get back to work. There's cake in the break room.")
    else:
        print("Stupid move. Death by strangely aroused alligators was inevitable")
else:
    print("You suffered a horrible death by a coked up angry beaver")