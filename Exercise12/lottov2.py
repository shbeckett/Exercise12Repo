from random import seed
from random import sample
print("This version uses the sample method")
seed(1)
choice = input("Would you like some help picking your lottery numbers? Type Y for yes or Q to quit")
while choice.upper() == "Y":
    sequence = [n for n in range(50)]
    subset = sample(sequence,6)
    print("Your lucky numbers are: " + str(subset))
    choice = input("Would you like some help picking your lottery numbers? Type Y for yes or Q to quit")
if choice.upper() == "Q":
    print("Very sensible, you're more likely to get struck by lightning anyway, why not stick a bet on that?!")