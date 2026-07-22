class studentManagement:
    def __init__(self):
        self.students=[]
    def menu(self):
            while True:
                    try:
                        print("===========student management==============")
                        print("1.   Add student")
                        print("2.   view student")
                        print("3.   update student")
                        print("4.   delete student")
                        print("5.   exit")
        
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
                            print("exit")
                            break
                        else:
                            print("invailed choice.")
                    except ValueError:
                        print("Please enter a number.")
            return
    def add_student(self):
        student={}
        student["name"]=input("enter student name: ")
        for stu in self.students:
            if stu["name"].lower() == student["name"].lower():
                print("Student already exists.")
                return
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
        print("student added Successfully!....")

    def view_student(self):
        if len(self.students)==0:
            print("no students founds")
            return
        print("==========student list=======")
        for i ,stu in enumerate(self.students,start=1):
            print(f"student {i}")
            print("Name : ",stu["name"])
            print("age : ",stu["age"])
            print("class: ",stu["class"])
    def update_student(self):
        self.view_student()
        if len(self.students)==0:
            return
        index=(int(input("enter the st1udent number : ")))-1
        if 0<=index<len(self.students):
            self.students[index]["name"]=input("enter the name : ")
            while True:
                age=int(input("enter the age : "))
                if 6<=age<=18:
                    self.students[index]["age"]=age
                    break
                else:
                    print("invalid age . pleaec enter age again.")
            while True:
                c=int(input("enter the class : "))
                if 1<=c<=10:
                    self.students[index]["class"]=c
                    break
                else:
                    print("Invalid class. Please enter again.")
            print("Student Updated Successfully!")
        else:
            print("invaild student number ")
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
                break
            else:
                print("invalid input plaecs try again...")






s=studentManagement()
s.menu()