'''n=int(input("enter the reverse"))
t=n
rev=0
if n<0:
    n=-n
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if t<0:
    rev=rev*-1
print(rev)'''
def reverse_num(n):
    t = n
    rev = 0
    if n < 0:
        n = -n
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10

    if t < 0:
        rev = rev * -1
    return rev
n=int(input("enter the number : "))
h=reverse_num(n)
print(h)
'''
if n==h:
    print("palindrome")
else:
    print("not ")'''