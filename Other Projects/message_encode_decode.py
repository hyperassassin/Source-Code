from tkinter import *
import base64

root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Message - Encode and Decode")

l1 = Label(root , text = "ENCODE DECODE " , font = "arial 20 bold").pack()

text = StringVar()
key = StringVar()
mode = StringVar()
result = StringVar()

def encode(key,message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key,message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return("".join(dec))

def set_mode():
    if(mode.get() == 'e'):
        result.set(encode(key.get() , text.get()))
    elif(mode.get() == 'd'):
        result.set(decode(key.get() , text.get()))
    else:
        result.set(" Invaild Mode ")
        
def reset():
    text.set("")
    key.set("")
    mode.set("")
    result.set("")

l2 = Label(root , font = ("arial 12 bold") , text = "MESSAGE").place(x = 60 , y =60)
e1 = Entry(root , font = ("arial 10") , textvariable = text , bg = "ghost white").place(x = 290 , y = 60)

l3 = Label(root , font = ("arial 12 bold") , text = "KEY").place(x = 60 , y = 90)
e2 = Entry(root , font = ("arial 10") , textvariable = key , bg = "ghost white").place(x = 290 , y = 90)

l4 = Label(root , font = ("arial 12 bold") , text = "MODE(e - encode,d - decode)").place(x = 60 , y = 120)
e3 = Entry(root , font = ("arial 10") , textvariable = mode , bg = "ghost white")
e3.place(x = 290 , y = 120)

e4 = Entry(root , font = ("arial 10 bold") , textvariable = result , bg = "ghost white").place(x = 290 , y = 150)

b1 = Button(root , font = ("arial 10 bold") , text ="RESULT" , padx = 2 , bg = "LightGray" , command = set_mode).place(x = 60 , y = 150)
b2 = Button(root , font = ("arial 10 bold") , text ="RESET" , padx = 2 , width = 6 , bg = "LimeGreen" , command = reset).place(x = 80 , y = 190)
b3 = Button(root , font = ("arial 10 bold") , text ="EXIT" , padx = 2 , pady = 2 , width = 6 , bg = "OrangeRed" , command = exit).place(x = 180 , y = 190)

root.mainloop()
