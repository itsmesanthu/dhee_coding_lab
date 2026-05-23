def harshad(n):
    temp=n
    sum=0
    while n>0:
        rem=n%10
        sum+=rem
        n=n//10
    return temp%sum==0
n=int(input("enter the number:" ))
flag=harshad(n)
if flag:
    print(f"the {n} is harshad number")
else:
    print(f"the {n} is not harshad number")
     