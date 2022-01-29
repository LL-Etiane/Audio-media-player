from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer
from tkinter import ttk
import os

playlist=[]
mixer.init()
#funtion to ask open file
def open_file():
    global filename
    filename=filedialog.askopenfilename()
    add_musics(filename)

#funtion to add musics to list
def add_musics(f):
        f=os.path.basename(f)
        listbox.insert(0,f)
        playlist.insert(0,filename)

#function to delete musics from the list
def del_music():
    indexinlist = listbox.curselection()
    indexinlist = int(indexinlist[0])
    listbox.delete(indexinlist)
    playlist.pop(indexinlist)

#help function
def help_b():
    messagebox.showinfo("About Me","I am just a guy who love programing and learning each day. You can "
                                   "mail me on lukongleinyuyetiane@gmail.com")

#play music function
def play_music():
    global played
    if played:
        mixer.music.unpause()
        status["text"] = "Music Unpaused "
        played=FALSE
    else:
        try:
            indexinlist=listbox.curselection()
            indexinlist=int(indexinlist[0])
            playnow=playlist[indexinlist]
            mixer.music.load(playnow)
            mixer.music.play()
            status["text"] = "playing "+os.path.basename(playnow)
        except:
            pass
    
#stop music
def stop_music():
    mixer.music.stop()
    status["text"] = "music stopped"

#pause_music
played=FALSE
def pause_music():
    global played
    if not played:
        mixer.music.pause()
        status["text"]="music paused"
        played=TRUE

#rewind music
def rewind_music():
    try:
        mixer.music.load(filename)
        mixer.music.play()
        status["text"] = "Music Rewinded"
    except:
        pass


#set volume
def set_volume(val):
    volume=float(val)/100
    mixer.music.set_volume(volume)

#mute music
muted=FALSE
def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.5)
        scale.set(50)
        muted=FALSE
    else:
        mixer.music.set_volume(0.0)
        scale.set(0)
        mutebutton.configure(image=unmuteimage)
        muted=TRUE


def close_me():
    stop_music()
    root.destroy()

root=Tk()

#status bar
status=Label(root,text="Virus media Player", relief=SUNKEN, anchor=W, bg="#ac9f9f")
status.pack(side=BOTTOM, fill=X)

#creating the menu bars
MainMenu=Menu(root)
root.config(menu=MainMenu)

#file menu
file=Menu(MainMenu,tearoff=0)
MainMenu.add_cascade(label="File", menu=file)
file.add_command(label="Open", command=open_file)
file.add_command(label="Exit",command=root.destroy)

#help menu
help=Menu(MainMenu,tearoff=0)
MainMenu.add_cascade(label="Help", menu=help)
help.add_command(label="About", command=help_b)

#frame to contain the buttons
ContainFrame=Frame(root,height=100,bg="#261b1b")
ContainFrame.pack(fill=X)

#play button
playimage=PhotoImage(file="play.png")
playbutton=Button(ContainFrame,image=playimage, command=play_music)
playbutton.grid(row=0, column=0, padx=5)

#stop button
stopimage=PhotoImage(file="stop.png")
stopbutton=Button(ContainFrame,image=stopimage, command=stop_music)
stopbutton.grid(row=0, column=1, padx=5)

#pause button
pauseimage=PhotoImage(file="pause.png")
pausebutton=Button(ContainFrame,image=pauseimage, command=pause_music)
pausebutton.grid(row=0, column=2, padx=5)

#volume control
scale=Scale(ContainFrame, from_=0, to=100,orient=HORIZONTAL,bg="#605b5b", command=set_volume)
scale.set(50)
mixer.music.set_volume(0.5)
scale.grid(row=0,column=4, padx=20)

#rewind button
rewindimage=PhotoImage(file="rewind.png")
rewindbutton=Button(ContainFrame, image=rewindimage, command=rewind_music)
rewindbutton.grid(row=0, column=3, padx=5)

#mute button
unmuteimage=PhotoImage(file="mute.png")
muteimage=PhotoImage(file="unmute.png")
mutebutton=Button(ContainFrame, image=muteimage, command=mute_music)
mutebutton.grid(row=0,column=7,padx=10)

#list box
rightframe=Frame(root)
rightframe.pack(side=RIGHT)
listbox=Listbox(rightframe,bg="#b4b7a9")
listbox.pack()

#list add and delete buttons
add=Button(rightframe,text="Add",bg="#605b5b",command=open_file)
add.pack(side=LEFT,padx=5)
delete=Button(rightframe,text="Delete",bg="#605b5b",command=del_music)
delete.pack(side=LEFT)

root.protocol('WM_DELETE_WINDOW',close_me)
root.title("virus mp3 player")
root.mainloop()
