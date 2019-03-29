#!/usr/bin/python
import sys 
from random import randrange
#print(sys.argv[0])

class Bin:

    def __init__(self,c):
        self.c = c
        self.contents = []
        self.filled = 0

    def add(self,item):
        if self.filled + item > self.c:
            return False
        self.contents.append(item)
        self.filled = self.filled + item
        return True

def generate_random_items(n=10,low_value=1,high_value=10):
    return [int(randrange(low_value,high_value+1)) for i in range(n)]

#print(generate_random_items())

def random_solution(items,c):
    pass

items = generate_random_items()

c = 20


