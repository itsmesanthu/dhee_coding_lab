'''class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        super().__init__()
        self.b=20
class C(B):
    def __init__(self):
        super().__init__()
        self.c=30
cf=C()
print(cf.c)
print(cf.b)
print(cf.a)
class A:
    def __init__(self):
        self.a=10
    def display(self):
        print("inside A")
class B(A):
    def  display(self):
        print("inside B")
class C(B):
    def display(self):
        print("inside C")
class D(C):
    def dispD(self):
        C.display(self)
        B.display(self)
        A.display(self)
d=D()
d.dispD()'''
'''a=int(input("a="))
b=int(input("b="))
c=a/b
print(c)
print("pgm is end")'''
a=int(input("a="))
b=int(input("b="))
try:
    c=a/b
    print(c)
except Exception as e:
    print("error in pgm")
print("pgm is end")