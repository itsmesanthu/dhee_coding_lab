#inbuilt methoda on set:
s1={1,2,3,4}
s2={3,4,5,6}
s3={5,6,7,8}
s31=s1.union(s2)
print(s31)
s4=s1.intersection(s2)
print(s4)
s5=s1.difference(s2)
print(s5)
s6=s2.difference(s1)
print(s6)
s7=s1.symmetric_difference(s2)
print(s7)
#isdisjoints
print("isdisjoints")
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s3))
print(s3.isdisjoint(s1))
#superset and subset
print("superset and subset")
a1={1,2,3,4,5}
a2={1,2}
print(a1.issuperset(a2))
print(a1.issubset(a2))
print(a2.issuperset(a1))
print(a2.issubset(a1))
#frozen set
b1=frozenset([10,20,30,40,50])
print(b1)
# b1.add(60)
# b1.discord(40)
#s1={10,20,[20,30],40,50}
#print(s1)
s2={10,20,(20,30),45}
print(s2)
s3={10,20,{30,40},50}
print(s3)