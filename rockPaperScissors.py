import random

r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

l = '-------------------'

img = [r, p, s]
choice = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
npc = random.randint(0,2)

if choice > 2 or choice < 0:
    print("Invalid number, you lose!")
else:
    print("\n\n\n")
    print ("You played")
    print (l)
    print (img[choice])
    print ("Computer played")
    print (l)
    print (img[npc])

    if choice == 0 and npc == 2:
        print("You Win!")
    elif npc == 0 and choice == 2:
        print("You lose!")
    elif npc > choice:
        print("You lose!")
    elif npc < choice:
        print("You win!")
    elif choice == npc:
        print("It's a draw.")