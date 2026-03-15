#wap to display the hcf/gcd of the given 2 number.
'''def findGCD(n1,n2):
    hcf=1 #
    lower =n1
    if n2<n1:
        lower=n2
    for i in range(2,lower+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf
n1=int(input("enter the number"))
n2=int(input("enter the number"))
res=findGCD(n1,n2)
print(f"the GCD of {n1} and {n2} is : {res}")
'''
#wap to display the hcf/gcd of the given 2 number.
def findGCD(n1,n2):
    hcf=1 #
    lower =n1
    if n2<n1:
        lower=n2
    for i in range(2,lower+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf
n1=int(input("enter the number"))
n2=int(input("enter the number"))
res=findGCD(n1,n2)
if res==1:
    print("this is co prime")
else:
    print("this not co prime")
