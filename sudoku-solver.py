

# This function solve the sudoku recursively using the function ans and the functions defined below.
def ans(mat):
    find = find_empty(mat)
    if not find:
        return True
    else:
        hor, ver = find

    for i in range(1,10):
        if correct(mat, i, (hor, ver)):
            mat[hor][ver] = i

            if ans(mat):
                return True

            mat[hor][ver] = 0

    return False


# This function will find empty space in the sudoku matrix
def find_empty(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return (i, j)  # like y,x coordinate

    return None




# This function is used to print the sudoku matrix in a presentable manner, dividing the matrix into mini cubes.
def print_matrix(mat):
    for i in range(len(mat)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(mat[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")    #end="" because we do not want to go to next line

            if j == 8:
                print(mat[i][j])
            else:
                print(str(mat[i][j]) + " ", end="")
                

#This function checks for a valid value by checking in row,column and the small cube it is part of.
def correct(mat, val, pos):
    # Checking row
    for i in range(len(mat[0])):
        if mat[pos[0]][i] == val and pos[1] != i:
            return False

    # Checking column
    for i in range(len(mat)):
        if mat[i][pos[1]] == val and pos[0] != i:
            return False

    # Check small cubes inside the main matrix
    matrix_row = pos[1] // 3
    matrix_col = pos[0] // 3

    for i in range(matrix_col*3, matrix_col*3 + 3):
        for j in range(matrix_row * 3, matrix_row*3 + 3):
            if mat[i][j] == val and (i,j) != pos:
                return False

    return True




# Code for inputing unsolved sukdoku-matrix from row 1 to 9 with the instruction to include space between the entered numbers.
matrix = []
for i in range(9):
    print("Enter the row",i+1,"with space between numbers")
    hor = [int(x) for x in input().split()]
    matrix.append(hor)
    

print_matrix(matrix)  #Original sudoku-matrix
ans(matrix)
print("_________________________________")
print_matrix(matrix)  #Solved sudoku-matrix
