'''
1. The sample() function randomly selects N items from a given collection (list, tuple, string, dictionary, set) and returns them as a list.
2. It returns in the form of list.
3. If size of subset is more than size of given collection then we get value error  
'''
from random import *

# Select any three chars from a string
#print(sample('Python',3))


# Randomly select a subset of size three from a given set of strings
print(sample({'Python', 'C++', 'Java', 'Go'}, 3))


# Randomly select a tuple of three elements from a base tuple
print(sample((21, 12, -31, 24, 65, 16.3), 4))

# Randomly select a list of three elements from a base list
print(sample([11, 12, 13, 14, -11, -12, -13, -14], 5))

# Randomly select a subset of size three from a given set of numbers
print(sample({110, 120, 130, 140}, 5))



