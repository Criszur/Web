import random
count = 0
dicerolls = 0
def dicerolls ():
    return random.randint (1,6)
user = int(input("How many games would you like to roll ?"))
for i in range (user):
    guesses = dicerolls()
    print("The guess is", guesses)
