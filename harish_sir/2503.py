'''def fun1():
    print("enter the fun1")
    try:
        fun2()
    except Exception as e:
        print("the error in fun1")
    print("living fun1")

def fun2():
    print("enter the fun2")
    res=10/0
    print(res)
    print("living fun2")
print("program is started ")
fun1()
print("the program is end")'''
'''def fun1():
    print("enter the fun1")
    try:
        fun2()
    except Exception as e:
        print("the error in fun1")
    print("living fun1")

def fun2():
    print("enter the fun2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("error in fun2")
    print("living fun2")
print("program is started ")
fun1()
print("the program is end")


def fun1():
    print("enter the fun1")
    try:
        fun2()
    except Exception as e:
        print("the error in fun1")
    print("living fun1")

def fun2():
    print("enter the fun2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("error in fun2")
        raise e
    print("living fun2")
print("program is started ")
fun1()
print("the program is end")


a=int(input("enter a number : "))
b=int(input("enter b number : "))
try:
    res=a/b
    print(res)
except Exception as e:
    print("error in program")
else:
    print("narmally executed ")

print("progarm is ended")


try:
    a=int(input("enter a number : "))
    b=int(input("enter b number : "))
    res=a/b
    print(res)
except ValueError as e:
    print("it is a value error")
    print(e.__str__())
except ZeroDivisionError as e:
    print("it is a zero division error")
    print(e.__str__())
except Exception as e:
    print("error in program")
    print(e.__str__())

def fun1():
    print("enter the fun1")
    try:
        fun2()
    except Exception as e:
        print("the error in fun1")
        raise e
    print("living fun1")

def fun2():
    print("enter the fun2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("error in fun2")
        raise e
    print("living fun2")
print("program is started ")
try:
    fun1()
except Exception as e:
    print("error in main fun")
print("the program is end")'''


def fun1():
    print("enter the fun1")
    try:
        fun2()
    except Exception as e:
        print("the error in fun1")
        raise e
    finally:
        print("living fun1")

def fun2():
    print("enter the fun2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("error in fun2")
        raise e
    finally:
     print("living fun2")
print("program is started ")
try:
    fun1()
except Exception as e:
    print("error in main fun")
print("the program is end")