def isintpalindrome(n,rev,temp):
    if n<=0:
        return rev==temp
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    return isintpalindrome(n,rev,temp)
num=int(input("enter s num: "))
flag=isintpalindrome(num,0,num)
if flag:
    print("int palindrome")
else:
    print("non int palindrome")