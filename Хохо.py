board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

win_combs = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def print_board():
    print(board[0], end="")
    print(board[1], end="")
    print(board[2])

    print(board[3], end="")
    print(board[4], end="")
    print(board[5])

    print(board[6], end="")
    print(board[7], end="")
    print(board[8])


def step_board(step, symbol):
    ind = board.index(step)
    board[ind] = symbol


def get_result():
    win = ""

    for i in win_combs:
        if board[i[0]] == "x" and board[i[1]] == "x" and board[i[2]] == "x":
            win = "x"
        if board[i[0]] == "o" and board[i[1]] == "o" and board[i[2]] == "o":
            win = "o"
    return win



game_over = False
player1 = True

while game_over is False:

    print_board()

    if player1 is True:
        symbol = "x"
        step = int(input("Игрок 1, ваш ход:"))
    else:
        symbol = "o"
        step = int(input("Игрок 2, ваш ход:"))

    step_board(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not player1
    

print_board()
print("победил", win)
