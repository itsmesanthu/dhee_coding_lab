# a=[10,20,30,40,50]
# print(a)
# a.insert(2,25)
# print(a)
# a.append(43)
# a.append(643)
# a.append(123)
# # a.append(1,2,3,4)
# b=[1,2,3,4]
# a.extend(b)
# print(a)
# a.extend([120,234,200])
# print(a)
# a.remove(30)
# print(a)
# a.pop()
# print(a)
# a.pop()
# a.pop(3)
# print(a)
# # print(a.index(255))
# print(a.count(100))
# a.clear()
# print(a)
# del a
# # print(a)
# d=[10,20,30,40]
# print(d)
# for index,value in enumerate(d):
#     print(index,"- ",value)
# a=[10,20,30,40,[50]]
# print(a)
# a1=a
# b1=a.copy()
# a[4][0]=100
# print(a)
# print(a1)
# print(b1)
'''import copy
a=[10,20,30,40,[50]]
print(a)
a1=a
b1 = copy.deepcopy(a)
a[4][0]=100
print(a)
print(a1)
print(b1)'''
#list comprehension 
'''a=[11,22,13,14,15]
b=[data+1 for data in a]
print(a)
print(b)'''
a=[x*x for x in range(1,11) if x%2==0]
print(a)