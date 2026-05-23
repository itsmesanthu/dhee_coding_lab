def perfect(n):
    i = 1
    total = 0
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != (n // i):
                total += (n // i)
        i += 1
    if total - n == n:
        return True
    return False
n = int(input("Enter a number: "))
flag = perfect(n)
if flag:
    print("This is a perfect number")
else:
    print("This is not a perfect number")

