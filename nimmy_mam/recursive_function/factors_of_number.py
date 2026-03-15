'''def factor(n,i):
    if i*i>n:
        return
    if n%i==0:
        print(i,end=" ")
        if i !=(n//i):
            print((n//i),end=" ")
    factor(n,(i+1))
n=int(input("enter the number : "))
f=factor(n,1)'''


#
#this programe need more memory space for execution os we need writte the code
'''def factor(n,i):
    if i*i>n:
        return
    if n%i==0:
        print(i,end=" ")
        if i !=(n//i):
            print((n//i),end=" ")
    factor(n,(i+1))
def isprimenum(n,i,count):
    if i*i>n:
        return count==2
    if n%i==0:
        count+=1
        if i !=(n//i):
            count+=1
     return isprimenum(n,(i+1),count)
n=int(input("enter the number : "))
f=factor(n,1)
print("=============================")
flag=isprimenum(n,1,0)
print(flag)'''
def factor(n, i):
    if i * i > n:
        return
    if n % i == 0:
        print(i, end=" ")
        if i != (n // i):
            print(n // i, end=" ")
    factor(n, i + 1)
def isprimenum(n, i, count):
    if i * i > n:
        return count == 2
    if n % i == 0:
        count += 1
        if i != (n // i):
            count += 1
    return isprimenum(n, i + 1, count)
n = int(input("Enter the number: "))
factor(n, 1)
print("\n=============================")
flag = isprimenum(n, 1, 0)
print(flag)
