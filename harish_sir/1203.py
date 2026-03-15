'''class Student:
    def _init_(self):
        self.__name=''
    @property
    def getset (self):
        return self.__name
    @getset.setter
    def getset(self, value):
        self.__name=value

s = Student()
s.getset="rama"
r=s.getset
print(r)'''"""

class demo:
    def __private_method(self,a,b):
        return a+b
    def __private_method(self,a,b):
        return a*b
    def calculate(self):
        add= self.__private_method(5,13)
        mul= self.__private_method(10,30)
        print(add)
        print(mul)
d=demo()
d.calculate()"""
'''class parent:
    def __init__(self):
        self.a=10
class child(parent):
    def __init__(self):
        self.b=20
cf=child()
print(cf.b)
print(cf.a)'''
'''class parent:
    def __init__(self):
        self.a=10
class child(parent):
    def __init__(self):
        parent.__init__(self)
        self.b=20
cf=child()
print(cf.b)
print(cf.a)'''
'''def liner(arr):
    s=0
    for i in range(len(arr)):
        s=s+arr[i]
    return s

arr=[10,20,30]
sum=liner(arr)
print(sum)'''
'''def array_sum(arr):
    total = 0
    for i in arr:
        total = total + i
    return total

arr = []
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("Sum of array:", array_sum(arr))'''
def second_largest(arr):
    arr = list(set(arr))
    return arr
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print(arr)
print("Second largest element:", second_largest(arr))