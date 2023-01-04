import csv


class Student:

    def __init__(self, name=None, rollno=None, city=None):
        self.name = name
        self.rollno = rollno
        self.city = city
        self.lst = []

    def check_csv(self):
        header = ["Name", "Rollno", "City"]
        with open('D:/sandeep/Student_system.csv', 'r') as f:
            csvreader = csv.reader(f)
            if header not in csvreader:
                with open('D:/sandeep/Student_system.csv', 'w', newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=header)
                    writer.writeheader()
                    f.close()

    def add_details(self):
        self.lst.append([self.name, self.rollno, self.city])
        for i in range(len(self.lst)):
            f = open('D:/sandeep/Student_system.csv', 'a', newline="")
            self.check_csv()
            writer = csv.writer(f)
            writer.writerow(self.lst[i])
            f.close()

    def search(self, word):
        with open('D:/sandeep/Student_system.csv', 'r') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                if word in row:
                    print(f"Name: {row[0]}\n"
                          f"Rollno: {row[1]}\n"
                          f"City: {row[2]}")
                    break
            else:
                print("Not found. Try again !")

    def display(self):
        with open('D:/sandeep/Student_system.csv', 'r') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                print(f"Name: {row[0]}\n"
                      f"Rollno: {row[1]}\n"
                      f"City: {row[2]}\n")
            print("===============================")

    def update(self, roll_n):
        with open('D:/sandeep/Student_system.csv', 'r') as f:
            csvreader = csv.reader(f)
            csv_lst = []
            for row in csvreader:
                csv_lst.append(row)
                if roll_n in row:
                    print(f"Name: {row[0]}\n"
                          f"Rollno: {row[1]}\n"
                          f"City: {row[2]}\n")
        for row in csv_lst:
            if roll_n in row:
                row[0] = input("Enter Name: ")
                row[1] = input("Enter Rollno: ")
                row[2] = input("Enter City: ")
                print("====Updated Successfully====")
                break
        else:
            print("Not found. Try again !")
        with open('D:/sandeep/Student_system.csv', 'w') as f:
            pass
        for row in csv_lst:
            f = open('D:/sandeep/Student_system.csv', 'a', newline="")
            writer = csv.writer(f)
            writer.writerow(row)
            f.close()

    def delete(self, rol_n):
        with open('D:/sandeep/Student_system.csv', 'r') as f:
            csvreader = csv.reader(f)
            csv_lst = []
            for row in csvreader:
                csv_lst.append(row)
                if rol_n in row:
                    print(f"Name: {row[0]}\n"
                          f"Rollno: {row[1]}\n"
                          f"City: {row[2]}\n")
        for row in csv_lst:
            if rol_n in row:
                con = input("Are you sure? Y/N: ")
                if con == ("Y" or "y"):
                    csv_lst.remove(row)
                    print("====Deleted Successfully====")
                    break
                break
        else:
            print("Not found. Try again !")

        with open('D:/sandeep/Student_system.csv', 'w') as f:
            pass
        for row in csv_lst:
            f = open('D:/sandeep/Student_system.csv', 'a', newline="")
            writer = csv.writer(f)
            writer.writerow(row)
            f.close()


if __name__ == "__main__":

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
            std_1 = Student()
            std_1.display()
        elif cntn == 3:
            word = input("Please enter rollno for search: ")
            std_1 = Student()
            std_1.search(word)
        elif cntn == 4:
            roll_n = input("Please enter rollno for update: ")
            std_1 = Student()
            std_1.update(roll_n)
        elif cntn == 5:
            rol_n = input("Please enter rollno for delete: ")
            std_1 = Student()
            std_1.delete(rol_n)
        else:
            break
