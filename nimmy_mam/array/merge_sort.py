def merge(a, left, mid, right):
    i = left
    j = mid + 1
    k = 0

    c = [0] * (right - left + 1)

    while i <= mid and j <= right:
        if a[i] <= a[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = a[j]
            j += 1
        k += 1

    while i <= mid:
        c[k] = a[i]
        i += 1
        k += 1

    while j <= right:
        c[k] = a[j]
        j += 1
        k += 1

    for i in range(len(c)):
        a[left + i] = c[i]

def mergesort(a,left,right):
    if(left<right):
        mid=(left+right)//2
        mergesort(a,left,mid)
        mergesort(a,mid+1,right)
        merge(a,left,mid,right)
a=[100,-5,6,20,21,7,5,9,11,5]
mergesort(a,0,len(a)-1)
print(a)