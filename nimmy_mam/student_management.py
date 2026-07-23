import json
class studentManagement:
    def __init__(self):
        try: 
            with open("students.json","r") as file:
                self.students=json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            self.students=[]
    def menu(self):
            while True:
                    try:
                        print("===========student management==============")
                        print("1.   Add student")
                        print("2.   view student")
                        print("3.   update student")
                        print("4.   delete student")
                        print("5.   Search Student")
                        print("6.   total student")
                        print("7.   exit")
        
                        choice=int(input("enter you choice: "))
                        if choice==1:
                            self.add_student()
                        elif choice==2:
                            self.view_student()
                        elif choice==3:
                            self.update_student()
                        elif choice==4:
                            self.delete_student()
                        elif choice==5:
                            self.search_student()
                        elif choice==6:
                            self.total_student()
                        elif choice==7:
                            print("exited...")
                            break
                        else:
                            print("invailed choice.")
                    except ValueError:
                        print("Please enter a number.")
            return
    def add_student(self):
        student={}
        student["id"]=int(input("enter the student id : "))
        for stu in self.students:
            if stu["id"]==student["id"]:
                print("id already taken..")
                return
        student["name"]=input("enter student name: ")
        while True:
            age=int(input("enter the student age:"))
            if age>=6 and age<=18:
                student["age"]=age
                break
            else:
                print("Invalid age. Please enter again.")
        while True:
            c=int(input("enter the class: "))
            if c>=1 and c<=10:
                student["class"]=c
                break
            else:
                print("Invalid class. Please enter again.")
        self.students.append(student)
        self.save_data()
        print("student added Successfully!....")

    def view_student(self):
        self.students.sort(key=lambda x: x["class"])
        if len(self.students)==0:
            print("no students founds")
            return
        print("==========student list=======")
        print("_"*45)
        print(f"{'id':<8}{'name':<15}{'age':<8}{'class'}")
        print("_"*45)
        for stu in self.students:
            print(f"{stu['id']:<8}{stu['name']:<15}{stu['age']:<8}{stu['class']}")
    def update_student(self):
        self.view_student()
        if len(self.students) == 0:
            return
        index = int(input("Enter student number: ")) - 1
        if 0 <= index < len(self.students):
            new_id = int(input("Enter new ID: "))
            for i, stu in enumerate(self.students):
                if i != index and stu["id"] == new_id:
                    print("ID already exists.")
                    return
            self.students[index]["id"] = new_id
            self.students[index]["name"] = input("Enter new name: ")
            while True:
                age = int(input("Enter age: "))
                if 6 <= age <= 18:
                    self.students[index]["age"] = age
                    break
                print("Invalid age.")
            while True:
                c = int(input("Enter class: "))
                if 1 <= c <= 10:
                    self.students[index]["class"] = c
                    break
                print("Invalid class.")
            self.save_data()
            print("Student Updated Successfully!")
        else:
            print("Invalid student number.")
    def delete_student(self):
        self.view_student()
        if len(self.students)==0:
            print("no student data...")
            return
        while True:
            i=(int(input("enter the student number :")))-1
            if 0<=i<len(self.students):
                self.students.pop(i)
                print("student delete successfully!...")
                self.save_data()
                break
            else:
                print("invalid input plaecs try again...")
    def search_student(self):
            name = input("Enter student name: ")
            found = False
            for stu in self.students:
                if stu["name"].lower() == name.lower():
                    print("-" * 45)
                    print(f"{'ID':<8}{'Name':<15}{'Age':<8}{'Class'}")
                    print("-" * 45)
                    print(f"{stu['id']:<8}{stu['name']:<15}{stu['age']:<8}{stu['class']}")
                    found = True
                    break
            if not found:
                print("Student not found.")
    def total_student(self):
       print("Total student is : ",len(self.students))
    def save_data(self):
        with open("students.json","w")as file:
            json.dump(self.students,file)


s=studentManagement()
s.menu()