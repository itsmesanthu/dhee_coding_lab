'''def dispFactors(n):
    print(f"The factors of {n} are: ", end="")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
def countFactors(n):
    countFact, countCycles = 0, 0
    for i in range(1, n + 1):
        countCycles += 1
        if n % i == 0:
            countFact += 1
    return countFact, countCycles

n = int(input("Enter a number: "))
dispFactors(n)
print("\n=================================")
resFact, resCycles = countFactors(n)
print(f"The number of factors of {n} is: {resFact}")
'''
def dispFactors(n):
    print(f"The factors of {n} are: ")
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i, end=" ")
            if i != n // i:
                print((n // i), end=" ")
        i += 1
def countFactors(n):
    countFact, countCycles = 0, 0
    for i in range(1, n + 1):
        countCycles += 1
        if n % i == 0:
            countFact += 2
    return countFact, countCycles

n = int(input("Enter a num:"))
dispFactors(n)
resFact, resCycles = countFactors(n)
print(f"\nThe number of factors of {n} is: {resFact}")
print("=================================")
print(f"The number of cycles taken to count the factors is: {resCycles}")