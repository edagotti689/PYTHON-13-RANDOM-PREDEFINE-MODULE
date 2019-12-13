'''
1. choice() Returns a randomly selected element from a non-empty sequence such as list,tuple,set,etc.
2. An empty sequence as argument raises an IndexError.
'''
import random

# Generate a random string from the list of strings
print(random.choice( ['Python', 'C++', 'Java'] ))

# Generate a random number from the list [-1, 1, 3.5, 7, 15]
print(random.choice([-1, 1, 3.5, 9, 15]))

# Generate a random number from a uniformly distributed tuple
print(random.choice((1.1, -5, 6, 4, 7)))

# Generate a random char from a string
print(random.choice('Learn Python Programming'))
