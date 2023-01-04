class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        area = self.length * self.width
        return area

    def rectangle_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def display(self):
        print("=======Rectangle=======")
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.rectangle_area()}")
        print(f"Perimeter: {self.rectangle_perimeter()}")


class Parallelepipede(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume_rectangle(self):
        volume = self.length * self.width * self.height
        print("-----------------------------")
        print(f"Volume: {volume}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def student_display(self):
        self.display()
        print(f"Section: {self.section}")


class BankAccount:
    def __init__(self, account_num, name, balance):
        self.account_num = int(account_num)
        self.name = str(name)
        self.balance = float(balance)

    def deposit(self, d):
        self.balance = self.balance + d

    def withdraw(self, w):
        if w > self.balance:
            return "Insufficient balance !"
        else:
            self.balance = self.balance - w

    def display(self):
        print(f"Acc No: {self.account_num}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


from math import pi


class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def circle_area(self):
        area = pi * self.r ** 2
        return area

    def circle_perimeter(self):
        perimeter = 2 * pi * self.r
        return perimeter

    def testbelongs(self, x, y):
        if (x - self.a) ** 2 + (y - self.b) ** 2 == self.r ** 2:
            print(f"A point {x, y} belongs to circle C(O, {self.r})")
        else:
            print(f"A point {x, y} does not belongs to circle C(O, {self.r})")


class Computation:
    def __init__(self):
        pass

    def factorial(self, f):
        j = 1
        for i in range(1, f + 1):
            j = i * j
        print(f"Factorial of {f} is: {j}")

    def n_sum(self, n):
        j = 0
        for i in range(1, n + 1):
            j = j + i
        print(f"Sum of first {n} integers is: {j}")

    def test_prime(self, p):
        for i in range(2, 9):
            if p > 2 and p % i == 0:
                print(f"{p} is not a prime number")
                break
            print(f"{p} is a prime number")
            break

    def mul_table(self, m):
        for i in range(1, 11):
            mul = m * i
            print(f"{m} X {i} = {mul}")

    @staticmethod
    def list_div(l):
        lst = []
        for i in range(1, l + 1):
            if l % i == 0:
                lst.append(i)
        print(f"Divisor of {l} is: {lst}")


class Book:
    def __init__(self):
        self.title = str(input("Enter Title of Book: "))
        self.author = str(input("Enter Author Name: "))
        self.price = int(input("Enter Price of Book: "))

    def view(self):
        print("\n")
        print("==========Book Details==========")
        print(f"Book-Title: {self.title}")
        print(f"Book-Author: {self.author}")
        print(f"Book-Price: {self.price}")


