def pattern_A():
    for row in range(7):
        for colm in range(5):
            if (colm in range(1, 4) and row == 0) or row == 3:
                print("*", end=" ")
            elif (colm == 0 or colm == 4) and row != 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\r")


def pattern_B():
    for row in range(7):
        for colm in range(5):
            if colm in range(0, 4) and (row == 0 or row == 6 or row == 3):
                print("*", end=" ")
            elif colm == 0 or (colm == 4 and row in range(1, 6)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\r")


def pattern_C():
    for row in range(7):
        for colm in range(5):
            if row in range(1, 6) and colm == 0:
                print("*", end=" ")
            elif colm in range(1, 5) and row not in range(1, 6):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\r")


def pattern_D():
    for row in range(7):
        for colm in range(5):
            if row in range(0, 7) and colm == 0:
                print("*", end=" ")
            elif row in range(1, 6) and colm == 4:
                print("*", end=" ")
            elif colm in range(1, 4) and row not in range(1, 6):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\r")

