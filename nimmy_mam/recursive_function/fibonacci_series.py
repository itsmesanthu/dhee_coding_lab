'''#wap to pprint fidonacci series
def fibo(pos,n1,n2):
    if pos<=0:
        return
    print(n1,end=" ")
    fibo(pos-1,n2,n1+n2)
pos=int(input("enter the number : "))
fibo(pos,0,1)'''
#wap to print n th fibonaicc series
def fibo(pos):
    if pos<=1:
        return pos
    return  fibo(pos-1)+fibo(pos-2)
pos=int(input("enter thee n th number : "))
h=fibo(pos)
print(f"the element present at pos :{pos} is : {h} ")