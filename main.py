#Imports
import tkinter as t
from pygame import mixer
import os


dir = "C:/" #the songs directory
songs = os.listdir(dir) #we get all the archives in the directory and put them in a list
choose=0 #this will determinate which song from the list we will be playing

#starting the mixer
mixer.init() #starting the mixer
#mixer.music.load(dir+"/"+songs[choose]) #starting with the first song of the folder
mixer.music.set_volume(0.5) #setting volume
#mixer.music.play() #playing

#the callback from the buttons
#paused its the variable that determinate if the song is paused or not
paused = 0
def play_callback():
    global paused
    if paused == True:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True
    song_tittle()

#every time we hit the back button, we got choose-1, we stop playing the song, concatenate the directory + the song and play it. If the choose get out of the index range, then we start from the last song. The same principles applies for the skip_calback
def back_callback():
    global choose
    global songs
    try:
        choose -= 1
        mixer.music.stop()
        mixer.music.load(dir+"/"+songs[choose])
        mixer.music.play()
    except IndexError:
        choose = len(songs)
        mixer.music.stop()
        mixer.music.load(dir+"/"+songs[choose])
        mixer.music.play()
    song_tittle()

def skip_callback():
    global choose
    try:
        choose += 1
        mixer.music.stop()
        mixer.music.load(dir+"/"+songs[choose])
        mixer.music.play()
    except IndexError:
        choose = 0
        mixer.music.stop()
        mixer.music.load(dir+"/"+songs[choose])
        mixer.music.play()
    song_tittle()

def submit_callback():
    #getting the info from entry
    global dir
    global songs
    global choose
    choose=0
    info=direc.get()
    dir = info.replace("\\","/")
    songs = os.listdir(dir) #we get all the archives in the directory and put them in a list
    mixer.music.stop()
    mixer.music.load(dir+"/"+songs[choose]) #starting with the first song of the folder
    mixer.music.play() #playing
    song_tittle()

#the function that will create the GUI
def interface():
    #instancing the window
    window = t.Tk()
    #setting window name
    window.title("Vitonhos Music Player")

    #converting images from png to photoimage
    icon_background = t.PhotoImage(file="bg.png")
    play_button = t.PhotoImage(file="play.png")
    back_button = t.PhotoImage(file="back.png")
    skip_button = t.PhotoImage(file="skip.png")

    #setting the window icon
    window.iconphoto(True, icon_background)

    #setting the window size
    window.geometry("600x600")
    window.resizable(width=False, height=False)

    #setting the canvas
    my_canvas = t.Canvas(window, width=600, height=600)

    #setting the background image
    my_canvas.create_image(0,0, image=icon_background, anchor="nw")

    #setting the buttons
    play = t.Button(window, command=play_callback, image=play_button,border=False, bg = "#087a77", activebackground="#087a77")
    buttonplay_window = my_canvas.create_window(229,467, 
                                                anchor="nw", 
                                                window=play)

    back = t.Button(window, command=back_callback,image=back_button,border=False, bg = "#0a7075", activebackground="#0a7075")
    buttonback_window = my_canvas.create_window(110,469, 
                                                anchor="nw", 
                                                window=back)

    skip = t.Button(window, command=skip_callback,image=skip_button,border=False, bg = "#088e7b", activebackground="#088e7b")
    buttonskip_window = my_canvas.create_window(388,469, 
                                                anchor="nw", 
                                                window=skip)                                            

    submit = t.Button(window, command=submit_callback, text="Submit", bg="#087a77", fg="white", font=("Impact",10), activebackground="#087a77", activeforeground="white")
    buttonsubmit_window = my_canvas.create_window(550,20,
                                                 anchor="ne",
                                                 window=submit)

    global direc #here we gotta set direc as global to be able to get it info in the callback
    direc = t.Entry(window, width=75)
    direc_window = my_canvas.create_window(498,23,
                                            anchor="ne",
                                            window=direc)

    #setting the texts
    my_canvas.create_text(300,250, 
                        font=("Impact",40),
                        fill="white",
                        text="Song:")

    #setting the song tittle text function
    global song_tittle
    def song_tittle():
        global songs
        global choose
        my_canvas.delete("song_name")
        my_canvas.create_text(300,300, 
                            font=("Impact",20),
                            tag="song_name",
                            fill="white",
                            text="{}".format(songs[choose]))
    song_tittle()

    #initializing the labels and the window
    my_canvas.pack(fill='both',expand=True)
    window.mainloop()

#calling the interface function
interface()