def auto(n):
    s=n*n
    temp=n
    d=0
    while n>0:
        if n%10:
            d+=1
        n=n//10
    l=s%(10**d)
    return l==temp
n=int(input("entre number:"))
flag=auto(n)
if flag:
    print(f"the number {n} is automorphic number ")
else:
     print(f"the number {n} is not a  automorphic number ")