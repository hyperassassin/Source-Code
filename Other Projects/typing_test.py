from tkinter import *
from timeit import default_timer as timer
import random

window = Tk()
window.geometry("450x200")
window.title("Typing Test")
window.resizable(0,0)
window.configure(background="Salmon")

x = 0

def game():
    global x
    if x == 0:
        window.destroy()
        x =x+1
    def check_result():
        if(entry.get() == words[word]):
            end = timer()
            l4.config(text = end-start)
        else:
            print("Wrong Spelling")

    words = ["programming","coding","software","system","hardware","algorithm"]
    word = random.randint(0,(len(words)-1))
    start = timer()

    root = Tk()
    root.geometry("450x200")
    root.title("Main")
    root.resizable(0,0)
    root.configure(background="Salmon")

    l1 = Label(root , text = words[word] , font ="times 20" , bg = "Salmon")
    l1.place(x=120,y=10)

    l2 = Label(root , text = " Type The Word :- " , font = "times 14" , bg = "Salmon")
    l2.place(x=10 , y=55)

    l3 = Label(root , text = " Word Time :- " , font = "times 14" , bg = "Salmon")
    l3.place(x=10 , y=100)

    l4 = Label(root , text = "" , font = "times 14" , bg = "Salmon")
    l4.place(x=140 , y=100)

    entry = Entry(root , font = "times 14")
    entry.place(x=200 , y=55)

    b2 =Button(root , text = "Done" , command = check_result , width = 10 , bg = "grey")
    b2.place(x=50 , y=150)

    b3 = Button(root , text = "Try Again" , command = game , width = 10 , bg = "grey")
    b3.place(x=150 , y=150)

    close = Button(root , text = " Exit " , command = exit , width = 10 , bg = "grey")
    close.place(x=250 , y=150)

    root.mainloop()

x1 = Label(window , text = " Lets Go Start The Test.... " , font = "times 20" , bg = "Salmon")
x1.place(x=10 , y=50)

b1 = Button(window , text = " Start " , command = game , width = 12 , bg = "grey")
b1.place(x=150 , y=100)

window.mainloop()
