'''
Fibonicci series:
* the initial 2 position vals is 0 and 1
*the next position val is the sum of previos 2 position val in range  1<=pos<=natural number
*intially n1=0,n2=1
        n1 task :
                    1. display the current cycle val
                    2. hold the next cycle val (n1=n2)
        n2 task :
                    1. first update n1
                    2. hold the future cycle val
        temp task:
                    1. before modifying n1 and n2 , temaporaily hold sum of n1+n2
                    2. pass the sum of n1+n2 to n2

'''
def fiboseries(pos):
    n1,n2=0,1
    while pos>0:
        print(n1, end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
        pos-=1
pos=int(input("enter the  position : "))
fiboseries(pos)