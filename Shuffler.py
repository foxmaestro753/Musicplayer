import pygame
import random
import os
import numpy as np
import soundfile as sf
from tkinter import Tk, filedialog
import tkinter as tk

os.environ['SDL_VIDEODRIVER'] = 'x11'

def choose_music_folder():
    Tk().withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

def get_music_files(folder_path):
    music_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".wav"):
            music_files.append(os.path.join(folder_path, file))
    return music_files

def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_song_index])
    pygame.mixer.music.play()

def shuffle_playlist():
    global playlist, shuffled_playlist, current_song_index
    shuffled_playlist = playlist.copy()
    np.random.shuffle(shuffled_playlist)
    current_song_index = 0
    pygame.mixer.music.load(shuffled_playlist[current_song_index])
    pygame.mixer.music.play()

def update_current_song_label():
    current_song_label.config(text=f"Current Song: {os.path.basename(playlist[current_song_index])}")

def play_pause():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        play_pause_button.config(text="Pause")
    else:
        pygame.mixer.music.pause()
        paused = True
        play_pause_button.config(text="Play")

def next_song():
    play_next_song()
    update_current_song_label()

def shuffle_songs():
    shuffle_playlist()
    update_current_song_label()

def quit_music_player():
    pygame.mixer.music.stop()
    window.quit()

# Initialize Pygame
pygame.init()

# Choose the music folder
music_folder = choose_music_folder()

# Get the music files from the chosen folder
playlist = get_music_files(music_folder)

# Shuffle the playlist initially
current_song_index = 0
shuffle_playlist()

# Create the GUI window
window = tk.Tk()
window.title("Song Playlist")
window.geometry("400x200")

# Current Song Label
current_song_label = tk.Label(window, text="Current Song: ")
current_song_label.pack()

# Play/Pause Button
paused = False
play_pause_button = tk.Button(window, text="Pause", command=play_pause)
play_pause_button.pack()

# Next Song Button
next_song_button = tk.Button(window, text="Next Song", command=next_song)
next_song_button.pack()

# Shuffle Button
shuffle_button = tk.Button(window, text="Shuffle", command=shuffle_songs)
shuffle_button.pack()

# Quit Button
quit_button = tk.Button(window, text="Quit", command=quit_music_player)
quit_button.pack()

# Update the initial current song label
update_current_song_label()

# Initialize mixer module
pygame.mixer.init()
pygame.mixer.music.load(playlist[current_song_index])
pygame.mixer.music.play()

# Run the GUI main loop
window.mainloop()

# Quit Pygame
pygame.quit()