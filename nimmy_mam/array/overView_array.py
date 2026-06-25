# -----------------------------------------
# 1. Create an empty list (dynamic array)
# -----------------------------------------
arr = []
print("Initial empty list length:", len(arr))  # 0

# -----------------------------------------
# 2. Append elements (add at end)
# -----------------------------------------
arr.append(10)        # add integer
arr.append("abc")     # add string
arr.append(23.6)      # add float

print("After appends:", arr)
print("Length:", len(arr))

# -----------------------------------------
# 3. Access last element
# -----------------------------------------
print("Last element:", arr[len(arr) - 1])
# better way: arr[-1]

# -----------------------------------------
# 4. Append another element
# -----------------------------------------
arr.append(100)
print("After adding 100:", arr)

# -----------------------------------------
# 5. Update element at index
# -----------------------------------------
arr[3] = 25   # replace 100 with 25
print("After update:", arr)

# -----------------------------------------
# 6. Insert at specific position
# -----------------------------------------
arr.insert(1, 455)  # insert 455 at index 1
print("After insert at index 1:", arr)

# -----------------------------------------
# 7. Insert at index greater than length
#    (Python automatically adds at end)
# -----------------------------------------
arr.insert(20, 200)
print("After insert at large index:", arr)

# -----------------------------------------
# 8. Nested list (list inside list)
# -----------------------------------------
l2 = [1, 2, 3]
l3 = [55, 65]

l2.append(l3)  # l3 becomes a single element inside l2
print("l2 after append(l3):", l2)
print("l3:", l3)

# -----------------------------------------
# 9. Modify nested list (reference concept)
# -----------------------------------------
l2[3][1] = 72  # changes l3 also
print("After modifying nested list:")
print("l2:", l2)
print("l3 (also changed):", l3)

# -----------------------------------------
# 10. Dynamic array using user input
# -----------------------------------------
arr2 = []
n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter number: "))
    arr2.append(value)

print("Final dynamic array:", arr2)