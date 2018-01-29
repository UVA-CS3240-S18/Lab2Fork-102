# Mark Sherriff (mss2x)

numbers = (input("Numbers: ")).split()

square = [[0,0,0],[0,0,0],[0,0,0]]

count = 0

is_square = True

for i in range(3):
    for j in range(3):
        square[i][j] = int(numbers[count])
        count += 1
# print(square)
print("You entered:")
for row in square:
    print(str(row[0]) + '\t' + str(row[1]) + '\t' + str(row[2]))

# check rows
for i in range(3):
    if sum(square[i]) != 15:
        is_square = False
        print("Row " + str(i) + " " + str(square[i]) + " fails the test!")

# check cols
for i in range(3):
    if square[0][i] + square[1][i] + square[2][i] != 15:
        is_square = False
        t_square = list(map(list, zip(*square)))
        print("Column " + str(i) + " " + str(t_square[i]) +  " fails the test!")

# check diagonals
if square[0][0] + square[1][1] + square[2][2] != 15:
    is_square = False
    print("Left->Right diagonal [" + str(square[0][0]) + ", " + str(square[1][1]) + ", " + str(square[2][2]) + "] fails the test!")

if square[0][2] + square[1][1] + square[2][0] != 15:
    is_square = False
    print("Right->Left diagonal [" + str(square[0][2]) + ", " + str(square[1][1]) + ", " + str(square[2][0]) + "] fails the test!")

if not is_square:
    print("This is not a Lo Shu Magic Square!")
else:
    print("This is a valid Lo Shu Magic Square!")



