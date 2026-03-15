'''num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    i = 2
    while i * i <= num:
        if num % i == 0:
            print("Not a Prime Number")
            break
        i += 1
    else:
        print("Prime Number")
        '''
'''def isprimenum(n):#n=10
    countFact, i = 0, 1 #2,3
    while i * i <= n:#1*1<=10,2*2<=10,
        if n % i == 0:#10%1=0,10%2==0
            countFact += 1 #2
            if i != (n // i): #1!=(10//1),2!=(10//2)
                countFact += 1#3
        i += 1
    return countFact == 2
n = int(input("Enter a number: "))
flag = isprimenum(n)
if flag:
    print("Prime Number")
else:
    print("Not a Prime Number")
'''
def isprimenum(n):#n=10
    countFact, i = 0, 1 #2,3
    while i * i <= n:#1*1<=10,2*2<=10,
        if n % i == 0:#10%1=0,10%2==0
            countFact += 1 #2
            if i != (n // i): #1!=(10//1),2!=(10//2)
                countFact += 1#3
        i += 1
    return countFact == 2
n = int(input("Enter a number: "))
num = 2
count = 0
while count < n:
    if isprimenum(num):
        print(num, end=" ")
        count += 1
    num += 1

