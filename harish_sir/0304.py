def fun():
    yield 1
    yield 2
    yield 3
    yield 4
res=fun()
for i in res:
    print(i)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
print("========================")
def fun1():
    n=1
    while(n<=10):
        sqr=n*n
        yield sqr
        n=n+1
res1=fun1()
# print(res1.__next__())
# print(res1.__next__())
# print(res1.__next__())
  # print(res1.__next__())
# print(res1.__next__())
# print(res1.__next__())
# print(res1.__next__())
# print(res1.__next__())
print("===================")
for i in res1:
    print(i)
print("=========================")
from abc import ABC, abstractmethod

# Abstract Base Class
class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Petrol Engine Class
class PetrolEngine(Engine):

    def start(self):
        print("Petrol Engine Start")

    def stop(self):
        print("Petrol Engine Stop")


# Diesel Engine Class
class DieselEngine(Engine):

    def start(self):
        print("Diesel Engine Start")

    def stop(self):
        print("Diesel Engine Stop")


# Car Class (uses Engine)
class Car:

    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()


# Object Creation
p = PetrolEngine()
d = DieselEngine()

c = Car(d)

c.start_engine()
c.stop_engine()