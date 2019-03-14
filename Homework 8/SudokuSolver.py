#!/usr/bin/python
from itertools import permutations

full_availability = list(permutations([1,2,3,4,5,6,7,8,9]))
#def constraint class
class Constraint:
    
    __slots__=["availability_list","cells"]

    def __init__(self,constraint_num):
        self.availability_list= full_availability[:]
        if constraint_num <9:
            self.cells = [(constraint_num,i) for i in range(9)]
        else:
            self.cells = [(i,constraint_num-9) for i in range(9)]

        #print(self.cells)


# global list of constraints
constraints = [Constraint(i) for i in range(18)]
#global 2d array for puzzle

#forward checking

#DFS
def hey():
    #propogate

    #assign solved

    #assign for dfs
    pass

print(constraints[0].availability_list)
