'''class animal:
    def eat(self):
        print("eating")
    def breath(self):
        print("breath")
    def sleep(self):
        print("sleep")
class tigre(animal):
    def eat(self):
        print("tiger will hunt and eat")
class deer(animal):
    def eat(self):
        print("deer will grab and eat  ")
class mankey(animal):
    def eat(self):
        print("monkey will steal and eat")
c=tigre()
b=deer()
a=mankey()
a.eat()
a.sleep()
a.breath()
c.sleep()
c.eat()
c.breath()
b.breath()
b.eat()
b.sleep()'''
class Plane:
    def takeoff(self):
        print("Plane is takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
class Cargo(Plane):
    def takeoff(self):
        print("Cargo is takeoff")
    def fly(self):
        print("Cargo is flying")
    def land(self):
        print("Cargo is landing")
class Passenger(Plane):
    def takeoff(self):
        print("Passenger is takeoff")
    def fly(self):
        print("Passenger is flying")
    def land(self):
        print("Passenger is landing")
class Fighter(Plane):
    def takeoff(self):
        print("Fighter is takeoff")
    def fly(self):
        print("Fighter is flying")
    def land(self):
        print("Fighter is landing")
def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
c = Cargo()
p = Passenger()
f = Fighter()
allowplane(c)
