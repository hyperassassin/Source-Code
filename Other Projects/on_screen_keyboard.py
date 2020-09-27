from tkinter import *
import tkinter.scrolledtext as scrolledtext

root = Tk()
root.title("On Screen Keyboard")

def select(v):
    if v=="<-":
        txt = text.get(1.0,END)
        val = len(txt)
        text.delete(1.0,END)
        text.insert(1.0,txt[:val-2])
    elif v=="Space":
        text.insert(END," ")
    elif v=="Tab":
        text.insert(END,"    ")
    else:
        text.insert(END,v)

text = scrolledtext.ScrolledText(root , width=75 , height=4 , wrap=WORD , padx=10 , pady=10 , borderwidth=5 , relief=RIDGE)
text.grid(row = 1 , columnspan = 16)

btn = ['q','w','e','r','t','y','u','i','o','p','<-','7','8','9','-','a','s','d','f','g','h','j','k','l','[',']','4','5'
       ,'6','+','z','x','c','v','b','n','m',',','.','Tab','0','1','2','3','/','Space']
r = 2
col = 0

for b in btn:
    cmd = lambda x=b:select(x)
    if b != 'Space':
        Button(root , text=b , width=4 , bg = 'black' , fg = 'white' , relief = 'raised' , padx = 2 , pady = 4 , bd = 6 , command = cmd).grid(row = r , column = col)
    if b == "Space":
        Button(root , text=b , width=5 , bg = 'black' , fg = 'white' , relief = 'raised' , padx = 380 , pady = 4 , bd = 6 , command = cmd).grid(row = 6 , columnspan = 16)
    col += 1
    if col > 14 and r == 2:
        col = 0
        r += 1
    if col > 14 and r == 3:
        col = 0
        r += 1

root.mainloop()
