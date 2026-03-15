'''#finding a substring in the many string
str="Id you think you con or you con't you are right"
print(str.count("you"))
str1="you"
print(str1 in str)
print(str.find("you"))
print(str.index("you"))
print(str.rfind("you"))
print(str.rindex("you"))
print(str.find("hio"))
#print((str.index("hio")))
str2=input("enter the word: ")
str2=str2.lower()
print(str2)
str2=str2.upper()
print(str2)
str2=str2.swapcase()
print(str2)

#globle string interning(globle inter tool)
a=10
b=20
c=10
d=30
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(a is b)
print(b is c)
print(c is d)
print(a is c)
'''

str=chr(input("enter the string 1 : "))
str1=chr(input("enter the string 2 : "))
if str>str1:
    print("string 1 is greater then string 2")
elif str1>str:
    print("string 2 is greater then string 1")
else:
    print("both string is equal")
print(count(str1))
#removeing the spasce ot the ending and bign end
s=" python is a language"
print(s)
s1=s.lstrip()
print(s1)
s2=s.rstrip()
print(s2)
s3=s.strip()
print(s3)
# removing all spaces in string
s=input("enter the string : ")
i=0
new=""
while i<=len(s)-1:
    d=s[i]
    if(d==" "):
        i=i+1
    else:
        new=new+d
        i=i+1
print(new)
#chacking the string . it's char or num or both type
s="python language"
print(s)
print(len(s))
s1=s.split()
print(s1)
print(len(s1))
h=input("enter the string :")
if h.isalpha():
    print("string contain only char")
if h.isdigit():
    print(" string contain only num")
if h.isalnum():
    print("string contain both")'''
#string formatting
name=input(" enter the name : ")
age=int(input("enter the age : "))
adders=input("enter the student adders : ")
quali=input("enter the qualification : ")
print("the student name is : {} .\n student  age is :{} \n student adders is : {} \n student qualification : {}". format(name,age,adders,quali))
print("the student name is : {3} .\n student  age is :{2} \n student adders is : {1} \n student qualification : {0}". format(name,age,adders,quali))
