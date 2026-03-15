'''def leapyear():
    y = int(input("enter the year : "))
    if (y % 100!=0 and y %4==0)or (y% 400 ==0):
        print(f"{y} is a leap year ")
    else:
        print(f"{y} this not a leap year ")
d=leapyear()
def leapyear(y):
    return (y % 100 != 0 and y % 4 == 0) or (y % 400 == 0)
y= int(input("enter the year : "))
flags=leapyear(y)
if flags:
    print(f"{y} is a leap year ")
else:
    print(f"{y} this not a leap year ")
from sys import flags


def leapyear(y):
    return (y % 100 != 0 and y % 4 == 0) or (y % 400 == 0)
sr=int(input("enter start year"))
er=int(input("enter the end year : "))
if sr>er:
    print("invalid...")
else:
    print("leap yaer's: ")
    for i in range(sr,(er+1)):
        flags=leapyear(i)
        if flags:
            print(i,end=" ")

flags=leapyear(i)
if flags:
    print(f"{i} this not a leap year ")
else:
    print(f"{i} this all a leap year ")
#wap cont the number of digits in a give number.
n=int(input("enter the number :"))
count=0
if n<0:
    n*=-1
while n>0:
    n=n//10
    count+=1
print(count)
'''
def leapYear(year):
    return(year % 100 !=0 and year % 4==0)or(year % 400 == 0)
sr=int(input("enter start year:"))
er=int(input("enter end year:"))
if sr>er:
    print("Invalid I/P")
else:
    print("Leap year's: ")
    for i in range (sr,(er+1)):
        flag=leapYear(i)
        if flag:
            print(i, end=" ")
    print("\nNon leap yaer's: ")
    for i in range(sr,(er+1)):
        flag =leapYear(i)
        if not flag:
            print(i, end=" ")
'''#create a function
def counting(n):
    count = 0
    if n<0:
        n*=-1
    while n>0:
        n=n//10
        count+=1
    return count

n=int(input("enter the number :"))
h=counting(n)
print(h)
'''