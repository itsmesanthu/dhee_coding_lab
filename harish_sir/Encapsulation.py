class without:
    def __init__(self):
        self.balance=1000
a=without()
print(a.balance)
a.balance=2000
print("without:",a.balance)

class withE:
    def __init__(self):
        self.__balance=1000
    def show(self):
        print("with:",self.__balance)
b=withE()
# print(b.__balance).    . AttributeError: 'withE' object has no attribute '__balance'
# access a private variables 
# 1 call method 
b.show()
#Name Mangling
#Python changes the name of a private variable internally.

print(b._withE__balance)


class Bank:

    def __init__(self):
        self.__balance = 10000

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        self.__balance = amount

obj = Bank()

print("Old Balance:", obj.get_balance())

obj.set_balance(20000)

print("New Balance:", obj.get_balance())

#         Object
#            │
#            ▼
#     +----------------+
#     | __balance      |  ← Private Variable
#     +----------------+
#       ▲          ▲
#       │          │
#  Getter()     Setter()
#  (Read)      (Update)
 
#  example one 
class Student:

    def __init__(self, mark):
        self.__mark = mark      # Private variable

    # Getter Method
    def get_mark(self):
        return self.__mark

    # Setter Method
    def set_mark(self, new_mark):
        if 0 <= new_mark <= 100:
            self.__mark = new_mark
        else:
            print("Invalid Marks")


# Create Object
student1 = Student(97)

# Get Marks
print("Current Marks:", student1.get_mark())

# Update Marks
student1.set_mark(85)
print("Updated Marks:", student1.get_mark())

# Invalid Update
student1.set_mark(120)
print("Final Marks:", student1.get_mark())

#student age
class studentage:
    def __init__(self,age):
        if 5<age<25:
            self.__age= age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 5<age<25:
            self.__age=age
        else:
            print("invaild")
s1=studentage(18)
print("Current Age:",s1.get_age())
# s1.set_age(22)
# print("update Age:",s1.get_age())
# s1.set_age(45)
# print("final age:",s1.get_age())

#Mobile Battery