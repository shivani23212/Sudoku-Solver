# initialise board
board =[[0, 7, 0, 0, 2, 0, 0, 4, 6],
    [0, 6, 0, 0, 0, 0, 8, 9, 0],
    [2, 0, 0, 8, 0, 0, 7, 1, 5],
    [0, 8, 4, 0, 9, 7, 0, 0, 0],
    [7, 1, 0, 0, 0, 0, 0, 5, 9],
    [0, 0, 0, 1, 3, 0, 4, 8, 0],
    [6, 9, 7, 0, 0, 2, 0, 0, 8],
    [0, 5, 8, 0, 0, 0, 0, 6, 0],
    [4, 3, 0, 0, 8, 0, 0, 7, 0]]


def print_board(board):
    for row in range(0, len(board)): 
        for column in range(0, len(board[row])):
            print(board[row][column], end=" ") # print digit followed by space
            if (column % 3 == 2 and column !=0 and column != (len(board[row]))-1): # vertical line every 3rd digit
                print("|", end=" ")
            if (column % 8 == 0 and column !=0): # at end of every row start next line
                print(end="\n")
        if (row % 3 == 2 and row != 0): # after every 3rd row, print row separator
            print("---------------------")

def empty_space(board):
    for row in range(0, len(board)):
        column_val = board[row].index(0) if 0 in board[row] else None # returns first instance of 0 in 1d list
        if (column_val != None):
            return (row, column_val) # return location of 0
    
    return False

def is_num_valid(board, position, num):

    # if num already exists in row (and not due to us just inserting it) return False
    if num in board[position[0]] and board[position[0]].index(num) != position[1]: return False

    # check if num already exists in column (and not due to us just inserting it) return False
    for i in range(0, len(board)):
       if board[i][position[1]] == num and i != position[0]: return False
    
    # check if num already exists in 3 x 3 grid
    # get index of top left of grid
    row_start_index = position[0] - (position[0]%3)
    col_start_index = position[1] - (position[1]%3)

    for j in range(row_start_index, row_start_index+3):
        for k in range(col_start_index, col_start_index+3):
            if board[j][k] == num and (j != position[0] and k != position[1]): return False

    return True

def is_board_complete(board):
    if not empty_space(board): return True
    else:
        row, column = empty_space(board)

        for i in range(1, 10): # for nums 1 to 9
            if is_num_valid(board, (row, column) , i):
                board[row][column] = i # if num valid, insert it in board

                # recursively run function (filling more squares each time) on updated board
                if is_board_complete(board): return True

                # if previous call to is_board_complete returns False, reset prev square
                board[row][column] = 0
    
    return False

print_board(board)
print("\n")
is_board_complete(board)
print_board(board)