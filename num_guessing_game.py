import random
import os

class Guessgame:
    def __init__(self):
        self.g_num = None
        self.lower = int(input("Enter the lower bound: "))
        self.upper = int(input("Enter the upper bound: "))
        self.num = random.randint(self.lower, self.upper)
        print(f"Guess the number between {self.lower} to {self.upper}.")

    def num_guess(self):
        while True:
            try:
                self.g_num = input("Enter the number: ")
                if int(self.g_num) < self.num:
                    print("You guessed smalled number. Try again..!")

                elif int(self.g_num) > self.num:
                    print("You guessed high number. Try again..!")

                elif int(self.g_num) == self.num:
                    print("Congratulation. You guessed the right number.")
                    contn = int(input("Enter 1 for continue and 0 for exit: "))
                    if contn == 1:
                        self.lower = int(input("Enter the lower bound: "))
                        self.upper = int(input("Enter the upper bound: "))
                        self.num = random.randint(self.lower, self.upper)
                        print(f"Guess the number between {self.lower} to {self.upper}.")
                        continue
                    else:
                        break
            except:
                print("invalid input. Try again..!")



n1 = Guessgame()
n1.num_guess()
