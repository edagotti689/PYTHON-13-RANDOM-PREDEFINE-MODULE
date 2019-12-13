'''
1. randrange() is used to generate a random integer number b/w given range(start<=x<stop)
2. we rquired three arguments randrange(start,stop,step)
'''
import random

# start default value is 0
print(random.randrange(20))


#step is optional default value is 1
j = random.randrange(10,26)
print(j)


i = random.randrange(10,26,2)
print(i)
