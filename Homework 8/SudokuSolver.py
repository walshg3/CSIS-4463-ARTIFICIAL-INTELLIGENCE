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
                    _forward_check(board.constraints[j+9],i,cell)
                    _forward_check(board.constraints[(math.floor(i/3)*3)+math.floor(j/3)+18],
                            (math.floor(i/3)*3)+j%3,
                            cell)

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
    #forward_check(board)
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
        _forward_check(nextboard.constraints[math.floor(index/9)],index%9,value)
        s = visit(nextboard,index+1)
        if s != 0:
            return s
    return 0

def puzzle_check(puzzle, solution):
    '''
    Checks to see if the puzzle is the correct solution
    Arguments:
        puzzle:  puzzle to be checked
        solution: solution file (.txt)
    Outputs: True or False 
    '''
    solutionfile = open("solutions/"+solution+".txt")
    solutionList = []
    #head = [next(solutionfile) for x in range(12)]
    #print(head)
    for row in solutionfile:
        #print(row[:22])
        solutionList.append([cell for cell in row[:22].split()])
    solutionfile.close()
    # Start Deleting Line not needed 
    # Probably can make this nicer
    del solutionList[0][3]
    del solutionList[0][6]
    del solutionList[1][3]
    del solutionList[1][6]
    del solutionList[2][3]
    del solutionList[2][6]
    del solutionList[3]
    del solutionList[3][3]
    del solutionList[3][6]
    del solutionList[4][3]
    del solutionList[4][6] 
    del solutionList[5][3]
    del solutionList[5][6]
    del solutionList[6]
    del solutionList[6][3]
    del solutionList[6][6]
    del solutionList[7][3]
    del solutionList[7][6]
    del solutionList[8][3]
    del solutionList[8][6]
    del solutionList[9]
    del solutionList[9]
    del solutionList[9]
    del solutionList[9]
    del solutionList[9]

    checklist = []
    for row in solutionList:
        for cell in row:
            checklist.append(cell)
    print(checklist)
    
    return checklist == puzzle

    


    

puzzle_check("test", "s01a_s")
    

'''
board = BoardState()
#print([u.cells for u in board.constraints])
for i in range(9):
    for j in range(9):
        print((math.floor(i/3)*3)+math.floor(j/3))
forward_check(board)
print(visit(board,0).puzzlelist)
'''

