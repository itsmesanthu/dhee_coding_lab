'''
 enter the number :4
1
232
34543
4567654'''
n=int(input(" enter the number :"))
for i in range(1,n+1):
    noc=i
    for j in range(1,i*2):
        if j<i:
            print(noc,end="")
            noc+=1
        else:
            print(noc,end="")
            noc-=1
    print()
'''
enter the number :4
   1
  232
 34543
4567654
'''
n=int(input(" enter the number :"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    noc=i
    for j in range(1,i*2):
        if j<i:
            print(noc,end="")
            noc+=1
        else:
            print(noc,end="")
            noc-=1
    print()