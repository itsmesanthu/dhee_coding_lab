# def strong(n):
#     temp=n
#     sum=0
#     while n>0:
#         a=n%10
#         f=1
#         for i in range(1,a+1):
#             f*=i
#         sum+=f
#         n=n//10

#     return temp==sum
# n=int(input("entre number:"))
# flag=strong(n)
# if flag:
#     print(f"the number {n} is strong number ")
# else:
#      print(f"the number {n} is not a  strong number ")
def strong(n):
    temp=n
    sum=0
    while n>0:
        a=n%10
        f=factor(a)
        sum+=f
        n=n//10
    return temp==sum
def factor(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n=int(input("entre number:"))
flag=strong(n)
if flag:
    print(f"the number {n} is strong number ")
else:
     print(f"the number {n} is not a  strong number ")