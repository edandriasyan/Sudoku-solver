#sarqum enq matric
a = [
	[5,3,0 ,0,7,0 ,0,0,0],
	[6,0,0 ,1,9,5 ,0,0,0],
	[0,9,8 ,0,0,0 ,0,6,0],

	[8,0,0 ,0,6,0 ,0,0,3],
	[4,0,0 ,8,0,3 ,0,0,1],
	[7,0,0 ,0,2,0 ,0,0,6],

	[0,6,0 ,0,0,0 ,2,8,0],
	[0,0,0 ,4,1,9 ,0,0,5],
	[0,0,0 ,0,8,0 ,0,7,9]	
]

#katarum a algoritmy
def solve(matrix):
    find = find_empty(matrix)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(matrix, i, (row, col)):
            matrix[row][col] = i

            if solve(matrix):
                return True	
            matrix[row][col] = 0

    return False

#stuguma tvyal vandakum kara lini ed arjeqy te voch
def valid(matrix, num, pos):
    # stugum a toxy
    for i in range(len(matrix[0])):
        if matrix[pos[0]][i] == num and pos[1] != i:
            return False

    # stugum a syuny
    for i in range(len(matrix)):
        if matrix[i][pos[1]] == num and pos[0] != i:
            return False

    # stugum a qarakusin
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if matrix[i][j] == num and (i,j) != pos:
                return False

    return True

#matrixy sirun tpelu hamar
def print_board(matrix):
    for i in range(len(matrix)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(matrix[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(matrix[i][j])
            else:
                print(str(matrix[i][j]) + " ", end="")

#gtnum a te vortex a datark vandak
def find_empty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(a)
print("_________________________")
solve(a)
print_board(a)