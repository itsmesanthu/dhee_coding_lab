'''#has a relationdship delegation
class radio:
    def turnon(self,x):
        if(x==1):
            print("radio is on")

        else:
            print("radio off")
class car:
    def __init__(self,min,max):
        self.cmin=min
        self.cmax=max
        self.r=radio()
c=car(60,120)
print(c.cmax)
print(c.cmin)
c.r.turnon(1)
c.r.turnon(2)'''
#implemantion of has a relationship
#compasition
'''class os:
    def __init__(self):
        self.status=True
        print("os is installing")
    def getos(self):
        print("os is still installing")
class moble:
    def __init__(self,name):
        self.mname=name
        self.o=os()
        print("mobile is created ")
        print("with os installed")
m=moble("iphone")
print(m.mname)
print(m.o.status)
m.o.getos()'''
"""del m
print("after deleting")
print(m.mname)"""
#implementation of aggreation 
class Charger:
    def __init__(self, name):
        self.cname = name
        print("Charger is ready")

    def getCharger(self):
        print("Charger is used for charging")
class Mobile:
    def __init__(self, name):
        self.mname = name
        self.c1 = None
        print("Mobile is ready")
    def hasmobile(self, c):
        self.c1 = c
        print("Both mobile and charger are connected")
m = Mobile("iphone")
charge = Charger("iphone charger")
m.hasmobile(charge)
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()
del m
print(charge.cname)
charge.getCharger()
