arr=[]
print(len(arr))
#print(arr[0])
arr.append(10)
arr.append("abc")
arr.append(23.6)
print(len(arr))
print(arr[len(arr)-1])
arr.append(100)
print(arr)
arr[3]=25
arr.insert(1,455)
print(arr)
arr.insert(20,200)
print(arr)
l2=[1,2,3]
l3=[55,65]
l2.append(l3)
print(l2)
print(l3)
l2[3][1]=72
print(l2)
print(l3)
l4=[5,6]
l5=[100,200,300]
#print(l4)
#WAP to create a dynamic integer array
arr=[]
n=int(input("enter the number of element"))
for i in range(n):
    a=input("enter the number :")
    arr.append(a)
print(arr)