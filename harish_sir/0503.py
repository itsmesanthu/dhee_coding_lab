#wap to collect 5 inter value for the user and print only a even number
l = []
i = 0
while i <= 4:
    n = int(input("enter the number"))
    if n % 2 == 0:
        l.insert(i, n)
    i = i + 1
print(l)
'''
def even(num):
    if num%2==0:
        return True
    else:
        return False
l=[]
i=0
while i<=4:
    n=int(input("enter the number"))
    l.insert(i,n)
    i=i+1
print(l)
i=0

while (i <=4):
    n1=l[i]
    status=even(n1)
    if status==True:
        print(l[i])
    i+=1
#fillter():-
def even(num):
    if num%2==0:
        return True
    else:
        return False
l=[]
i=0
while i<=4:
    n=int(input("enter the number"))
    l.insert(i,n)
    i=i+1
print(l)
r=list(filter(even,l))
print(r)
'''
'''l=[]
i=0
while i<=4:
    n=int(input("enter the number"))
    l.insert(i,n)
    i=i+1
print(l)
r=list(filter(lambda num:(num%2==0),l))
print(r)
#mapping the function
l=[]
i=0
while i<=4:
    n=int(input("enter the number"))
    l.insert(i,n)
    i=i+1
print(l)
def operator(data):
    return data+10
r=list(filter(lambda num:(num%2==0),l))
print(r)
r1=list(map(operator,l))
print(r1)
#using lambda function in mapping ():-
l=[]
i=0
while i<=4:
    n=int(input("enter the number"))
    l.insert(i,n)
    i=i+1
print(l)
def operator(data):
    return data+10
r3=list(map(lambda data:data+10,l))
print(r3)'''




'''def outer():
    print("inside outer")
    def inner():
        print("inner side")
    inner()
    print(inner)
outer()
print(outer)'''
# total 5 type of veriables

'''a=10
def outer():
    b=20
    print(a)
    print(b)
    def inner():
        c=30
        print(a)
        print(b)
        print(c)
    inner()
    print(a)
    print(b)
outer()
print(a)'''


'''a=10
def outer():
    global a
    a=25
    b=20
    print(a)
    print(b)
    def inner():
        nonlocal b
        b=45
        c=30
        print(a)
        print(b)
        print(c)
    inner()
    print(a)
    print(b)
outer()
print(a)'''

#LEGB Rule
'''
error
  ^
built in scope
  ^
global scope
 ^
 enclosed scope
 ^
 local scope
 '''
'''x=10
def outer():
    x=15
    def inner():
        x=20
        print(x)
    inner()
outer()'''