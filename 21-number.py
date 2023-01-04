import random


class Number:
    def __init__(self):
        self.n_lst = []

    def check(self, num):
        if num == 0:
            return False
        elif num == 1:
            return True
        elif num - self.n_lst[-1] == 1:
            return True
        else:
            return False

    def first_chance(self):
        start = True
        while start:
            print("Your Turn")
            num_count = int(input("How many numbers do you wish to enter?\n[You can enter only 1-3 numbers at a "
                                  "time.]\n>"))
            if num_count in range(1, 4):
                pass
            else:
                print("Number out of range.")
                print("Game Over")
                start = False
                return
            print("Please enter the numbers")
            for i in range(num_count):
                num = int(input("> "))
                if self.check(num):
                    self.n_lst.append(num)
                else:
                    print("You have entered a nonconsecutive value")
                    print("Game Over")
                    start = False
                    return
                if self.n_lst[-1] == 20:
                    print(f"Order of Input after computer turn is:\n{self.n_lst}")
                    print("You Win..!")
                    start = False
                    return
            comp_f = random.randint(1, 3)
            for i in range(comp_f):
                self.n_lst.append(self.n_lst[-1] + 1)
                if self.n_lst[-1] == 20:
                    print(f"Order of Input after computer turn is:\n{self.n_lst}")
                    print("You Loss..!")
                    start = False
                    return
            print(f"Order of Input after computer turn is:\n{self.n_lst}")

    def second_chance(self):
        n = random.randint(1, 3)
        for i in range(1, n+1):
            self.n_lst.append(i)
        print(f"Order of Input after computer turn is:\n{self.n_lst}")
        self.first_chance()


if __name__ == '__main__':
    print("===============Welcome to 21-Number Game================\n")
    chance = int(input("Enter '1' for First chance\nand '2' for Second chance > "))
    n = Number()
    if chance == 1:
        n.first_chance()
    elif chance == 2:
        n.second_chance()
    else:
        chance = 2
        n.second_chance()
