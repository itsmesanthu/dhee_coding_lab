
from threading import Thread,Lock
lock=Lock()
import time
speed = 1
class AudioThread(Thread):
    def run(self):
        global speed
        for i in range(1, 8):
            with lock:
                print(f"Audio playing... speed = {speed}x")
                time.sleep(1/speed)
class VideoThread(Thread):
    def run(self):
        global speed
        for i in range(1, 8):
            with lock:
                print(f"Video playing... speed = {speed}x")
                time.sleep(1/speed)
class BufferThread(Thread):
    def run(self):
        while True:
            with lock:
                print("Buffering next content...")
                time.sleep(1)
audio = AudioThread()
video = VideoThread()
buffer = BufferThread()
buffer.daemon = True
audio.start(),video.start(),buffer.start()
time.sleep(6)
print("\nChanging speed to 2x...\n")
speed = 2
audio.join(),video.join()
print("Playback completed")