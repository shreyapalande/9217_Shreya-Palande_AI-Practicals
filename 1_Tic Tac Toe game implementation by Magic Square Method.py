import random

csymbol = "X"
usymbol = "O"


def exp1():

    while True:
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        end = False
        MagicSquare = [8, 1, 6, 3, 5, 7, 4, 9, 2]

        while True:
            usymbol = input('Choose X or O: ').capitalize()
            if (usymbol != "X" and usymbol != "O"):
                print("Incorrect symbol")
                # exit(0)
            elif (usymbol == "X"):
                csymbol = "O"
                break
            else:
                csymbol = "X"
                break

        def PrintBoard():
            print()
            print('', board[0], "|", board[1], "|", board[2])
            print("---|---|---")
            print('', board[3], "|", board[4], "|", board[5])
            print("---|---|---")
            print('', board[6], "|", board[7], "|", board[8])
            print()

        def GetNumber():
            while True:
                number = input("Enter a number from the numbers avaliable in the grid to play: ")
                try:
                    number = int(number)
                    if number in range(1, 10):
                        return number
                    else:
                        print("\nNumber not on board")
                except ValueError:
                    print("\nThat's not a number. Try again")
                    continue

        def Turn(player, symbol):
            global ans

            if (player == "user"):
                placing_index = GetNumber() - 1

            elif (player == "computer"):
                for x in range(9):
                    for y in range(9):
                        if x != y:
                            if (board[x] == csymbol and board[y] == csymbol):
                                ans = 15-(MagicSquare[x]+MagicSquare[y])
                                if (ans > 0 and ans <= 9):
                                    for i in range(9):
                                        if MagicSquare[i] == ans:
                                            placing_index = i
                                            if board[placing_index] == "X" or board[placing_index] == "O":
                                                break
                                            board[placing_index] = csymbol
                                            return
                            elif (board[x] == usymbol and board[y] == usymbol):
                                ans = 15-(MagicSquare[x]+MagicSquare[y])
                                if (ans > 0 and ans <= 9):
                                    for i in range(9):
                                        if MagicSquare[i] == ans:
                                            placing_index = i
                                            if board[placing_index] == "X" or board[placing_index] == "O":
                                                break
                                            board[placing_index] = csymbol
                                            return
                            else:
                                if (board[0] == 1):
                                    placing_index = 0
                                elif (board[2] == 3):
                                    placing_index = 2
                                elif (board[6] == 7):
                                    placing_index = 6
                                elif (board[8] == 9):
                                    placing_index = 8
                                else:
                                    placing_index = (random.randint(1, 9))-1
            if board[placing_index] == "X" or board[placing_index] == "O":
                print("\nBox already occupied. Try another one. ")
                Turn(player, usymbol)
            else:
                board[placing_index] = symbol

        def CheckWin(player):
            count = 0

            for x in range(9):
                for y in range(9):
                    for z in range(9):
                        if x != y and y != z and z != x:
                            if board[x] == player and board[y] == player and board[z] == player:
                                if MagicSquare[x] + MagicSquare[y] + MagicSquare[z] == 15:
                                    print("Player", player, "wins!\n")
                                    return True

            for a in range(9):
                if board[a] == "X" or board[a] == "O":
                    count += 1
                if count == 9:
                    print("The game ends in a Tie\n")
                    return True

        while not end:

            PrintBoard()
            end = CheckWin(usymbol)
            if end == True:
                break
            print("User's turn to play: ")
            Turn("user", usymbol)

            PrintBoard()
            end = CheckWin(csymbol)
            if end == True:
                break
            print("Computer's turn to play: ")
            Turn("computer", csymbol)

        if input("Do you want to play again? (y/n): ").lower() != "y":
            break


exp1()
