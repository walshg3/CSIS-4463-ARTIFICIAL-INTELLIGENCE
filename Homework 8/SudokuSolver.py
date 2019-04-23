#!/usr/bin/python
#   @author Brain Fox and Greg Walsh
#  ______      _              ______                          _   _____                  _    _       _     _     
#    ___ \    (_)             |  ___|                        | | |  __ \                | |  | |     | |   | |    
#  | |_/ /_ __ _  __ _ _ __   | |_ _____  __   __ _ _ __   __| | | |  \/_ __ ___  __ _  | |  | | __ _| |___| |__  
#  | ___ \ '__| |/ _` | '_ \  |  _/ _ \ \/ /  / _` | '_ \ / _` | | | __| '__/ _ \/ _` | | |/\| |/ _` | / __| '_ \ 
#  | |_/ / |  | | (_| | | | | | || (_) >  <  | (_| | | | | (_| | | |_\ \ | |  __/ (_| | \  /\  / (_| | \__ \ | | |
#  \____/|_|  |_|\__,_|_| |_| \_| \___/_/\_\  \__,_|_| |_|\__,_|  \____/_|  \___|\__, |  \/  \/ \__,_|_|___/_| |_|
#                                                                                 __/ |                           
#                                                                                |___/                             
# DFS visit:
#   for each cell sequentially:
#       
#       if cell has been assigned skip
#       for values in cell's availability list:
#
#           assign cell
#           run propagation
#           if any cell has availabilty list of length 0
#               backtrack
#           
#           assign all cells with availability list of length 1
#           propagate on those cells
#           if any cell has availabilty list of length 0
#               backtrack
#           
#   
import math
import sys
from timeit import timeit
from collections import deque
# Counter used for counting backtracking
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
            return [int(27*math.floor((constraint_num%9)/3)+3*(constraint_num%9%3)+i) for i in range(3)]+\
                    [int(9+27*math.floor((constraint_num%9)/3)+3*(constraint_num%9%3)+i) for i in range(3)]+\
                    [int(18+27*math.floor((constraint_num%9)/3)+3*(constraint_num%9%3)+i) for i in range(3)]
                
# global
constraints = [make_constraints(i) for i in range(27)]
limited = deque()

class BoardState:
    
    def __init__(self,puzzle,new = True):
        if(new):
            self.availability_lists = [['1','2','3','4','5','6','7','8','9'] for i in range(81)]
            self.assigned = set()
            self.puzzle_list= puzzle
    
    def copy(self):
        """
        Copies the Boardstates puzzle_list, availability_list, and assigned list
        """
        temp = BoardState(False)
        temp.puzzle_list = self.puzzle_list[:]
        temp.availability_lists = [alist[:] for alist in self.availability_lists]
        temp.assigned = self.assigned.copy()
        return temp


def forward_check(board):
    """
    Forward checks the board and adds cell to the assigned list
    Input: board
    """
    for i,cell in enumerate(board.puzzle_list):
        if cell != '0':
            board.assigned.add(i)
            propagate(board,i)

def propagate(board,cell):
    """
    limits the availability list of all cells limited by the cell
    at a given index
    """
    global limited
    for constraint in constraints:
        if cell in constraint:
            for other_cell in constraint:
                if other_cell in board.assigned :
                    continue
                #remove assigned value from availability lists
                if board.puzzle_list[cell] in board.availability_lists[other_cell]:
                    board.availability_lists[other_cell].remove(board.puzzle_list[cell])
                    if len(board.availability_lists[other_cell])==0:
                        #break this leg of DFS if puzzle is unsolvable in current state
                        limited = deque()
                        return False
                    elif len(board.availability_lists[other_cell])==1:
                        limited.append(other_cell)
    
    return True
    '''if(len(limited)!=0):
        for c in limited:
            print(cell)
            print(c)
            if board.puzzle_list[c] == '0':
                board.puzzle_list[c] = board.availability_lists[c][0]
            if not propagate(board,c):
                return False
    '''

#DFS
def visit(board,index):
    """
    DFS assigns values to cells. Backtracks when a constraint is violated
    """
    if(index == 81):
        return board

    global limited

    if index in board.assigned:
        return visit(board,index+1)

    for value in board.availability_lists[index]:
        nextboard = board.copy()
        nextboard.puzzle_list[index] = value
        nextboard.assigned.add(index)

        if (not propagate(nextboard,index)):
            continue
            
        #assign values which have been shown to have one possible value in last propagate call
        while(len(limited)>0):
            limited_cell = limited.pop()
            nextboard.puzzle_list[limited_cell] = nextboard.availability_lists[limited_cell][0]
            nextboard.assigned.add(limited_cell)
            if not propagate(nextboard,limited_cell):
                continue
        
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
    puzzle_list = []
    try :
        puzzle = open(name)
    except:
        print("could not find that file")
        exit()
    for row in puzzle:
        for cell in row.split():
            puzzle_list.append(cell)
    puzzle.close()
    board=BoardState(puzzle_list)
    forward_check(board)
    return visit(board,0).puzzle_list

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

if __name__=="__main__":
    if(len(sys.argv)==1):
        print("Hello!", "\n", "Please enter path to Sudoku puzzle to solve (You can find available Sudoku files in the sudokus folder)")
        puzzle_name = input()
    else:
        puzzle_name = sys.argv[1]
    t = timeit(lambda : output(solve(puzzle_name)),number =1)
    print("\nTime taken to solve: "+ str(t))

    
    
