import tkinter as tk
import pygame
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.mixer.init()

music_file = 'multo.mp3'

lyrics = [
    "Di mo ba ako lilisanin?",
    "Hindi pa ba sapat pagpapahirap sa 'kin?",
    "Hindi na ba ma-mamamayapa?",
    "'Di na ba ma-mamayapa?"
]

music_duration = 18

display_duration = music_duration / len(lyrics)

def play_music():
    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        display_lyrics()
    except pygame.error as e:
        print(f"Terjadi kesalahan saat memuat atau memutar musik: {e}")

def display_lyrics():
    for line in lyrics:
        lyric_label.config(text=line)
        root.update()
        time.sleep(display_duration)
    lyric_label.config(text="")

root = tk.Tk()
root.title("Pemutar Musik")
root.geometry("400x300")

lyric_label = tk.Label(root, text="", font=("Arial", 16), justify="center")
lyric_label.pack(expand=True)

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

root.mainloop()
