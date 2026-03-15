def gcd(n1,n2):
    if n1==0:
        return n2
    if n1<n2:
        n1,n2=n2,n1
    return gcd((n1%n2),n2)
def ccp(n1,n2):
    if n1==0:
        return n2==1
    if n1<n2:
        n1,n2=n2,n1
    return gcd((n1%n2),n2)
num1=int(input("enter the n1:"))
num2=int(input("enter the n2: "))
res=gcd(num1,num2)
print(res)
print("=============================")
flag=ccp(num1,num2)
print(flag)
print("=============================")
def  gcdloop(n1,n2):
    while n1>0:
        if n1 < n2:
            n1, n2 = n2, n1
        return gcd((n1 % n2), n2)
o=gcdloop(num1,num2)
print(o)
print("=============================")
def coploop(n1,n2):
    while n1>0:
        if n1 < n2:
            n1, n2 = n2, n1
        n1=n1%n2
        return n2 ==1
c=coploop(num1,num2)
print(c)