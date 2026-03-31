'''def creatarray():
    print("Enter the elements into the array to be created:")
    l1 = []
    while True:
        try:
            n = int(input("Enter an element: "))
            l1.append(n)
        except Exception as e:
            return l1
def findMax(arr):
    maxele, maxeleid = -2**31, -1
    secmaxele, secmaxeleid = -2**32, -1
    for i in range(0, len(arr)):
        if arr[i] > maxele:
            secmaxele, secmaxeleid = maxele, maxeleid
            maxele, maxeleid = arr[i], i
        elif arr[i] != maxele and arr[i] > secmaxele:
            secmaxele, secmaxeleid = arr[i], i
    return [maxele, maxeleid, secmaxele, secmaxeleid]
arr = creatarray()
max1 = findMax(arr)
print("The array is:", arr)
print("Max element:", max1[0], "at index", max1[1])
print("Second max:", max1[2], "at index", max1[3])'''

'''def creatarray():
    print("Enter the elements into the array to be created:")
    l1 = []
    while True:
        try:
            n = int(input("Enter an element: "))
            l1.append(n)
        except Exception as e:
            return l1
def findMin(arr):
    minele, mineleid = 2**31, -1
    secminele, secmineleid = 2**32, -1
    for i in range(0, len(arr)):
        if arr[i] < minele:
            secminele, secmineleid = minele, mineleid
            minele, mineleid = arr[i], i
        elif arr[i] != minele and arr[i] < secminele:
            secminele, secmineleid = arr[i], i
    return [minele, mineleid, secminele, secmineleid]
arr = creatarray()
min1 = findMin(arr)
print("The array is:", arr)
print("Min element:", min1[0], "at index", min1[1])
print("Second min:", min1[2], "at index:", min1[3])'''
def creatarray():
    print("Enter the elements into the array to be created:")
    l1 = []
    while True:
        try:
            n = int(input("Enter an element: "))
            l1.append(n)
        except Exception as e:
            return l1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr=creatarray()
res=bubble_sort(arr)
print(res)