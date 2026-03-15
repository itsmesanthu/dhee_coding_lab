"""def outer():
    print("enter hi")
    def inner():
        print("hello")
    return inner
o=outer()
print(o)
o()
# call inner function outside the function it called as closures in python"""
#decorater in python
'''def print_msg():
    print("Hello Everyone")

def outer(print1):
    print("Entering outer")
    def inner():
        print("Entering inner")
        ref = print1
        ref()
        print("leaving inner")
    print("calling inner")
    return inner
ptr1 = print_msg
ptr2 = outer(ptr1)
ptr2()
print("pgm end")'''
#wap to convert the string into an upper case by using decorater in python
def print_msg():
    msg = "python course"
    return msg

def outer(print1):
    print("Inside outer")
    def inner():
        print("Inside inner")
        ref = print1
        res = ref()
        res1 = res.upper()
        print(res1)
        print("leaving inner")
    return inner

ptr1 = outer(print_msg)   # pass function reference
ptr1()
print("pgm end")