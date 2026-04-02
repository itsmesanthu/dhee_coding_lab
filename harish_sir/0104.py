'''#shallow copy
a=[10,20,30,40,50]
print(a)
a1=a
print(a1)
a[2]=60
print(a)
print(a1)
d=[10,20,30,40,50]
print(d)
a1=d
a2=d.copy()
del d[2]
print(d)
print(a1)
print(a2)
#arthemeatic opertion on list
a=[10,20,30]
b=[40,50,60]
print(a+b)
#print(a-b) substerction  not support to list
print(a*5)
# print(a/b) division also not supported for list
d=[11,22,33,44]
print(d)
print(11 in d)
print(34 in d)
print(22 not in d)
print(21 not in d)'''
# inbulit funtion in list
# all9()
# any()
# sorted()
a=[10,20,30,40,50]
print(len(a))
print(min(a))
print(max(a))
print(all(a))
b=[10,20,0,30,40,5,0]
print(all(b))
print(any(b))
c=[0,0,0,0,0,0]
print(all(c))
print(any(c))
d=[21,31,23,12,2,4,7,0,12,3,1]
print(sorted(d))
print(sorted(d,reverse=True))
a.insert(2,25)
print(a)
a.append(23)
a.append(256)
print(a)