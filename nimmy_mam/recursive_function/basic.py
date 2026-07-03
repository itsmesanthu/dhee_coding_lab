# Factorial of a Number using Recursion
n = int(input("Enter a number to find its factorial: "))

def fecat(n):
    if n <= 1:
        return 1
    return n * fecat(n - 1)

print(fecat(n))


# Fibonacci-like Recursive Function (Custom Logic)
n = int(input("Enter the term for the Fibonacci-like function: "))

def fib(n):
    if n <= 0:
        return n
    return n + fib(n - 1) + fib(n - 2)

print(fib(n))


# Print Numbers from N to 1
n = int(input("Enter a number to print from N to 1: "))

def number(n):
    if n == 0:
        return
    print(n, end=" ")
    return number(n - 1)

number(n)
print()


# Print Numbers from 1 to N
n = int(input("Enter a number to print from 1 to N: "))

def number_rev(n):
    if n == 0:
        return
    number_rev(n - 1)
    print(n, end=" ")

number_rev(n)
print()


# Count Number of Digits using Recursion
m = int(input("Enter a number to count its digits: "))

def count_digit(n):
    a = 0
    if n == 0:
        return 0
    a += 1
    return 1 + count_digit(n // 10)

print(count_digit(m))


# Sum of Digits using Recursion
s = int(input("Enter a number to find the sum of its digits: "))

def sum_of_digit(n):
    if n <= 0:
        return n
    return (n % 10) + sum_of_digit(n // 10)

print(sum_of_digit(s))


# Sum of First N Natural Numbers
num = int(input("Enter N to find the sum of first N natural numbers: "))

def sum_of_first_n_number(n):
    if n == 0:
        return 0
    return n + sum_of_first_n_number(n - 1)

print(sum_of_first_n_number(num))


# Print Even Numbers from N to 1
s = int(input("Enter N to print even numbers from N to 1: "))

def even_number_of_n_number(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        print(n, end=" ")
    return even_number_of_n_number(n - 1)

even_number_of_n_number(s)
print()


# Print Odd Numbers from N to 1
s = int(input("Enter N to print odd numbers from N to 1: "))

def odd_number_of_n_number(n):
    if n == 1:
        return 1
    if n % 2 != 0:
        print(n, end=" ")
    return odd_number_of_n_number(n - 1)

odd_number_of_n_number(s)
print()


# Product of First N Natural Numbers (Factorial)
p = int(input("Enter N to find the product of first N natural numbers: "))

def product_of_n_number(n):
    if n == 1:
        return 1
    return n * product_of_n_number(n - 1)

print(product_of_n_number(p))


# Tribonacci-like Recursive Function (Custom Logic)
f = int(input("Enter the term for the Tribonacci-like function: "))

def trifibonic(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return n + trifibonic(n - 1) + trifibonic(n - 2) + trifibonic(n - 3)

print(trifibonic(f))
