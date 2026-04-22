# import time
# class vlc:
#     def apl_open(self):
#         print("VLC aplliction opened")
#         time.sleep(3)
#     def video_start(self):
#         print("video started playing")
#         time.sleep(3)
#     def audio_start(self):
#         print("audio started playing")
#         time.sleep(3)
#     def prag_bar(self):
#         print("progress bar is activated")
#         time.sleep(3)
#     def valume(self):
#         print("valume incresing")
#         time.sleep(3)
# v=vlc()
# v.apl_open()
# v.video_start()
# v.audio_start()
# v.prag_bar()
# v.valume()
# print("vlc aplliction closed")
'''import time
from threading import Thread

class apl_open(Thread):
        def run(self):
            print("VLC aplliction opened")
            time.sleep(3)
class video_start(Thread):
         def run(self):
            print("video started playing")
            time.sleep(3)
class audio_start(Thread):
         def run(self):
            print("audio started playing")
            time.sleep(3)
class prag_bar(Thread):
         def run(self):
            print("progress bar is activated")
            time.sleep(3)
class valume(Thread):
         def run(self):
            print("valume incresing")
            time.sleep(3)

v=apl_open()
v1=video_start()
v2=audio_start()
v3=prag_bar()
v4=valume()
v.start()
v1.start()
v2.start()
v3.start()
v4.start()
print("vlc aplliction closed")'''
'''import time
from threading import Thread
class print_name(Thread):
    def run(self):
        name=["rama","krishna","arjuna"]
        for i in name:
            print(i)
            time.sleep(3)
class print_num(Thread):
    def run(self):
         for i in range(10):
            print(i)
            time.sleep(3)
class sum(Thread):
    def run(self):
        a=10
        b=29
        c=a+b
        print("the sum is ",c)
        time.sleep(3)
p=print_name()
p1=print_num()
p2=sum()
p.start()
p1.start()
p2.start()
p.join()
p1.join()
p2.join()
print("program is ended")
'''
'''import time
from threading import Thread
class even(Thread):
    def run(self):
        for i in range(0,101):
            if i%2==0:
                print(i)
                time.sleep(2)
class odd(Thread):
    def run(self):
         for i in range(0,101):
            if i%2!=0:
                print(i)
                time.sleep(2)
e=even()
o=odd()
e.start()
o.start()
e.join()
o.join()'''
import time
from threading import Thread
class even(Thread):
    def run(self):
        for i in range(0,101,2):
                print(i)
                time.sleep(2)
class odd(Thread):
    def run(self):
         for i in range(1,101,2):
                print(i)
                time.sleep(2)
e=even()
o=odd()
e.start()
o.start()
e.join()
o.join()