# def sumStrNumber(s):
#   nstr,charDig,sumNum="",0,0
#   for i in range(0,len(s)):
#     if "0"<=s[i]<="9":
#       charDig=(charDig*10)+(ord(s[i])-48)
#     else:
#       if charDig!=0:
#         sumNum=sumNum+charDig
#         charDig=0
#       nstr=nstr+s[i]
#   if charDig!=0:
#     sumNum=sumNum+charDig
#     charDig=0
#   return (nstr+str(sumNum))
# s=input("enter a string : ")
# print("original string",s)
# res=sumStrNumber(s)
# print("sumed character digit :",res)

"""wap to reverse the entirenstring
    In a reversal logic if the cursor is traversing to LHS 
    then keep the output memory on RHS
     
    -
      """
# def strIncreRev(s):
#   nstr=""
#   for i in range(0,len(s)):
#     nstr=s[i]+nstr
#   return nstr
# str=input("Enter the string: ")
# res=strIncreRev(str)
# print(res)

# def strincreRev(s,nstr,i):
#     if i>=len(s):
#         return nstr
#     nstr=s[i]+nstr
#     i+=1
#     return strincreRev(s,nstr,i)

# str=input("enter the string: ")
# res=strincreRev(str,"",0)
# print(res)

# def strDecreRev(s,nstr,i):
#     if i<0:
#         return nstr
#     nstr=nstr+s[i]
#     i-=1
#     return strDecreRev(s,nstr,i)

# stri=input("enter the string: ")
# res=strDecreRev(stri,"",len(stri)-1)
# print(res)

"""
read method
1.read()
2.read(bytes)
3.readline()
4.readlines()
"""
# print("enter the filename: ")
# fname=input()
# fptr=open(fname,"r")
# data=fptr.read()
# print(data)


# print("enter the filename: ")
# fname=input()
# fptr=open(fname,"r")
# data2=fptr.read(10)
# print(data2)

# print("Enter the filename: ")
# fname=input()
# fptr=open(fname,"r")
# data3=fptr.readline()
# print(data3)

# print("Enter the filename: ")
# fname=input()
# fptr=open(fname,"r")
# data3=fptr.readlines()
# print(data3)

"""serialization/picking"""
# import pickle
# class student:
#     def __init__(self,name,age,height,addr):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.addr=addr

#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.height)
#         print(self.addr)
# s=student("rama",22.5,5.6,"bang")
# f=open("names.txt","wb")
# pickle.dump(s,f)
# print("Object is saved into text file")
# f.close()

#De-serialization/unpickling
# import pickle
# class student:
#   def __init__(self,name,age,height,addr):
#     self.name=name
#     self.age=age
#     self.height=height
#     self.addr=addr
#   def display(self):
#     print(self.name)
#     print(self.age)
#     print(self.height)
#     print(self.addr)
# f=open("names.txt","rb")
# s=pickle.load(f)
# s.display()
# print("object is retrived")
# f.close()