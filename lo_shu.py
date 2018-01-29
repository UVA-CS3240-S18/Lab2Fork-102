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
for i in range (3):
    print(str(square[i][0]) + '\t' + str(square[i][1]) + '\t' + str(square[i][2]))

# check rows
for i in range(3):
    if square[i][0] + square[i][1] + square[i][2] != 15:
        is_square = False
        print("Row " + str(i) + " fails the test!")
        print(str(square[i][0]) + '\t' + str(square[i][1]) + '\t' + str(square[i][2]))

# check cols
for i in range(3):
    if square[0][i] + square[1][i] + square[2][i] != 15:
        is_square = False
        print("Column " + str(i) + " fails the test!")
        print(str(square[0][i]) + '\t' + str(square[1][i]) + '\t' + str(square[2][i]))

# check diagonals
if square[0][0] + square[1][1] + square[2][2] != 15:
    is_square = False
    print("Left->Right diagonal fails the test!")
    print(str(square[0][0]) + '\t' + str(square[1][1]) + '\t' + str(square[2][2]))

if square[0][2] + square[1][1] + square[2][0] != 15:
    is_square = False
    print("Right->Left diagonal fails the test!")
    print(str(square[0][2]) + '\t' + str(square[1][1]) + '\t' + str(square[2][0]))

if not is_square:
    print("This is not a Lo Shu Magic Square!")
else:
    print("This is a valid Lo Shu Magic Square!")



