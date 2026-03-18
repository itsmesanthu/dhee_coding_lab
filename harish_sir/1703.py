'''class Heart:
    def __init__(self, name):
        self.hname = name
        print("Heart is alive")

    def getheart(self):
        print("Heart is accessing")


class Car:
    def __init__(self, name):
        self.cname = name
        print("Car is ready")

    def getcar(self):
        print("Car is ready to drive")


class Person:
    def __init__(self, name):
        self.pname = name
        self.h = Heart("hooo")   
        self.c1 = None
        print("Person is ready")
        print("With heart connected")

    def hasperson(self, c):
        self.c1 = c
        print("Person and Car connected")

P = Person("nnn")
cf=Car("nnn")
P.hasperson(cf)
print(P.pname)
print(P.c1.cname)
print(P.h.hname)
P.h.getheart()
P.c1.getcar()
del P'''
class A:
    def dispA(self):
        print("a")
print(A.mro())
class B:
    def dispB(self):
        print("B")
print(B.mro())
class C(A,B):
    def dispC(self):
        print("c")
print(C.mro())