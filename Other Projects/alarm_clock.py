from tkinter import *
from tkinter import messagebox
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        #print("The Set Date is:",date) #Current Date  
        #print(now)  #Current Time
        if now == set_alarm_timer:
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            messagebox.showinfo("Wake" , "Wake Up !!!!!")
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

root = Tk()
root.title(" Alarm Clock ")
root.geometry("400x200")
root.configure(background = "Salmon")
root.resizable(0,0)

time_format=Label(root, text= "Note :- Enter time in 24 hour format !!!", fg="red",bg="black",font="Arial").place(x=40,y=140)
addTime = Label(root,text = "Hour   Min       Sec",font=60 , bg = "Salmon").place(x = 150)
setYourAlarm = Label(root,text = "When to wake you up",fg="blue",bg="Salmon",relief = "solid",font=("Helevetica",10,"bold")).place(x=0, y=29)

hour = StringVar()
min1 = StringVar()
sec = StringVar()

hourTime= Entry(root,textvariable = hour,bg = "pink",width = 15).place(x=150,y=30)
minTime= Entry(root,textvariable = min1,bg = "pink",width = 15).place(x=190,y=30)
secTime = Entry(root,textvariable = sec,bg = "pink",width = 15).place(x=240,y=30)

submit = Button(root,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =60,y=90)
exit1 = Button(root , text = " Stop" ,fg="red",width = 10,command = exit).place(x=160,y=90)

root.mainloop()
