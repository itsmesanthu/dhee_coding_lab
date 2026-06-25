def createarray():
    l=[]
    while True:
        try:
            n=int(input("enter element:"))
            l.append(n)
        except Exception as e:
            return l
def prefix(arr,r,l):
    n=len(arr)
    p=[0]*n
    p[0]=arr[0]
    for i in range(1 ,n):
        p[i]=p[i-1]+arr[i]
    if l == 0:
        return p[r]
    else:
        return p[r] - p[l - 1]

arr=createarray()
r=int(input("enter rigth : "))
l=int(input("enter the left :"))
res=prefix(arr,r,l)
print(res)
