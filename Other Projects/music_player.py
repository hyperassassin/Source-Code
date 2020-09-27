from tkinter import *
import pygame
import os

class musicplayer:
    def __init__(self,root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        frame1 = LabelFrame(self.root , text ="Track Name", font =("times new roman",15,"bold") , bg = "grey" , fg = "white" , bd = 5 , relief = GROOVE)
        frame1.place(x=0,y=0,width=600,height=100)
        songtrack = Label(frame1 , textvariable = self.track , font =("times new roman",16,"bold") , bg = "grey" , fg = "red").grid(row = 0 , column = 0 , padx = 10 , pady = 5)
        trackstatus = Label(frame1 , textvariable = self.status , font =("times new roman",16,"bold") , bg = "grey" , fg = "gold").grid(row = 0 , column = 1 , padx = 10 , pady = 5)

        frame2 = LabelFrame(self.root,text = "Music Controls",font =("times new roman",15,"bold"),bg = "grey",fg = "white",bd = 5,relief = GROOVE)
        frame2.place(x=0,y=100,width=600,height=100)

        playbtn = Button(frame2,text = "START",command = self.playsong,width = 6,height = 1,font =("times new roman",16,"bold"),fg = "navyblue",bg = "gold").grid(row = 0 , column = 0 , padx = 10 , pady = 5)
        pausebtn = Button(frame2,text = "PAUSE",command = self.pausesong,width = 8,height = 1,font =("times new roman",16,"bold"),fg = "navyblue",bg = "gold").grid(row = 0 , column = 1 , padx = 10 , pady = 5)
        unbtn = Button(frame2,text = "PLAY",command = self.unpausesong,width = 6,height = 1,font =("times new roman",16,"bold"),fg = "navyblue",bg = "gold").grid(row = 0 , column = 2 , padx = 10 , pady = 5)
        stopbtn = Button(frame2,text = "STOP" ,command = self.stopsong,width = 6,height = 1,font =("times new roman",16,"bold"),fg = "navyblue",bg = "gold").grid(row = 0 , column = 3 , padx = 10 , pady = 5)

        frame3 = LabelFrame(self.root , text = "Song Playlist", font =("times new roman",15,"bold") , bg = "grey" , fg = "white" , bd = 5 , relief = GROOVE)
        frame3.place(x=600,y=0,width=400,height=200)

        scroll_y = Scrollbar(frame3 , orient = VERTICAL)
        self.playlist = Listbox(frame3 , yscrollcommand = scroll_y.set , selectbackground = "gold" , selectmode = SINGLE , font =("times new roman",12,"bold") , bg = "silver" , fg = "navyblue" , bd = 5 , relief = GROOVE)

        scroll_y.pack(side = RIGHT , fill = Y)
        scroll_y.config(command = self.playlist.yview)
        self.playlist.pack(fill = BOTH)

        os.chdir(r"C:\Users\Hp\Desktop\New folder")

        songtracks = os.listdir()

        for track in songtracks:
            self.playlist.insert(END,track)

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()
    def stopsong(self):
      self.status.set("-Stopped")
      pygame.mixer.music.stop()
    def pausesong(self):
      self.status.set("-Paused")
      pygame.mixer.music.pause()
    def unpausesong(self):
      self.status.set("-Playing")
      pygame.mixer.music.unpause()

root = Tk()
musicplayer(root)
root.mainloop()
        
