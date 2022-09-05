# Tims practice shit
print ("Welcome to the tip calculator.")
total = input ("What was the total bill? $")
percent = input ("What percentage tip would you like to give? %")
partysize = input ("How many people to split the bill? ")
tipamt = float(percent)/100+1
amt = "{:.2f}".format(round(float(total) * tipamt / int(partysize), 2))
print (f"Each person should pay ${amt}")

# Compare this snippet from rockPaperScissors.py:
# # Rock Paper Scissors
# import random
#
