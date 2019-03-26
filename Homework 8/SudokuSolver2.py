#!/usr/bin/python
#   @author Brain Fox and Greg Walsh
#   ______      _              ______                          _   _____                  _    _       _     _     
#    ___ \    (_)             |  ___|                        | | |  __ \                | |  | |     | |   | |    
#  | |_/ /_ __ _  __ _ _ __   | |_ _____  __   __ _ _ __   __| | | |  \/_ __ ___  __ _  | |  | | __ _| |___| |__  
#  | ___ \ '__| |/ _` | '_ \  |  _/ _ \ \/ /  / _` | '_ \ / _` | | | __| '__/ _ \/ _` | | |/\| |/ _` | / __| '_ \ 
#  | |_/ / |  | | (_| | | | | | || (_) >  <  | (_| | | | | (_| | | |_\ \ | |  __/ (_| | \  /\  / (_| | \__ \ | | |
#  \____/|_|  |_|\__,_|_| |_| \_| \___/_/\_\  \__,_|_| |_|\__,_|  \____/_|  \___|\__, |  \/  \/ \__,_|_|___/_| |_|
#                                                                                 __/ |                           
#                                                                                |___/                             
from itertools import permutations
import math
# Counter used for counting backtracking
counter =0 
def make_constraints(constraint_num):
        """
        Constrains are that of sudoku rules:
        1-9 in row 
        1-9 in column
        1-9 in the 3x3 matrix 
        """
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
        """
        Copies the Boardstates puzzlelist, availability_list, and assigned list
        """
        temp = BoardState(False)
        temp.puzzlelist = self.puzzlelist[:]
        temp.availability_lists = [alist[:] for alist in self.availability_lists]
        temp.assigned = self.assigned.copy()
        return temp


def forward_check(board):
    """
    Forward checks the board and adds cell to the assigned list
    Input: board
    """
    for i,cell in enumerate(board.puzzlelist):
        if cell != '0':
            board.assigned.add(i)
            propogate(board,i)

def find_conflict(board,cell):
    """
    locates conflicts in constraints
    """
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
    """

    """
   
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
    """

    """
    global counter
    #for each value
    #assign 
    if(index == 81):
        return board
    
    if index in board.assigned:
        return visit(board,index+1)

    for value in board.availability_lists[index]:
        nextboard = board.copy()
        nextboard.puzzlelist[index] = value
        nextboard.assigned.add(index)
        
        counter = counter+1

        if(find_conflict(nextboard,index)):
            continue
        propogate(nextboard,index)
        s = visit(nextboard,index+1)
        if s != 0:
            return s
    return 0

def solve(name):
    """
    Solves the Puzzle using forward_check() and visit()
    Input: name of puzzle from sudokus (Without ".txt")
    returns list of solved Puzzle
    """
    puzzlelist = []
    puzzle = open("sudokus/"+name+".txt")

    for row in puzzle:
        for cell in row.split():
            puzzlelist.append(cell)
    puzzle.close()
    board=BoardState(puzzlelist)
    forward_check(board)
    return visit(board,0).puzzlelist

def output(puzzle):
    '''
    Outputs puzzle in 9x9 format
    Input: Puzzle (Solved Puzzle)
    '''
    n = m = 0
    while m < len(puzzle):
        m = m+9
        print(" ".join(puzzle[n:m]))
        n = m

def puzzle_check(puzzle, solution):
    '''
    Checks to see if the puzzle is the correct solution
    Arguments:
        puzzle: puzzle to be checked
        solution: solution file (.txt)
    Outputs: True or False 
    '''
    solutionfile = open("solutions/"+solution+"_s.txt")
    solutionList = []
    for row in solutionfile:
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
    # Check if the AI's solution is the actual solution
    for i, item in enumerate(checklist):
        if puzzle[i] != item:
            return False
    return True

print("Hello!", "\n", "Please Enter Sudoku puzzle to solve (You can find available Sudoku in the sudokus folder)")
puzzle_name = input()
output(solve(puzzle_name))
#output(solve("hard"))
#print(puzzle_check(solve(puzzle_name), puzzle_name))i
#print("\n",counter)
