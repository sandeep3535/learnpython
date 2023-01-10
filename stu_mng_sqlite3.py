import sqlite3
import datetime


class Student:

    def __init__(self, name=None, rollno=None, city=None):
        self.name = name
        self.rollno = rollno
        self.city = city

    @staticmethod
    def create_database():
        conn = sqlite3.connect("student_data.db")
        c = conn.cursor()
        c.execute(""" CREATE TABLE IF NOT EXISTS student 
                              (Name text,
                               Rollno int,
                               city text)""")
        conn.commit()
        conn.close()

    def add_details(self):
        conn = sqlite3.connect("student_data.db")
        c = conn.cursor()
        c.execute("INSERT INTO student VALUES (?,?,?)", (self.name, self.rollno, self.city))
        conn.commit()
        conn.close()

    @staticmethod
    def search(r_no):
        conn = sqlite3.connect("student_data.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM student WHERE Rollno = {r_no}")
        result = c.fetchall()
        if len(result) != 0:
            print(f"Name: {result[0][0]}\n"
                  f"Rollno: {result[0][1]}\n"
                  f"City: {result[0][2]}")
        else:
            print("Not found. Try again !")
        conn.commit()
        conn.close()

    @staticmethod
    def display(lmt):
        conn = sqlite3.connect("student_data.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM student LIMIT {lmt} ")
        result = c.fetchall()
        for row in range(len(result)):
            print(f"Name: {result[row][0]}\n"
                  f"Rollno: {result[row][1]}\n"
                  f"City: {result[row][2]}\n")
        conn.commit()
        conn.close()

    @staticmethod
    def update(roll_n):
        conn = sqlite3.connect("student_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM student WHERE Rollno = ?", (roll_n,))
        result = c.fetchall()
        if len(result) != 0:
            print()
            n = input("Enter Name: ")
            r = int(input("Enter Rollno: "))
            ct = input("Enter City: ")
            c.execute(f"UPDATE student SET Name = ?, Rollno = ?, City = ? WHERE Rollno = ?", (n, r, ct, roll_n))
            print("====Updated Successfully====")
            conn.commit()
            conn.close()
        else:
            conn.commit()
            conn.close()
            return

    def delete(self, rol_n):
        conn = sqlite3.connect("student_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM student WHERE Rollno = ?", (rol_n,))
        result = c.fetchall()
        if len(result) != 0:
            cond = input("Are you sure? Y/N: ")
            if cond == "Y" or cond == "y":
                c.execute("DELETE FROM student WHERE Rollno = ?", (rol_n,))
                print("====Deleted Successfully====")
                conn.commit()
                conn.close()
                return
            else:
                conn.commit()
                conn.close()
                return
        else:
            conn.commit()
            conn.close()
            return


if __name__ == "__main__":
    Student.create_database()
    print("=========Welcome=========")
    while True:
        print("===============================")
        print("Enter 1 for Add Details...!")
        print("Enter 2 for Display Details...!")
        print("Enter 3 for Search Details...!")
        print("Enter 4 for Update Details...!")
        print("Enter 5 for Delete Details...!")
        print("Enter 6 for Exit...!")
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        cntn = int(input("Please enter your input here: "))
        print("===============================")
        if cntn == 1:
            n = input("Enter Name: ")
            r = input("Enter Rollno: ")
            c = input("Enter City: ")
            if len(n) != 0 and len(r) != 0 and len(c) != 0:
                s1 = Student(n, r, c)
                s1.add_details()
            else:
                print("===============================")
                print("Please enter valid input..!")
        elif cntn == 2:
            limit = input("Enter the no of rows you want to display: ")
            std_1 = Student()
            std_1.display(limit)
        elif cntn == 3:
            r_no = input("Please enter rollno for search: ")
            std_1 = Student()
            std_1.search(r_no)
        elif cntn == 4:
            roll_n = input("Please enter rollno for update: ")
            std_1 = Student()
            std_1.search(roll_n)
            std_1.update(roll_n)
        elif cntn == 5:
            rol_n = input("Please enter rollno for delete: ")
            std_1 = Student()
            std_1.search(rol_n)
            std_1.delete(rol_n)
        else:
            break
