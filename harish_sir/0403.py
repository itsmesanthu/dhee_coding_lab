'''a=10
def fun1():
    print(a)
    b=20
    print(b)
def fun2():
    print(a)
    c=30
    print(c)
print(a)
fun1()
print(a)
fun2()
print(a)'''
'''a=10
def fun1():
    a=100
    print(a)
    b=20
    print(b)
def fun2():
    a=1000
    print(a)
    c=30
    print(c)
    print(a)
print(a)
fun1()
print(a)
fun2()
print(a)'''
'''
def fun1():
    global a
    a=100
    print(a)
    b=20
    print(b)
def fun2():
    global a
    a=1000
    print(a)
    c=30
    print(c)
fun1()
print(a)
fun2()
print(a)'''
#Lambda function
#lambda argument : expressions
'''num=int(input("enter the num : "))
s=lambda num:num+num
print(s(num))'''
# wap to collect only 5 inter element and for the user input and stor in a list
'''l=[]
i=0
while i<=4:
    n=int(input("enter the number"))
    l.insert(i,n)
    i=i+1
print(l)'''
#wap to collect 5 inter value for the user and print only a even number
l = []
i = 0
while i <= 4:
    n = int(input("enter the number"))
    if n % 2 != 0:
        l.insert(i, n)
    i = i + 1
print(l)
