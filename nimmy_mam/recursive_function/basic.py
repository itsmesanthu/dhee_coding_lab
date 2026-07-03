n=int(input("enter the number: "))
def fecat(n):
    if n<=1:
        return 1
    return n*fecat(n-1)
a=fecat(n)
print(a)
def fib(n):
    if n<=0:
        return n
    return n+fib(n-1)+fib(n-2)
fib(n)
def number(n):
    if n==0:
        return 
    print(n,end=" ")
    return number(n-1)
number(n)
print()
def number_rev(n):
    if n==0:
        return
    number_rev(n-1)
    print(n,end=" ")
number_rev(n)
print()
def count_digit(n):
    a=0
    if n==0:
        return 0
    a+=1
    return 1+count_digit(n//10)
m=int(input("enter the number :"))
print(count_digit(m))

def sum_of_digit(n):
    if n<=0:
        return n
    return (n%10)+sum_of_digit(n//10)
s=int(input("enter the number : "))
print(sum_of_digit(s))

def sum_of_first_n_number(n):
    if n==0:
        return 0
    return n+sum_of_first_n_number(n-1)
num=int(input("enter the n th number : "))
print(sum_of_first_n_number(num))
 
def even_number_of_n_number(n):
    if n==0:
        return 0
    if n%2==0:
        print(n,end=" ")
    return even_number_of_n_number(n-1)
s=int(input("enter the n th number : "))
print(even_number_of_n_number(s))


def odd_number_of_n_number(n):
    if n==1:
        return 1
    if n%2!=0:
        print(n,end=" ")
    return odd_number_of_n_number(n-1)
s=int(input("enter the n th number : "))
print(odd_number_of_n_number(s))

def product_of_n_number(n):
    if n==1:
        return 1
    return n*product_of_n_number(n-1)
p=int(input("enter the number : "))
print(product_of_n_number(p))


def trifibonic(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    return n+trifibonic(n-1)+trifibonic(n-2)+trifibonic(n-3)
f=int(input("enter the number  : "))
print(trifibonic(f))