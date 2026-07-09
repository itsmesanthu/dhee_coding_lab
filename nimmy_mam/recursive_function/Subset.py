def subset(arr, ans, i):
    if i == len(arr):
        print(ans)
        return
    subset(arr, ans + [arr[i]], i + 1)
    subset(arr, ans, i + 1)

arr = [1, 2, 3]
subset(arr, [], 0)