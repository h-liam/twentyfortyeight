import random
print(*[4]*4)

print([[_] * 4 for _ in range(4)])
def random_num_list():
    return [random.choice([0]*40+[2]*9 + [4]) for _ in range(4)]

print("rand", random_num_list())
board_test = [random_num_list() for _ in range(4)]


print("og board")
for row in board_test:
    print(row)


print(list(zip(*board_test))) # * expands list
transposed_board = list(zip(*board_test))

print(list(zip(*transposed_board)))

print(type(transposed_board[0]))

print([list(x) for x in transposed_board])

transposed_board = [list(x) for x in transposed_board]


print("transposed board")
for row in transposed_board:
    print(row)

print(type(transposed_board[0]))
new_board = []
for row in transposed_board:
    non_zeros = [val for val in row if val != 0]
    new_board.append([0] * (len(row) - len(non_zeros)) + non_zeros)

transposed_board = new_board

transposed_back_board = [list(x) for x in list(zip(*transposed_board))]


print("transformed back")
for row in transposed_back_board:
    print(row)
print(transposed_back_board)
