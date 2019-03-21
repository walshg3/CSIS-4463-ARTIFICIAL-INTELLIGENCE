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
puzzlelist= []
puzzle = open("sudokus/s01a.txt")
for row in puzzle:
    puzzlelist.append([int(cell) for cell in row.split()])
puzzle.close()
#print(puzzlelist)
#remove the close file []
puzzlelist = puzzlelist[:9]

#forward checking
def _forward_check(constraint,index,value):
    newlist=[]
    for option in constraint.availability_list:
        if option[index]==value:
            #constraint.availability_list.remove(option)
            newlist.append(option)
    constraint.availability_list = newlist

def forward_check():
    for i,row in enumerate(puzzlelist):
        for j,cell in enumerate(row):
            if cell != 0:
                if not len(constraints[i])==1:
                    _forward_check(constraints[i],j,cell)
                if not len(constraints[i])==1:
                    _forward_check(constraints[j+9],i,cell)


#DFS
def hey():
    #propogate

    #assign solved

    #assign for dfs
    pass

for i in range(18):
    print(len(constraints[i].availability_list))
print(constraints[16].availability_list)
