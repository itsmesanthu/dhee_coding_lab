a1=[]
i=0
while True:
    num=int(input("enter the value: "))
    a1.insert(i,num)
    i+=1
    print("do you wish to contine")
    print("pess 1: yes")
    print("pess 2: no")
    choice=int(input())
    if choice==1:
        continue
    else:
        break
print(a1)

# Create list
a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Type of list
print(type(a))
# Print list
print(a)
# Length of list
print(len(a))   # 9
# Indexing
print(a[1])     # 20
print(a[7])     # 80
# Slicing examples
print(a[4:7])   # [50, 60, 70]
print(a[7:])    # [80, 90]
# Negative slicing (may return empty if range invalid)
print(a[-3:-8])    
# Reverse slicing
print(a[-3:-8:-1])
print(a[:-5:-1])
print(a[6::-1])
# More slicing
print(a[-1:-2:-1])
print(a[::3])
print(a[-2::2])
print(a[-8:-5:0])   # NOTE: step cannot be 0 (will cause error)