import copy
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
s1=student
s2=copy.deepcopy(student)
student["addr"]["prem"]="hyd"
print(student["addr"]["prem"])
print(s1["addr"]["prem"])
print(s2["addr"]["prem"])
emp_id=[101,201,301,401]
emp_name=["tanu","anu","santhu","raki"]
emp_sal=[10000,30000,200,70000]
emp_addr=["mysore","banglore","chitradurga","kodagu"]
info=list(zip(emp_name,emp_sal,emp_addr))
info1=dict(zip(emp_id,info))
print(info)
print()
print(info1)


#file processing in python :
fname=input("enter the file name:")
fptr=open(fname,"w")
for i in range(5):
    data=input("enter the name:")
    fptr.write(data +"\n")
fptr.close()
print("5 name one written to text file")
# Program to store employee details into a text file

print("Enter the filename")
fname = input()      # example: emp.txt

# Open file in write mode
fobj = open(fname, "w")

# Loop to enter 5 employee records
for i in range(5):
    eid = input("Enter the eid: ")
    ename = input("Enter the ename: ")
    edest = input("Enter the designation: ")
    esal = input("Enter the salary: ")
    eaddr = input("Enter the address: ")

    # Write data to file separated by tabs
    fobj.write(eid + "\t" + ename + "\t" + edest + "\t" + esal + "\t" + eaddr + "\n")
fobj.close()

print("Employee details are stored in text file")