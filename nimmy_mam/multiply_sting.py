def multiply( num1, num2):
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 = n1 * 10 + (ord(num1[i]) - 48)
        for i in range(len(num2)):
            n2 = n2 * 10 + (ord(num2[i]) - 48)
        return str(n1 * n2)
num1=str(input("enter the number 1 :"))
num2=str(input("enter the number 2: "))
print(type(num1))
print(type(num2))
res=multiply(num1,num2)
print(res)