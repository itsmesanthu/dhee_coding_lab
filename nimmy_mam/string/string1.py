def lowercase(s):
    n=""
    for i in range(0,len(s)):
        if "A"<= s[i]<="Z":
            n=n+chr(ord(s[i])+32)
        else:
            n=n+s[i]
    return n
def uppercase(s):
    n=""
    for i in range(0,len(s)):
        if "a"<=s[i]<="z":
            n=n+chr(ord(s[i])-32)
        else:
            n=n+s[i]
    return n
def swapcase(s):
    n=""
    for i in range(0,len(s)):
        if "a"<=s[i]<="z":
            n=n+chr(ord(s[i])-32)
        else:
            n=n+chr(ord(s[i])+32)
        
    return n
def chardigit(s):
    n=""
    sum=0
    for i in range(0,len(s)):
        if 48<=ord(s[i])<=57:
            sum=sum+(ord(s[i])-48)
        else:
            n=n+s[i]
    num=""
    while sum>0:
            rem=sum%10
            num=chr(rem+48)+num
            sum=sum//10
    #num=str(sum)
    return (n+num)
s=input("enter your string : ")
print("the original string is : ",s)
hi=lowercase(s)
print("lower case: ",hi)
h=uppercase(s)
print("upper case is:",h)
o=swapcase(s)
print("swap case :",o)
k=chardigit(s)
print("charatee digit sum :",k)
