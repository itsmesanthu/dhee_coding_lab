# def wordReversal(s):
#     s=s+" "
#     nsent=""
#     nword=""
#     for i in range(0,len(s)):
#         if s[i]!=" ":
#             nword=s[i]+nword
#         elif nword!="":
#             if nsent=="":
#                 nsent=nsent+nword
#             else:
#                 nsent=nsent+" "+nword
#             nword=""
#     return nsent
# s=input("enter a string :")
# print("original string :",s)
# re=wordReversal(s)
# print("the word is revesed in sent :",re)


# def sentReversal(s):
#     s=s+" "
#     nsent=""
#     nword=""
#     for i in range(0,len(s)):
#         if s[i]!=" ":
#             nword+=s[i]
#         elif nword!="":
#             if nsent=="":
#                 nsent=nword+nsent
#             else:
#                 nsent=nword+" "+nsent
#             nword=""
#     return nsent
# s=input("enter a string :")
# print("original string :",s)
# re=sentReversal(s)
# print("the  revesed in sent :",re)
def strfilter(s):
    n=""
    for i in range(0,len(s)):
        if "A"<=s[i]<="Z":
            n=n+chr(ord(s[i])+32)
        elif ("a"<=s[i]<="z") or ("0"<= s[i]<="9"):
            n=n+s[i]
        return n
def strpalindrom(s):
    s=strfilter(s)
    l,r=0,len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True   

s=input("enter a string :")
print("original string :",s)
f=strpalindrom(s)
if f:
    print("this string is palindrom")
else:
    print("this string is non palindrom")