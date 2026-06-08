def reves(s, i, j):
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
def rotate(s, k):
    s = list(s)         
    n = len(s)
    if k >= n:
        k = k % n
    reves(s, 0, k-1)        
    result = ""
    for ch in s:
        result = result + ch
    return result

s = "abcd"
k = 2
print("Original :", s)
print("Rotated  :", rotate(s, k))