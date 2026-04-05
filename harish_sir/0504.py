# t=(10,20,30,4)
# print(t)
# print(type(t))
# b=(10)
# print(b)
# print(type(b))
# b1=(10,)
# print(b1)
# print(type(b1))
'''t=(10,20,30,40,50,60,70,80,90)
print(t)
print(len(t))
print(t[4])
print(t[5])
print(t[0:3])
print(t[5:7])
print(t[7:])
print(t[:])
print(t[::-1])
print(t[6:2:-1])
print(t[:-3:-1])
print(t[-7:-2])
print(t[-5::2])
print(t[-4:-9])
print(t[:5:-1])
#print(t[-6:-2:0])'''
# insertion and deletion in tuple
t=(10,20,30,40,50,60,70,80,90)
print(t)
t1=t[0:2]+(25,)+t[2:]
print(t1)
t2=t[0:2]+t[5:]
print(t2)
#
names=["kahli","dhoni","iyer","hp"]
jnum=[18,7,96,33]
runs=[8500,5000,3000,6000]
team=["RCB","CSK","PKB","MI"]
res=list(zip(names,jnum,runs,team))
print(res)
from itertools import zip_longest
names=["kahli","dhoni","iyer","hp"]
jnum=[18,7,96,33]
runs=[8500,5000,3000,6000]
team=["RCB","CSK"]
res=list(zip_longest(names,jnum,runs,team))
print(res)