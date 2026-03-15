'''class demo:
    a=10 #static variables
    def __init__(self):
        self.b=17 #instance variables
        self.c=20 #instance variables
    def instanc(self):
        print(self.c) #instance method
        print(self.b) #instance method
    @staticmethod
    def staticdisp(): #satatic method
        print(demo.a) #satatic method
    @classmethod
    def classdisp(cls):
        print("python")  #class method
d1=demo()
demo.staticdisp()
demo.classdisp()
d1.instanc()'''
# tyee of function
'''def fun():
    a=10
    b=13
    c=a+b
    print(c)
def fun2():
    a=10
    b=20
    c=a+b
    return c
def fun3(a,b):
    c=a+b
    print(c)
def fun4(a,b):
    c=a+b
    return c
print(fun)
fun()
print("-------")
r1=fun2()
print(r1)
print("-------")
n1=32
n2=32
fun3(n1,n2)
print("------")
r3=fun4(n1,n2)
print(r3)'''
#passing a function as a parameter
def fun():
    print("inside function")
def fun2(x,y):
    z=x*y
    print(z)
def display(ptr1,ptr2):
    ptr1()
    ptr2(20.10)
print("------")
print(fun)
fun()
print("------")
fun2(3,9)
print("------")
ptr1=fun()
ptr2=fun2(4,2)
#display(ptr1,ptr2)
print("------")