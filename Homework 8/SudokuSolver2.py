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
    
    def __init__(self,puzzle,new = True):
        if(new):
            self.availability_lists = [['1','2','3','4','5','6','7','8','9'] for i in range(81)]
            self.assigned = set()
            self.puzzlelist= puzzle
    
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

def solve(name):
    puzzlelist = []
    puzzle = open("sudokus/"+name+".txt")

    for row in puzzle:
        for cell in row.split():
            puzzlelist.append(cell)
    puzzle.close()
    board=BoardState(puzzlelist)
    forward_check(board)
    return visit(board,0).puzzlelist
    

def puzzle_check(puzzle, solution):
    '''
    Checks to see if the puzzle is the correct solution
    Arguments:
        puzzle:  puzzle to be checked
        solution: solution file (.txt)
    Outputs: True or False 
    '''
    solutionfile = open("solutions/"+solution+"_s.txt")
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
    print(solution)
    for i, item in enumerate(checklist):
        if puzzle[i] != item:
            return False
    return True

puzzle_name = input()
print(puzzle_check(solve(puzzle_name), puzzle_name))
