def counting(n, count):
    if n<=0:
        return count
    n=n//10
    count +=1
    return counting(n, count)
def isasn(n,pow,asn,temp):
    if n<=0:
        return asn==temp
    base=n%10
    asn=asn+(base**pow)
    n=n//10
    return isasn(n,pow,asn,temp)

n = int(input("enter the number"))
pow = counting(n, 0)
flag=isasn(n,pow,0,n)
if flag:
    print("asn number")
else:
    print("non asn number")