from random import seed
from random import shuffle
print("This version uses the shuffle method to return six random numbers")
seed(1)
choice = input("Would you like some help picking your lottery numbers? Type Y for yes or Q to quit")
while choice.upper() == "Y":
    sequence = [n for n in range(50)]
    shuffle(sequence)
    print("Your lucky numbers are: " + str(sequence[0:6]))
    print("Good luck!")
    choice = input("Would you like some help picking your lottery numbers? Type Y for yes or Q to quit")
if choice.upper() == "Q":
    print("Very sensible, you're more likely to get struck by lightning anyway, why not stick a bet on that?!")
