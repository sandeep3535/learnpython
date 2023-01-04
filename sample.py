import random
import os
import time

main_list = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
new_main_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
comp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_with_x(user_inp, comp_inp,  main_list, new_main_list):
    for i in range(3):
        for j in range(3):
            if main_list[i][j] == int(user_inp):
                if new_main_list[i][j] == " " and user_inp != comp_inp:
                    new_main_list[i][j] = "X"
                else:
                    print(f"Board {user_inp} already filled. Try again..!")
                    user_inp = int(input("Player_2: "))
            if main_list[i][j] == comp_inp:
                if new_main_list[i][j] == " " and comp_inp != user_inp:
                    new_main_list[i][j] = "O"
                else:
                    print(f"Board {comp_inp} already filled. Try again..!")
                    comp_inp = int(input("Player_1: "))
            if j != 2:
                print(new_main_list[i][j], end=" | ")
            else:
                print(new_main_list[i][j], end=" ")
        print()


def check_draw():
    for row in new_main_list:
        for item in row:
            if item == " ":
                return False
    return True


for i in range(3):
    for j in range(3):
        if j != 2:
            print(main_list[i][j], end=" | ")
        else:
            print(main_list[i][j], end="")
    print()

con = True
while con:
    comp_inp = int(input("Player_1: "))
    check_with_x(user_inp, comp_inp, main_list, new_main_list)
    user_inp = int(input("Player_2: "))
    check_with_x(user_inp,comp_inp, main_list, new_main_list)
    for j in range(3):
        if all(new_main_list[i][j] == "X" for i in range(3)):
            print("You win")
            con = False
        elif all(new_main_list[i][j] == "O" for i in range(3)):
            print("Computer win")
            con = False
        elif all(new_main_list[j][i] == "X" for i in range(3)):
            print("You win...!")
            con = False
        elif all(new_main_list[j][i] == "O" for i in range(3)):
            print("Computer win")
            con = False
        elif all(new_main_list[i][i] == "X" for i in range(3)):
            print("You win...!")
            con = False
            break
        elif all(new_main_list[i][2 - i] == "X" for i in range(3)):
            print("You win...!")
            con = False
            break
        elif all(new_main_list[i][i] == "O" for i in range(3)):
            print("Computer win")
            con = False
            break
        elif all(new_main_list[i][2 - i] == "O" for i in range(3)):
            print("Computer win")
            con = False
            break
    if check_draw():
        print("match draw...!")
        break
