'''class a:
    def __init__(self):
        self.a1=10
class b(a):
    def __init__(self):
        a.__init__(self)
        self.b1=20
class c(b):
    def __init__(self):
        b.__init__(self)
        self.c1=30
cf=c()
print(cf.c1)
print(cf.b1)
print(cf.a1)'''
'''class Cargoplane:
    def takeoff(self):
        print("Plane is in takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
    def carry(self):
        print("Plane carry goods")
class Passengerplane:
    def takeoff(self):
        print("Plane is in takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
    def carry(self):
        print("Plane carry passengers")
class Fighterplane:
    def takeoff(self):
        print("Plane is in takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
    def carry(self):
        print("Plane carry weapons")
c = Cargoplane()
p = Passengerplane()
f = Fighterplane()
c.takeoff()
c.fly()
c.land()
c.carry()
p.takeoff()
p.fly()
p.land()
p.carry()
f.takeoff()
f.fly()
f.land()
f.carry()'''
'''class Plane:
    def takeoff(self):
        print("Plane is takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
class Cargo(Plane):
    def carry(self):
        print("Plane carry goods")
class Passenger(Plane):
    def carry(self):
        print("Plane carry passengers")
class Fighter(Plane):
    def carry(self):
        print("Plane carry weapons")
c = Cargo()
p = Passenger()
f = Fighter()
c.takeoff()
c.fly()
c.land()
c.carry()
p.takeoff()
p.fly()
p.land()
p.carry()
f.takeoff()
f.fly()
f.land()
f.carry()'''
class animal:
    def eat(self):
        print("eating")
    def breath(self):
        print("breath")
    def sleep(self):
        print("sleep")
class tigre(animal):

    pass
class deer(animal):
    pass
class mankey(animal):
    pass
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
b.sleep()


'''def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [5, 3, 8, 4, 2]

merge_sort(arr)

print("Sorted array:", arr)'''