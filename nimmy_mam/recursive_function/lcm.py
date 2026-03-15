'''def findlcm(n1,n2,lcm):
    if lcm>(n1*n2):
        return
    if lcm%n1==0 and lcm%n2==0:
        return lcm
    return findlcm(n1, n2, (lcm + 1))
def palindrome(num):
    temp = num
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    if num == rev:
        return True
    else:
        return False
num1=int(input("enter then number : "))
num2=int(input("enter the number : "))
o=findlcm(num1,num2,1)
print("LCM is:", o)
if palindrome(o):
    print("LCM is a Palindrome number")
else:
    print("LCM is NOT a Palindrome number")'''
# wap print all digit the given  number
#num=334
def digit(n,h):
    if n == 0:
        return h
    d=n%10
    h=h+d
    return digit(n//10,h)
num = int(input("Enter the number: "))
re=digit(num,0)
print(re)
