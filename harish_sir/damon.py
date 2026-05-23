import threading
import time

def task():
    while True:
        print("Background running")
        time.sleep(1)
t=threading.Thread(target=task)
t.daemon=True
t.start()
print("Main thread exists")