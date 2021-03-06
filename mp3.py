                        # SANJAY KUMAR MP3 PLAYER PROJECT IN PYTHON 
from tkinter import *
from tkinter import filedialog
import pygame
import os

root = Tk()
root.title('SK mp3 player')
root.iconbitmap('ic.ico')
root.geometry('550x430')
root.minsize(550,430)
root.maxsize(550,430)
root.configure(bg='cyan2')

# initialize pygame mixer
pygame.mixer.init()

# add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='songs/',title="Choose A Song",filetypes=(("mp3 files","*.mp3"),))
    # directory name and extension
    song=os.path.basename(song)
    song=song.replace('.mp3','')
    # adding one song
    song_box.insert(END, song)

# add all songs function
def add_songs():
    songs = filedialog.askopenfilenames(initialdir='songs/',title="Choose All Songs",filetypes=(("mp3 files","*.mp3"),)) 
    # directory name and extension
    # loop through song list and replace directory name and extension
    for song in songs:
        # insert into playlist
        song=os.path.basename(song)
        song=song.replace('.mp3','')
        song_box.insert(END,song)

# play button
def play():
    song=song_box.get(ACTIVE)
    song=f'C:/Users/sanju/OneDrive/Desktop/songs/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# stop function
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

# forward function
def forward():
    # get the current song tuple number
    next_song=song_box.curselection()
    # adding one to current song no.
    next_song=next_song[0]+1
    song=song_box.get(next_song)
    song=f'C:/Users/sanju/OneDrive/Desktop/songs/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    # moving active bar
    song_box.select_clear(0,END) 
    song_box.activate((next_song))
    song_box.selection_set(next_song,last=None)

# backward function
def backward():
    # get the current song tuple number
    prev_song=song_box.curselection()
    # substract one to current song no.
    prev_song=prev_song[0]-1
    song=song_box.get(prev_song)
    song=f'C:/Users/sanju/OneDrive/Desktop/songs/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # moving active bar
    song_box.select_clear(0,END) 
    song_box.activate((prev_song))
    song_box.selection_set(prev_song,last=None)

# delete a song 
def delete_song():
    # delete current selected song
    song_box.delete(ANCHOR)
    # stop music if playing
    pygame.mixer.music.stop()

# delete all songs 
def delete_songs():
    # delete all songs
    song_box.delete(0,END)
    # stop music if playing
    pygame.mixer.music.stop()

# creating Global pause variable
global paused
paused = True

# pause  and unpaused button
def pause(): 
    global paused
    if paused:
        # unpause
        pygame.mixer.music.pause()
        paused = False
    else:
         pygame.mixer.music.unpause()
         paused = True

# Label header title
head_label=Label(text="S K Music Player", bg="cyan4",fg="white",font=("Times", "21", "bold italic"),borderwidth=5, relief=SUNKEN)
head_label.pack(pady=10)

# create playlist Box
song_box= Listbox(root,bg="black",fg="yellow",width=80)
song_box.pack(pady=20)

# player control buttons images
play_img= PhotoImage(file='play.png')
pause_img=PhotoImage(file='pause.png')
backward_img=PhotoImage(file='back.png')
forward_img=PhotoImage(file='forward.png')
#stop_img=PhotoImage(file='stop.png')

# player control frame
control_frame=Frame(root,borderwidth=5,bg='cyan4', relief=SUNKEN)
control_frame.pack()

# player control buttons 
play=Button(control_frame,image=play_img,border=5,command=play)
pause=Button(control_frame,image=pause_img,border=5,command=pause)
backward=Button(control_frame,image=backward_img,border=5,command=backward)
forward=Button(control_frame,image=forward_img,border=5,command=forward)
#stop=Button(control_frame,image=stop_img,border=0,command=stop)

# position of buttons
backward.grid(row=0, column=1, padx=10)
play.grid(row=0, column=0, padx=10)
pause.grid(row=0, column=2, padx=10)
forward.grid(row=0, column=3, padx=10)
#stop.grid(row=0, column=4, padx=10)

# Label footer title
head_label=Label(text="SANJAY KUMAR (C) 2020",bg='goldenrod',fg='black',font=("Times", "12", "bold italic"),borderwidth=5)
head_label.pack(pady=22)

# create menu
my_menu=Menu(root)
root.config(menu=my_menu)

# create add sond menu
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label = "Add songs",menu = add_song_menu)
add_song_menu.add_command(label='Add One Song To Playlist', command = add_song)
# create add many songs menu
add_song_menu.add_command(label='Add Many Songs To Playlist', command = add_songs)

# delete song menu
remove_song_menu= Menu(my_menu)
my_menu.add_cascade(label='Remove Songs', menu=remove_song_menu)
remove_song_menu.add_command(label='Delete One Song From Playlist',command=delete_song)
remove_song_menu.add_command(label='Delete all Songs From Playlist',command=delete_songs)

root.mainloop()