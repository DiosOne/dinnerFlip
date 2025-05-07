''' 
This is a docstring for the module.
'''
import random

def is_even(n):
    '''Returns True if the given number is even, False otherwise.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.'''
    if n % 2 == 0:
        return True
    else:
        return False
    print("What are your two options for dinner?")
option1 = input("Option 1: ")
option2 = input("Option 2: ")
print("Your choices are " + option1 + " and " + option2)
print("Flip for " + option1 + " or " + option2 + "?")
input("Press enter to flip")
random_number=random.randint(1,1000)
if is_even(random_number):
    print("Heads, we have " + option1)
else:
    print("Tails, we have " + option2)
