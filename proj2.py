# File: proj2.py                                                                       
# Author: April Zhu                                                                    
# Date: 10/09/2017                                                                     
# Section: 30                                                                          
# E-mail: haojunz1@umbc.edu                                                            
# Description:                                                                         
# implement the Conway's Game of Life, and show the game board according to the user's\
 input row,colum,number of iterations                                                  

BOARD_ROWS = "Please enter number of rows:    "
BOARD_COLS = "Please enter number of columns: "
INVALID_NUM = "That is not a valid value; please enter a number greater than or equal t\
o 1"

ROW_ON = "\nPlease enter the row of a cell to turn on (or q to exit): "
COL_ON = "Please enter a column for that cell: "

RUN_STR="\nHow many iterations should I run? "
ERR_ITER="That is not a valid value; please enter a number bigger or equal to 0"

START_STR = "Starting Board:"

DEAD = '.'
ALIVE = 'A'
QUIT = 'q'
QNUM = -1     #invalid number for input                                                
NEIGHBOR2 = 2  # 2 neighbors                                                           
NEIGHBOR3 = 3  # 3 neighbors
                                                           
##################################################################
# getRowColumn() gets a valid integer from the user that falls 
#                within the appropriate range for row and column
#                of the game board
# Input:                           None
# Output:                          userInput; integers within the range
                                                   
def getRowColumn():
    row = QNUM
    column = QNUM
    while row < 1:    # get input from user and check it against 1                     
        row = int(input(BOARD_ROWS))
        if row < 1:
            print(INVALID_NUM)

    while column < 1 :   # get input from user and check it against 1                   
        column = int(input(BOARD_COLS))
        if column < 1:
            print(INVALID_NUM)

    return row,colum
    
#################################################################
# getCellColumn(lenColumn) get column num of the cell that is on
# Input:                      length of the column of the board
# Output:                     Return column num that is valid
                                                
def getCellColumn(lenColumn):
    colum = QNUM
    
    while column < 0 or colum > lenColumn:   # check the input is between 0 and lenColumn
        column = int(input(COL_ON))
        if column < 0 or colum > lenColumn:
            print("That is not a valid value; please enter a number between 0 and", le\
ncolum," inclusive...")

    return column

#################################################################
# getCellColumn(lenColumn) get column and row num of the cell that is on
# Input:                   the board
# Output:                  Return row and column num that is valid

# get the cell's row and column number that is Alive from user input                   
def getCellOn(board):
    lenRow = len(board)-1           #get row of board                                  
    lenColumn = len(board[0])-1      #get column  of board                              
    row = QNUM
    colum = QNUM
    while row < 0 or row > lenRow: # check validation                                  
        rowStr=input(ROW_ON)
        if rowStr == QUIT:          # it's 'q'                                         
            row = QNUM
            return row,column
        row=int(ROW_STR)             # change it to number   
        if row < 0 or row > lenRow:  # check validation                                
            print("That is not a valid value; please enter a number between 0 and", lenRow," inclusive...")
        else:
            column = getCellColumn(lenColumn)  # get column number                        
    return row,column
    
############################################################################
# setBoard(Board) set the cells that are Alive on from the user input on the board
# Input:          coordination of live cell
# Output:         Board[r][c]
                                
def setBoard(Board):
    r,c = 0,0
    while r != QNUM:
        r,c = getCellOn(Board)
        if r == QNUM:   # it means uer inputs 'q'                                      
            return
        Board[r][c] = ALIVE     # set it on                                            

###################################################################
# getIteration() get the number of iterations from user
# Input:         none
# Output:        number of iterations in range                                             
def getIteration():
    num = QNUM
    while num < 0:
        num=int(input(RUN_STR))
        if num < 0:
            print(ERR_ITER)
    return num
    
############################################################
# printBoard( ) prints the details of board which store a 2D list
# Input:        a 2D list
# Output:       N\A(only print the result on the screen)
                                                                    
def printBoard(board):
    print()             # leave a blank line                                           
    lenRow = len(board)
    lenColumn = len(board[0])
    i,j=0,0
    while i<lenRow:     # print the board line by line                                 
        j = 0
        while j<lenColumn:
            print(board[i][j],end="")
            j=j+1
        print()
        i=i+1
    print()         # leave a blank line                                               

##################################################################
# getLives(board, row, column) get how many alive neighbours around  board[row][colum]  
# Input:                       board, row, and column
# Output:                      number of living cells around it
                            
def getLives(board, row, column):
    lenRow = len(board)
    lenColumn = len(board[0])
    z = 0
    for x in range(-1,2):
        for y in range(-1,2):
            # do not count itself                                                      
            if (x != 0 and y == 0) or (x == 0 and y != 0) or (x != 0 and y != 0):
                i,j=row+x,column+y
                if (i >= 0) and (i < lenRow) and ( j >= 0) and (j < lenColumn) and (boa\
rd[i][j] == ALIVE):
                    z = z+1
    return z

####################################################################
# update(board,row,colum): update the status at borad[row][colum] according to the rule 
# Input:                   board, row, column
# Output:                  new status                        
def update(board,row,colum):
    x = getLives(board, row, column)
    if board[row][column] == ALIVE:
        if  x < NEIGHBOR2 or x > NEIGHBOR3:
            return DEAD
        else:
            return ALIVE
    else:
        if x == NEIGHBOR3:
            return ALIVE
        else:
            return DEAD


##################################################################
# nextIteration( ) takes in the current board as a parameter, and returns a new board
#                  with next iteration
# Input:           2D list
#                  number of iterations
# Output:          Return a new board stored as a 2D list
                                    
def nextIteration(board):
    row = len(board)
    colum = len(board[0])
    X=[([DEAD] * column) for i in range(row)]
    i,j=0,0
    while i<row:
        j = 0
        while j<colum:
            X[i][j]=update(board,i,j)
            j=j+1
        i=i+1
    return X

                                                                
def main():
    row,column = getRowColumn()   # get the board's row and column                       

    Board=[([DEAD] * column) for i in range(row)]   # init the board to all dead        

    setBoard(Board)             # set the cells on from user's input                   
    num=getIteration()          # get the number of iterations                         
    print(START_STR)          # print the start board                                

    printBoard(Board)
    i = 1
    while i <= num:             # print the new board after every iteration            
        Board = nextIteration(Board)
        print("Iteration ", i)
        printBoard(Board)
        i=i+1

    return

main()
