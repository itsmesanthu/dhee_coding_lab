#sets
s1={10,20,30,40,50}
print(s1)
print(type(s1))
#example 2
s2={10,20,20,10,30,40,20,30,40}
print(s2)
print(len(s2))
#example 3
s3={"rama",33.33,True}
print(s3)
#example 4
s4={}
print(type(s4))
#example 5
s5={10,20,30,40,50}
# print(s5[0])
# print(s5[1:4])
#set doesnot support for indexing and  slicinbg
a={10,20,30,40,50}
print(a)
for i in a:
    print(i)
for i,j in enumerate(a):
    print(i," ",j)
a1={10,20,30,40,50}
for i in a1:
    print(i," ",hash(i))
a2={"rama","sita","Rama","Sita"}
for i in a2:
    print(i," ",hash(i))
a3={10.2,20.3,40.2,30.32}
for i in a3:
    print(i," ",hash(i))
a4={True,False,True,False}
for i in a4:
    print(i," ",hash(i))
    print("==============")
    print(i," ",abs(hash(i)))
print("----------------------------------------")
a=set()
for i in range(5):
    print("enter the value: ")
    data=int(input())
    a.add(data)
print(a)
a.update([60,70,80])
print(a)
print("enter the value to discard ")
d=int(input("enter removing element: "))
a.discard(d)
print(a)