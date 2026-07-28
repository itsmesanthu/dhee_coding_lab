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
                        print("5.   Search Student by id")
                        print("6.   Search Student by name")
                        print("7.   total student")
                        print("8.   exit")
        
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
                            self.search_student_id()
                        elif choice==6:
                            self.search_student()
                        elif choice==7:
                            self.total_student()
                        elif choice==8:
                            print("exit ...!")
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
            try:
                age=int(input("enter the student age:"))
                if age>=6 and age<=18:
                        student["age"]=age
                        break
                else:
                    print("age must be in between 6 to 18")
            except ValueError:
               print("Please enter a valid number.")
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
        print("-"*45)
        print(f"{'id':<8}{'name':<15}{'age':<8}{'class'}")
        print("-"*45)
        for stu in self.students:
            print(f"{stu['id']:<8}{stu['name']:<15}{stu['age']:<8}{stu['class']}")
    def update_student(self):
        self.view_student()

        if not self.students:
            return

        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print("Invalid student ID.")
            return

        for stu in self.students:
            if stu["id"] == student_id:

                stu["name"] = input("Enter new name: ")

                # Update Age
                while True:
                    try:
                        age = int(input("Enter age: "))
                        if 6 <= age <= 18:
                            stu["age"] = age
                            break
                        else:
                            print("Age must be between 6 and 18.")
                    except ValueError:
                        print("Please enter a valid number.")

                # Update Class
                while True:
                    try:
                        c = int(input("Enter class: "))
                        if 1 <= c <= 10:
                            stu["class"] = c
                            break
                        else:
                            print("Class must be between 1 and 10.")
                    except ValueError:
                        print("Please enter a valid number.")

                self.save_data()
                print("Student Updated Successfully!")
                return

        print("Student not found.")
        
    def delete_student(self):
        self.view_student()

        if len(self.students) == 0:
            return

        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print("Invalid ID")
            return

        for stu in self.students:
            if stu["id"] == student_id:
                self.students.remove(stu)
                self.save_data()
                print("Student deleted successfully!")
                return

        print("Student not found.")
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
            json.dump(self.students,file,indent=4)
    def search_student_id(self):
                try:
                    studnet_id =int(input("Enter student id: "))
                except ValueError:
                    print("invaild  student id")
                found = False
                for stu in self.students:
                    if stu["id"] == studnet_id:
                        print("-" * 45)
                        print(f"{'ID':<8}{'Name':<15}{'Age':<8}{'Class'}")
                        print("-" * 45)
                        print(f"{stu['id']:<8}{stu['name']:<15}{stu['age']:<8}{stu['class']}")
                        found = True
                        break
                if not found:
                    print("Student not found.")

s=studentManagement()
s.menu()