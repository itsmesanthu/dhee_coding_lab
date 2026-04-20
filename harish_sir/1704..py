'''
read() methods:
1. read()
2. read(bytes)
3. readline()
4. readlines()
'''
# file=input("enter the file name :")
# file=open(file,"r")
# # data=file.read()
# # print(data)
# data1=file.readlines()
# print(data1)
'''import csv
print("Enter the filename")
fname=input()
fptr=open(fname,"w",newline="")
w=csv.writer(fptr)
w.writerow(["EID","ENAME","EDES","ESAL","EADDR"])
for i in range(5):
    eid=input("enter the eid: ")
    ename=input("enter the ename: ")
    edes=input("enter the edes: ")
    esal=input("enter the esal: ")
    eaddr=input("enter the eaddr: ")
    w.writerow([eid,ename,edes,esal,eaddr])
fptr.close()
print("5 employee details are stored in the csv file")'''
import csv
print("enter the file name :")
fname=input()
file=open(fname,"r")
data=csv.reader(file)
for i in data:
    print(i)
