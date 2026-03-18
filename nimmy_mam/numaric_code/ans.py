'''def counting(n):
    if n < 0:
        n = -n
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count
def isASN(n):
    temp = n
    if n < 0:
        n = -n
    power = counting(n)
    asn = 0
    while n > 0:
        base = n % 10
        asn = asn + (base ** power)
        n = n // 10
    if temp < 0:
        asn = -asn
    return temp == asn
n = int(input("Enter the number: "))
print("Digit count:", counting(n))
if isASN(n):
    print("It is an Armstrong (ASN) number")
else:
    print("It is NOT an Armstrong (ASN) number")'''

#wap to print all the ans<s present in user defined range of val's
'''def counting(n):
    if n < 0:
        n = -n
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def isASN(n):
    temp = n
    if n < 0:
        n = -n
    power = counting(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10
    return temp == total
start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
found =0
print("Armstrong numbers in the given range are:")
for i in range(start, end + 1):
    if not isASN(i):
        print(i, end=" ")
        found+=1
if found==0:
    print(0)'''
#wap to print all the non ans present in user defined range of val's
'''def counting(n):
    if n < 0:
        n = -n
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def isASN(n):
    temp = n
    if n < 0:
        n = -n
    power = counting(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10
    return temp == total
start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
found =0
print("Armstrong numbers in the given range are:")
for i in range(start, end + 1):
    if not isASN(i):
        print(i, end=" ")
        found+=1
if found==0:
    print(0)'''
#wap to  print first "n" ans
def counting(n):
    if n < 0:
        n = -n
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
def isASN(n):
    temp = n
    if n < 0:
        n = -n
    power = counting(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10
    return temp == total
n=int(input("enter the first n number :"))
count=0
num=0
print(f"the firdt {n} number od ans: ")
while count < n:
    if isASN(num):
        print(num, end=" ")
        count += 1
    num += 1
'''#wap to print first "n" non asn's
def counting(n):
    if n < 0:
        n = -n
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
def isASN(n):
    temp = n
    if n < 0:
        n = -n
    power = counting(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10
    return temp == total
n=int(input("enter the first n number :"))
count=0
num=0
re=isASN(n)
print(f"the firdt {n} number of non ans: ")'''
'''while count < n:
    if  not isASN(num):
        print(num, end=" ")
        count += 1
    num += 1'''
