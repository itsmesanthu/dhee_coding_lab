
# from threading import Thread,Lock
# lock=Lock()
# import time
# speed = 1
# class AudioThread(Thread):
#     def run(self):
#         global speed
#         for i in range(1, 8):
#             with lock:
#                 print(f"Audio playing... speed = {speed}x")
#                 time.sleep(1/speed)
# class VideoThread(Thread):
#     def run(self):
#         global speed
#         for i in range(1, 8):
#             with lock:
#                 print(f"Video playing... speed = {speed}x")
#                 time.sleep(1/speed)
# class BufferThread(Thread):
#     def run(self):
#         while True:
#             with lock:
#                 print("Buffering next content...")
#                 time.sleep(1)
# audio = AudioThread()
# video = VideoThread()
# buffer = BufferThread()
# buffer.daemon = True
# audio.start(),video.start(),buffer.start()
# time.sleep(6)
# print("\nChanging speed to 2x...\n")
# speed = 2
# audio.join(),video.join()
# print("Playback completed")

import math

n = 12
i = 1
conut=0
while i < math.sqrt(n):
    if n%i==0:
        conut+=2
        print(i)
        print(n//i)
    i+=1
print("count:",conut)

b=13
i = 2
while i < math.sqrt(b):
    if b%i==0:
        print("f")
    else:
        print("p")
    i+=1

a=int(input("enter the number: "))
if(math.sqrt(a)*math.sqrt(a))==a:
    print("add")
else:
    print("even")
n=[1,2,3,4,5]
res=[]
for i in range(len(n)):
    if(math.sqrt(n[i])*math.sqrt(n[i])==n[i]):
        res.append("Open")
    else:
        res.append("close")
print(res)
nums=[2,3,5,4,5,2,4]
n=0
for i  in range(len(nums)):
    n=n^nums[i]
print(n)

a=[1,2,13,4,5,6]
k=4
maxsum=0
for i in range(0,len(a)-k+1):
    sum=0
    j=0
    while j<k:
        sum=sum+a[i+j]
        j+=1
    maxsum=max(maxsum,sum)
print(maxsum)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr=[1,2,13,4,5,6]
res=bubble_sort(arr)
print(res)

def insertion(arr):
    n=len(arr)
    for i in range(0,(n-1)):
        for j in range(i+1,0,-1):
            if arr[i]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[i]
            else:
                break
arr=[1,2,13,4,5,6]
res=insertion(arr)
print(res)
#sum of subarray

# arr = [1, 2, 3]
# sum=0
# n=len(arr)
# for i in range(n):
#     l=i+1
#     r=n-i
#     sum+=(l*r*arr[i])
# print(sum)


# water
ans=0
i,j=0,len(arr)-1
while i<j:
    h=min(arr[i],arr[j])
    w=j-i
    ans=max(ans,h*w)
    if arr[i]<arr[j]:
        i+=1
    else:
        j-=1
print(ans)