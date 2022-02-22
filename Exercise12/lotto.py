from random import seed
from random import randint
print("This version uses the randint method")
seed(1)
choice = input("Would you like some help picking your lottery numbers? Type Y for yes or Q to quit")
while choice.upper() == "Y":
    print("Your lucky numbers are:")
    for n in range(6):
        value = randint(0,50)
        print(value)
    print("Good luck!")
    choice = input("Would you like some help picking your lottery numbers? Type Y for yes or Q to quit")
if choice.upper() == "Q":
    print("Very sensible, you're more likely to get struck by lightning anyway, why not stick a bet on that?!")


