a=[1,2,3,10,12,14,16,30]
b=[-3,-2,0,5,10,15,21,24]
c=[0]*(len(a)+len(b))
i,j,k=0,0,0
while k<len(c):
    if i<=len(a)-1 and j<=len(b)-1:
        if a[i]<b[j]:
            c[k]=a[i]
            k+=1
            i+=1
        else:
            c[k]=b[j]
            k+=1
            j+=1
    else:
        if i<=len(a)-1:
            c[k]=a[i]
            k+=1
            i+=1
        elif j<=len(b)-1:
            c[k]=b[j]
            k+=1
            j+=1
            
print(c)