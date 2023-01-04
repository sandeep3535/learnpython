import random
import os
import time


class TicTacToe:
    def __init__(self):
        self.main_list = [[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]
        self.new_main_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.comp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.position_board()

    def check_p1_position(self, p1):
        for i in range(3):
            for j in range(3):
                if self.main_list[i][j] == int(p1):
                    if self.new_main_list[i][j] == " ":
                        self.new_main_list[i][j] = "X"
                    else:
                        print(f"Board {p1} is already filled. Try again..!")
                        p1 = input("Player_1: ")

    def check_p2_position(self, p2):
        for i in range(3):
            for j in range(3):
                if self.main_list[i][j] == int(p2):
                    if self.new_main_list[i][j] == " ":
                        self.new_main_list[i][j] = "O"
                    else:
                        print(f"Board {p2} is already filled. Try again..!")
                        p2 = int(input("Player_2: "))

    def print_game(self):
        for i in range(3):
            for j in range(3):
                if j != 2:
                    print(self.new_main_list[i][j], end=" | ")
                else:
                    print(self.new_main_list[i][j], end="")
            print()

    def check_draw(self):
        for row in self.new_main_list:
            for item in row:
                if item == " ":
                    return False
        return True

    def position_board(self):
        os.system('cls')
        for i in range(3):
            for j in range(3):
                if j != 2:
                    print(self.main_list[i][j], end=" | ")
                else:
                    print(self.main_list[i][j], end="")
            print()

    def check_p1_win(self):
        for j in range(3):
            if all(self.new_main_list[i][j] == "X" for i in range(3)):
                return True
            elif all(self.new_main_list[j][i] == "X" for i in range(3)):
                return True
            elif all(self.new_main_list[i][i] == "X" for i in range(3)):
                return True
            elif all(self.new_main_list[i][2 - i] == "X" for i in range(3)):
                return True

    def check_p2_win(self):
        for j in range(3):
            if all(self.new_main_list[i][j] == "O" for i in range(3)):
                return True
            elif all(self.new_main_list[j][i] == "O" for i in range(3)):
                return True
            elif all(self.new_main_list[i][i] == "O" for i in range(3)):
                return True
            elif all(self.new_main_list[i][2 - i] == "O" for i in range(3)):
                return True


if __name__ == "__main__":
    game_start = TicTacToe()
    while True:
        player_1 = input("Player_1: ")
        game_start.check_p1_position(player_1)
        os.system('cls')
        game_start.print_game()
        if game_start.check_p1_win():
            choice = int(input("Player 1 win. \nPlease Enter 1 for continue and 0 for exit: "))
            if choice == 1:
                game_start = TicTacToe()
                continue
            else:
                break
        if game_start.check_draw():
            choice = int(input("Tie. Please Enter 1 for continue and 0 for exit: "))
            if choice == 1:
                game_start = TicTacToe()
                continue
            else:
                break
        player_2 = input("Player_2: ")
        game_start.check_p2_position(player_2)
        os.system('cls')
        game_start.print_game()
        if game_start.check_p2_win():
            choice = int(input("Player 2 wins. Please Enter 1 for continue and 0 for exit: "))
            if choice == 1:
                game_start = TicTacToe()
                continue
            else:
                break
        if game_start.check_draw():
            choice = int(input("Tie. Please Enter 1 for continue and 0 for exit: "))
            if choice == 1:
                game_start = TicTacToe()
                continue
            else:
                break
