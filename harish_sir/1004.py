#iterating the dictionary
emp={
    "id":101,
    "name":"santhu",
    "age":21,
    "addr":"beng"
}
print(emp)
print(len(emp))
print(emp["age"])
print("-----------------------")
for i in emp:
    print(i)
print("-----------------------")
for i in emp.keys():
    print(i)
print("-----------------------")
for i in emp:
    print(emp[i])
print("-----------------------")
for i in emp.values():
    print(i)
print("-----------------------")
for i in emp:
    print(i," ",emp[i])
print("-----------------------")
for i,j in emp.items():
    print(i," ",j)
print("-----------------------")
d={1:11,
   2:22,
   3:33,
   4:44
}
print(d)
d1=d
d[1]=111
print(d)
print(d1)
d2=d.copy()
d[1]=1111
print(d)
print(d1)
print(d2)
print("-----------------------")
student={
    "name":"santu",
    "age":21,
    "ph_number":{
        "mob1":1234,
        "mob2":4312
    },
    "addr":{
        "present":"mandy",
        "prem":"bengaluru"
    }
}
print(student)
print("-----------------------")
print(student["age"])
print(student["ph_number"]["mob1"])
print(student["addr"]["prem"])
print("-----------------------")
student["marks"]={
    1:70,2:85,3:97,4:100}
print("-----------------------")
print(student)
print("-----------------------")
s1=student
student["ph_number"]["mob1"]=34343
print(student["ph_number"]["mob1"])
print(s1["ph_number"]["mob1"])
print("-----------------------")
s2=student.copy()
student["addr"]["prem"]="hyd"
print(student["addr"]["prem"])
print(s1["addr"]["prem"])
print(s2["addr"]["prem"])
