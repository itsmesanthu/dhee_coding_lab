def neon(n):
    s=n*n
    temp=s
    sum=0
    while s>0:
        rem=s%10
        sum+=rem
        s=s//10
    return n==sum
n=int(input("enter the number:" ))
flag=neon(n)
if flag:
    print(f"the {n} is neon number")
else:
    print(f"the {n} is not neonß number")