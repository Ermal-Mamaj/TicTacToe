repeate = "y"

while repeate.lower() == "y":
    board = [' ' for x in range(9)]

    def print_board():
        row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
        row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
        row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def player_move(icon):
        if icon == 'X':
            player = 1
        elif icon == 'O':
            player = 2
        print(f"Your turn player {player}")

        choice = input("Enter your move (1-9): ").strip()
        while True:
            try:
                choice = int(choice)
                while choice > 9:
                    print("Please enter a number betwen 1 and 9")
                    choice = int(input("Please enter another move (1-9): ").strip())
                while board[choice - 1] != " ":
                    print("That place is alrady taken")
                    choice = int(input("Please enter another move (1-9): ").strip())
            except ValueError:
                print("Your move should be an intenger from 1-9")
                choice = input("Enter your move (1-9): ").strip()
                continue
            else:
                break


        board[choice - 1] = icon

    def is_victory(icon):
        if (board[0] == icon and board[1] == icon and board[2] == icon) or \
           (board[3] == icon and board[4] == icon and board[5] == icon) or \
           (board[6] == icon and board[7] == icon and board[8] == icon) or \
           (board[0] == icon and board[3] == icon and board[6] == icon) or \
           (board[1] == icon and board[4] == icon and board[7] == icon) or \
           (board[2] == icon and board[5] == icon and board[8] == icon) or \
           (board[0] == icon and board[4] == icon and board[8] == icon) or \
           (board[2] == icon and board[4] == icon and board[6] == icon):
            return True
        else:
            return False

    def is_draw():
        if ' ' not in board:
            return True
        else:
            return False

    while True:
        print_board()
        player_move('X')
        print_board()
        if is_victory('X'):
            print("X wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
        player_move('O')
        if is_victory('O'):
            print_board()
            print("O wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
    input("")
    repeate = input("Do u want to play again? y/n : ")