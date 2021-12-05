"""Demonstartio of random function"""
from random import choice, random, randint, randrange, uniform

print(random())  # 10 digit float number ranges between 1 and 0
print(randint(1, 10))  # random int number between 1 and 10
print(uniform(1, 10))  # random float values 1 and 10 not including them
print(randrange(10, 100, 5))  # random function with range functonalilty

# random choice
lst1 = ['sharique', 'nargis', 'abhishek', 'shraddha']
print(choice(lst1))
