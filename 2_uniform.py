'''
1. uniform() is used to generate a floating point random number between the numbers mentioned in its arguments.

2. it returns float number b/w given range(stat<x<stop)
'''

import random

k = random.uniform(5,10)
print(k)


def sample(a,b):
    print(random.uniform(a,b))
sample(10,20)
sample(20,25)
sample(1,5)


