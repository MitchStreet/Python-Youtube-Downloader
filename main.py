# YouTube downloader
# Designed and programmed by Mitchell Jay Street

# Import python modules
from tkinter import *
from tkinter import ttk as tk
from pytube import YouTube


# Receive YouTube link
def youtube_link():
    video_link = input("Enter the link: ")
    yt = YouTube(video_link)


# Make application window, TkInter
root = Tk()

# Window title
root.title("Youtube Downloader")

# Set window size
root.geometry("500x350")
root.resizable(False, False)

# Title text
title_text = tk.Label(root, text='Youtube Downloader', font=("Arial", 15))
title_text.place(relx=0.5, rely=0.05, anchor='center')  # Position

# Subtitle text
subtitle_text = tk.Label(root, text='Download any YouTube video to any format!', font=("Arial", 10))
subtitle_text.place(relx=0.5, rely=0.13, anchor='center')  # Position

# Link enter text
link_enter_text = tk.Label(root, text='Enter YouTube link below:', font=("Arial", 8))
link_enter_text.place(relx=0.5, rely=0.2, anchor='center')  # Position

# Enter YouTube link
enter_link = tk.Entry(root, width=50)
enter_link.place(relx=0.5, rely=0.26, anchor='center')  # Position

# Convert button
convert = tk.Button(root, text="Convert", command=youtube_link)
convert.place(relx=0.5, rely=0.35, anchor='center')  # Position

# Exit button
exit_program = tk.Button(root, text="Exit", command=root.destroy)
exit_program.place(relx=0.5, rely=0.95, anchor='center')

# Run GUI
root.mainloop()
