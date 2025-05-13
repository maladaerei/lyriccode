import time
from threading import Lock
import sys

lock = Lock()

def animate_text(text, delay=0.6):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, speed):
    animate_text(lyric, speed)

def sing_song(): 
    lyrics = [
        ("how can we go back to being friends", 0.06),
        ("when we just shared a bed?", 0.08),
        ("how can you look at me and pretend", 0.07),
        ("im someone you've never met ?", 0.08)
    ]

    for lyric, speed in lyrics:
        sing_lyric(lyric, speed)  

if __name__ == "__main__":
    sing_song()