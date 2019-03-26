#!/usr/bin/python
from itertools import permutations
import math

def make_constraints(constraint_num):
        if constraint_num <9:
            return [9*constraint_num+i for i in range(9)]
        elif(constraint_num<18):
            return [(constraint_num%9)+9*i for i in range(9)]
        else:
            return [27*math.floor((constraint_num%9)/3)+3*(constraint_num%9%3)+i for i in range(3)]+\
                    [9+27*math.floor((constraint_num%9)/3)+3*(constraint_num%9%3)+i for i in range(3)]+\
                    [18+27*math.floor((constraint_num%9)/3)+3*(constraint_num%9%3)+i for i in range(3)]
                
constraints = [make_constraints(i) for i in range(27)]
# global list of constraints
class BoardState:
    
    def __init__(self,new = True):
        if(new):
            self.availability_lists = [['1','2','3','4','5','6','7','8','9'] for i in range(81)]
            self.assigned = set()
            self.puzzlelist= []
            while(True):

                try:
                    puzzle = open(input("path: "))
                    break
                except:
                    pass

            for row in puzzle:
                for cell in row.split():
                    self.puzzlelist.append(cell)
            puzzle.close()
    
    def copy(self):
        temp = BoardState(False)
        temp.puzzlelist = self.puzzlelist[:]
        temp.availability_lists = [alist[:] for alist in self.availability_lists]
        temp.assigned = self.assigned.copy()
        return temp


#forward checking
def forward_check(board):
    for i,cell in enumerate(board.puzzlelist):
        if cell != '0':
            board.assigned.add(i)
            propogate(board,i)

def find_conflict(board,cell):
    for constraint in constraints:
        if cell in constraint:
            #check for conflict
            for other_cell in constraint:
                if other_cell == cell:
                    continue
                if board.puzzlelist[other_cell] == board.puzzlelist[cell]:
                    print("\t"+str(cell))
                    print("\t"+str(other_cell))
                    return True
    return False

def propogate(board,cell):
   
    for constraint in constraints:
        if cell in constraint:
            for other_cell in constraint:
                if other_cell in board.assigned :
                    continue
                #remove assigned value from availability lists
                if board.puzzlelist[cell] in board.availability_lists[other_cell]:
                    board.availability_lists[other_cell].remove(board.puzzlelist[cell])
#DFS
def visit(board,index):
    #for each value
    #assign 
    if(index == 81):
        return board
    if index in board.assigned:

        return visit(board,index+1)
    #print(index)
    #print(board.availability_lists[index])
    #print("\t"+str(board.availability_lists[16]))
    for value in board.availability_lists[index]:
        #print("-----")
        #print(index)
        #print(value)
        nextboard = board.copy()
        nextboard.puzzlelist[index] = value
        nextboard.assigned.add(index)
        if(find_conflict(nextboard,index)):
            continue
        propogate(nextboard,index)
        s = visit(nextboard,index+1)
        if s != 0:
            return s
    return 0


board = BoardState()
forward_check(board)
#print([u.cells for u in board.constraints])
print(visit(board,0).puzzlelist)
