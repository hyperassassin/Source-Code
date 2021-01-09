from tkinter import *
import random
import datetime
import qrcode
from PIL import Image,ImageDraw,ImageFont

def qr_code():
    img = Image.new('RGB',(1000,900),(255,255,255))
    draw = ImageDraw.Draw(img)
    
    (x,y) = (50,50)
    msg = t1.get()
    company = msg
    color = 'rgb(0,0,0)'
    font = ImageFont.truetype('arial.ttf',size = 60)
    draw.text((x,y),msg,fill = color,font = font)

    (x,y) = (600,75)
    idno = random.randint(10000000,90000000)
    msg = str("ID :- " + str(idno))
    color = 'rgb(0,0,0)'
    font = ImageFont.truetype('arial.ttf',size = 60)
    draw.text((x,y),msg,fill = color , font = font)

    (x,y) = (50,250)
    msg = t2.get()
    name = msg
    msg = str('Name : ' + str(msg))
    color = 'rgb(0,0,0)'
    font = ImageFont.truetype('arial.ttf',size = 45)
    draw.text((x,y),msg,fill = color , font = font)

    (x,y) = (50,350)
    msg = t3.get()
    msg = str('Gender : ' + str(msg))
    color = 'rgb(0,0,0)'
    draw.text((x,y),msg,fill = color , font = font)

    (x,y) = (400 , 350)
    msg = t4.get()
    msg = str('Age : ' + str(msg))
    color = 'rgb(0,0,0)'
    draw.text((x,y),msg,fill = color , font = font)

    (x,y) = (50 , 450)
    msg = t5.get()
    msg = str('Date Of Birth : ' + str(msg))
    color = 'rgb(0,0,0)'
    draw.text((x,y),msg,fill = color , font = font)

    (x,y) = (50 , 550)
    msg = t6.get()
    msg = str('Blood Group : ' + str(msg))
    color = 'rgb(255,0,0)'
    draw.text((x,y),msg,fill = color , font = font)

    (x,y) = (50 , 650)
    msg = t7.get()
    temp = msg
    msg = str('Mobile No : ' + str(msg))
    color = 'rgb(0,0,0)'
    draw.text((x,y),msg,fill = color , font = font)

    (x,y) = (50 , 750)
    msg = t8.get()
    msg = str('Address : ' + str(msg))
    color = 'rgb(0,0,0)'
    draw.text((x,y),msg,fill = color , font = font)

    img.save(str(name) + '.png')
    img = qrcode.make(str(company) + str(idno))
    img.save(str(idno) + '.bmp')

    til = Image.open(name + '.png')
    im = Image.open(str(idno) + '.bmp')
    til.paste(im , (650,350))
    til.save(name + '.png')

    print(('\n\n\n Your ID Card Successfully created in a PNG file ' + name + '.png'))

root = Tk()
root.title("ID Card Generator | Developed By Sagar")
root.geometry("400x450")
root.resizable(0,0)
root.configure(background = "salmon")

frame = LabelFrame(root , bg = "salmon")
frame.place(x = 0 , y = 80 , width = 400 , height = 300)

frame1 = LabelFrame(root , bg = "salmon")
frame1.place(x = 0 , y = 0 , width = 400 , height = 80)

title = Label(frame1 , text = "ID Card Generator | Developed by hyper_assassin" , font = ('arial',10,'bold') , bg = "salmon")
title.place(x = 35 , y = 20)

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y \t\t\t\t %I:%M:%S %p")

label = Label(frame1 , text = reg_format_date , bg = "salmon" , font = ('arial',9,"bold"))
label.place(x = 5 , y = 55)

l1 = Label(frame , text = "Company Name :- " , bg = "salmon")
l1.grid(row = 0 , column = 0 , ipadx = 7 , ipady = 7)

t1 = Entry(frame , relief = SUNKEN)
t1.grid(row = 0 , column = 1 , ipadx = 7 , ipady = 7)

l2 = Label(frame , text = "Full Name :- " , bg = "salmon")
l2.grid(row = 1 , column = 0 , ipadx = 7 , ipady = 7)

t2 = Entry(frame , relief = SUNKEN)
t2.grid(row = 1 , column = 1 , ipadx = 7 , ipady = 7)

l3 = Label(frame , text = "Gender :- " , bg = "salmon")
l3.grid(row = 2 , column = 0 , ipadx = 7 , ipady = 7)

t3 = Entry(frame , relief = SUNKEN)
t3.grid(row = 2 , column = 1 , ipadx = 7 , ipady = 7)

l4 = Label(frame , text = "Age :- " , bg = "salmon")
l4.grid(row = 3 , column = 0 , ipadx = 7 , ipady = 7)

t4 = Entry(frame , relief = SUNKEN)
t4.grid(row = 3 , column = 1 , ipadx = 7 , ipady = 7)

l5 = Label(frame , text = "Date of Birth :- " , bg = "salmon")
l5.grid(row = 4 , column = 0 , ipadx = 7 , ipady = 7)

t5 = Entry(frame , relief = SUNKEN)
t5.grid(row = 4 , column = 1 , ipadx = 7 , ipady = 7)

l6 = Label(frame , text = "Blood Group :- " , bg = "salmon")
l6.grid(row = 5 , column = 0 , ipadx = 7 , ipady = 7)

t6 = Entry(frame , relief = SUNKEN)
t6.grid(row = 5 , column = 1 , ipadx = 7 , ipady = 7)

l7 = Label(frame , text = "Mobile No :- " , bg = "salmon")
l7.grid(row = 6 , column = 0 , ipadx = 7 , ipady = 7)

t7 = Entry(frame , relief = SUNKEN)
t7.grid(row = 6 , column = 1 , ipadx = 7 , ipady = 7)

l8 = Label(frame , text = "Address :- " , bg = "salmon")
l8.grid(row = 7 , column = 0 , ipadx = 7 , ipady = 7)

t8 = Entry(frame , relief = SUNKEN)
t8.grid(row = 7 , column = 1 , ipadx = 7 , ipady = 7)

b1 = Button(root , text = "Generate ID Card" , command = qr_code , bg = "green")
b1.place(x = 130 , y = 400)
    
root.mainloop()
