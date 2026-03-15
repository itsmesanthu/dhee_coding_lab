'''class fan:
    def __init__(self):
        self.brand="usha"
        self.no_of_blades=3
        self.color="black"

f1=fan()
f2=f1
print(f1)
print(f2)
print(f1 is f2)
#evertime the code will run that give  memory location changed

#fromal parameter all variable which occurs in the method difination is call
# and actual parameter all variable which occurs in the methode
class demo:
    def dis(self,x,y):
        temp=x
        x=y
        y=temp
d=demo()
a=10
b=20
print("before swap")
print(a)
print(b)
d1=d.dis(a,b)
print("after swap")
print(a)
print(b)
# default argument and key word argument
class demo:
    def dis(self,x=1,y=2,z=3):
        print(x)
        print(y)
        print(z)
d1=demo()
a=10
b=20
c=30
d1.dis(a,b,c)
print("________")
d1.dis(a,b)
print("________")
d1.dis(a)
print("________")
d1.dis()
d1.dis(c)
print("________")
d1.dis(b,c)
print("________")
d1.dis(z=c)
print("________")
d1.dis(y=b)
print("________")
d1.dis(x=a)'''
class farmar:
    r=2.5
    def __init__(self,pt,tl):
        self.p=pt
        self.t=tl

    def dis(self):
        s1=(self.p*self.t*farmar.r)
        print(s1)
f1=farmar(200000,5)
f2=farmar(300000,3)
f1.dis()
f2.dis()