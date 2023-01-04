import random
import os

class Guessword:
    def __init__(self):
        self.char = None
        self.words = ['rainbow', 'computer', 'science', 'programming',
                      'python', 'mathematics', 'player', 'condition',
                      'reverse', 'water', 'board', 'geeks']
        self.word = random.choice(self.words)

    def guess_char(self):
        lst = ["_" for i in range(len(self.word))]
        lst_1 = [self.word[i] for i in range(len(self.word))]
        turn = len(self.word)

        for i in range(turn * 2):
            print(f"You have {(turn*2)-i} turn to complete the guess.")
            self.char = input("Guess the characters: ")
            os.system('cls')
            if self.char in lst_1:
                lst[lst_1.index(self.char)] = self.char
                lst_1[lst_1.index(self.char)] = "_"
                os.system('cls')
                print(" ".join(lst))
            elif self.char not in lst_1:
                os.system('cls')
                print("Wrong Input. Try again..!")
            if "_" not in lst:
                os.system('cls')
                print("congratulation. You guess the word.")
                return
        print("Out of turn. Game Over")


w1 = Guessword()
w1.guess_char()
