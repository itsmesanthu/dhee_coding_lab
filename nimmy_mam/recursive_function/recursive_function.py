def counting(n, count):
    if n<=0:
        return count
    n=n//10
    count +=1
    return counting(n, count)
n=int(input("enter the number"))
r=counting(n,0)
print(r)