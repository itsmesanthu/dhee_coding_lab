#anagram
def strfilter(s):
        n=""
        for i in range(len(s)):
            if "A"<=s[i]<="Z":
                n=n+chr(ord(s[i])+32)
            elif "a"<=s[i]<="z":
                n=n+s[i]
        return n
def anagram(s1,s2):
     s1=strfilter(s1)
     s2=strfilter(s2)
     dict={}
     if len(s1)!=len(s2):
          return False
     else:
          for i in s1:
            if i in dict:
                 dict[i]+=1
            else:
                  dict[i]=1
          for i in s2:
            if i in dict:
                      dict[i]-=1
            else:
                  dict[i]=-1
          for i in dict:
                 if dict[i]!=0:
                      return False
          return True
s1=input("enter the string 1 :")
s2=input("enter the string 2 :")
f=anagram(s1,s2)
if f :
     print("anagram")
else:
     print("non anagram")