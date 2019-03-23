#!/usr/bin/python
from itertools import permutations
import math

full_availability = set(permutations([1,2,3,4,5,6,7,8,9]))
#def constraint class
class Constraint:
    
    __slots__=["availability_list","cells"]

    def __init__(self,constraint_num,new=True):
        if(new):
            self.availability_list= full_availability.copy()
            if constraint_num <9:
                self.cells = [9*constraint_num+i for i in range(9)]
            elif(constraint_num<18):
                self.cells = [(constraint_num%9)+9*i for i in range(9)]
            else:
                self.cells=[27*math.floor((constraint_num%9)/3)+3*(constraint_num%9%3)+i for i in range(3)]+\
                        [9+27*math.floor((constraint_num%9)/3)+3*(constraint_num%9%3)+i for i in range(3)]+\
                        [18+27*math.floor((constraint_num%9)/3)+3*(constraint_num%9%3)+i for i in range(3)]
                

        #print(self.cells)
    
    def copy(self):
        temp = Constraint(False)
        temp.availability_list=self.availability_list.copy()
        temp.cells = self.cells
        return temp



# global list of constraints
class BoardState:
    
    def __init__(self,new = True):
        if(new):
            self.constraints = [Constraint(i) for i in range(27)]

            self.puzzlelist= []
            puzzle = open("sudokus/s02a.txt")
            for row in puzzle:
                self.puzzlelist.append([int(cell) for cell in row.split()])
            self.puzzlelist = self.puzzlelist[:9]
            puzzle.close()
    
    def get_availability_list(self,cell):
        row = math.floor(cell/9)
        column = cell%9
        availability = set()
        for option in self.constraints[row].availability_list:
            availability.add(option[column])
        return availability

    def copy(self):
        temp = BoardState(False)
        temp.puzzlelist = self.puzzlelist[:]
        temp.constraints = [i.copy() for i in self.constraints]
        return temp

#global 2d array for puzzle
#print(puzzlelist)
#remove the close file []

#forward checking
def _forward_check(constraint,index,value):
    newlist=[]
    for option in constraint.availability_list:
        if option[index]==value:
            #constraint.availability_list.remove(option)
            newlist.append(option)
    constraint.availability_list = newlist

def forward_check(board):
    for i,row in enumerate(board.puzzlelist):
        for j,cell in enumerate(row):
            if cell != 0:
                if not len(board.constraints[i].availability_list)==1:
                    _forward_check(board.constraints[i],j,cell)
                if not len(board.constraints[i].availability_list)==1:
                    _forward_check(board.constraints[j+9],i,cell)
'''
def _propogate(constraint,index,avail):
    newlist=[]
    for option in constraint.availability_list:
        if option[index] in avail:
            newlist.append(option)
    changed = True if len(newlist)!=len(constraint.availability_list) else False
    constraint.availability_list = newlist
    return changed

def propogate(board):
    changed = False
    for i in range(81):
        availability = board.get_availability_list(i)
        row = math.floor(i/9)
        column = i%9
        changed = _propogate(board.constraints[row],column,availability) 
        if len(board.constraints[row].availability_list)==0:
            return 0
        changed = _propogate(board.constraints[column+9],row,availability) or changed
        if len(board.constraints[column+9].availability_list)==0:
            return 0
    
    if changed:
        return propogate(board)
'''

def propogate(board):
    changed = False
    for constraint in board.constraints:
        if len(constraint.availability_list)==1:
            print("skip")
            continue
        for other_constraint in board.constraints:
            for i,cell in enumerate(constraint.cells):
                for j,other_cell in enumerate(other_constraint.cells):
                    if cell == other_cell:
                        break
                else:
                    continue
                #print(j)
                S = set()
                for option in constraint.availability_list:
                    S.add(option[i])
                #print(S)
                newlist = set()
                for option in other_constraint.availability_list:
                    if(option[j] in S):
                        newlist.add(option)
                changed = changed or len(newlist)!=len(other_constraint.availability_list)
                other_constraint.availability_list=newlist
    print(changed)
    if(changed):
        propogate(board)

#DFS
def visit(board,index):
    #propogate
    forward_check(board)
    if(propogate(board)==0):
        return 0
    #for each value
    #assign 
    if(index == 81):
        return board
    for value in board.get_availability_list(index):
        print("-----")
        print(index)
        print(value)
        nextboard = board.copy()
        nextboard.puzzlelist[math.floor(index/9)][index%9] = value
        s = visit(nextboard,index+1)
        if s != 0:
            return s
    return 0


board = BoardState()
#forward_check(board)
#propogate(board)
#print([i for i in board.get_availability_list(0)])
#print(board.get_availability_list(1))

'''
forward_check(board)
for i in range(18):
    print(len(board.constraints[i].availability_list))
propogate(board)
for i in range(18):
    print(len(board.constraints[i].availability_list))
'''
#print([u.cells for u in board.constraints])
print(visit(board,0).puzzlelist)
