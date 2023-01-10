import pymongo


class Student:

    def __init__(self, name=None, rollno=None, city=None):
        self.name = name
        self.rollno = rollno
        self.city = city

    def add_details(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["stu_data"]
        collection = db["student"]
        key = ["Name", "Rollno", "City"]
        value = [self.name, self.rollno, self.city]
        collection.insert_one(dict(zip(key, value)))

    @staticmethod
    def search(r_no):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["stu_data"]
        collection = db["student"]
        result = collection.find({'Rollno': r_no}, {'_id': 0})
        count = collection.count_documents({"Rollno": r_no})
        if count != 0:
            for item in result:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print()
        else:
            print("Not found. Try again !")

    @staticmethod
    def display(lmt):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["stu_data"]
        collection = db["student"]
        result = collection.find({}, {'_id': 0}).limit(lmt)
        for item in result:
            for key, value in item.items():
                print(f"{key}: {value}")
            print()

    @staticmethod
    def update(roll_n):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["stu_data"]
        collection = db["student"]
        result = collection.find({"Rollno": roll_n}, {"_id": 0})
        count = collection.count_documents({"Rollno": roll_n})
        if count != 0:
            for item in result:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print()
            n = input("Enter Name: ")
            r = int(input("Enter Rollno: "))
            ct = input("Enter City: ")
            _pre = {"Rollno": roll_n}
            _nxt = {"$set": {"Name": n, "Rollno": r, "City": ct}}
            collection.update_one(_pre, _nxt)
        else:
            print("Not found. Try again !")

    @staticmethod
    def delete(rol_n):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["stu_data"]
        collection = db["student"]
        result = collection.find({"Rollno": rol_n}, {"_id": 0})
        count = collection.count_documents({"Rollno": rol_n})
        if count != 0:
            for item in result:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print()
            cond = input("Are you sure? Y/N: ")
            if cond == "Y" or cond == "y":
                collection.delete_one({"Rollno": rol_n})
                print("====Deleted Successfully====")
            else:
                return
        else:
            print("Not found. Try again !")


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
            r = int(input("Enter Rollno: "))
            c = input("Enter City: ")
            if len(n) != 0 and len(str(r)) != 0 and len(c) != 0:
                s1 = Student(n, r, c)
                s1.add_details()
            else:
                print("===============================")
                print("Please enter valid input..!")
        elif cntn == 2:
            limit = int(input("Enter the no of rows you want to display: "))
            std_1 = Student()
            std_1.display(limit)
        elif cntn == 3:
            r_no = int(input("Please enter rollno for search: "))
            std_1 = Student()
            std_1.search(r_no)
        elif cntn == 4:
            roll_n = int(input("Please enter rollno for update: "))
            std_1 = Student()
            std_1.update(roll_n)
        elif cntn == 5:
            rol_n = int(input("Please enter rollno for delete: "))
            std_1 = Student()
            std_1.delete(rol_n)
        else:
            break
