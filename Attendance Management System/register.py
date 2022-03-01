from tkinter import *
from PIL import Image,ImageTk
from tkcalendar import *
from dateutil.parser import parse
from tkinter.tix import *
from tkinter import messagebox
import re
import pymysql
import random
import time
#Only Values Clear Remaining

#- - - - - - - - - - - - - - - - - - - -Root Window 
root = Tk()
root.title("Registeration Window")
#root.attributes('-fullscreen',True)  #For Fullscreen
#w = root.winfo_screenwidth()
#h = root.winfo_screenheight()
root.geometry("1280x860+0+0")
root.resizable(0,0)
root.config(bg = "white")
tip = Balloon(root)

#- - - - - - - - - - - - - - - - - - - -Functions
def clock_time():
    curr_time = time.strftime("%H:%M:%S")
    clock.config(text ="[" + curr_time + "]")
    clock.after(200,clock_time)

def date_today():
    curr_date = time.strftime("%d-%m-%Y")
    date_lbl.config(text = "[" + curr_date + "]")

def login():
    root.destroy()
    import login

def show_cal():
    global cal_window
    cal_window = Toplevel()
    cal_window.title("Select Your Birth Date")
    width = 250
    height = 230
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    cal_window.resizable(0, 0)
    cal_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
    cal_frame = Frame(cal_window)
    cal_frame.pack()
    cal = Calendar(cal_frame , selectmode = "day" , year = 2021 , month = 1 , day = 26)
    cal.pack()
    def check():
        a = cal.get_date()
        date_obj = parse(a)
        b = date_obj.date()
        if txt_dob.get() == "":
            txt_dob.insert(0,str(b))
        else:
            txt_dob.delete(0,END)
            txt_dob.insert(0,str(b))
    ok = Button(cal_frame , text = "Ok" , command = check) 
    ok.pack(pady = 10)

def main_function():
    #- - - - - - - - - - - - For Name
    regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',re.IGNORECASE)
    name = txt_name.get()
    res = regex_name.search(name)

    #- - - - - - - - - - - - Email Id
    regex_email = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
    mail = txt_email.get()
    res_email = regex_email.search(mail)

    #- - - - - - - - - - - - Contact No
    regex_phone = re.compile("^[7-9]\d{9}$")
    phone = txt_contact.get()
    res_phone = regex_phone.match(phone)

    #- - - - - - - - - - - - Username
    regex_user = re.compile("^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$")
    user_name = txt_user.get()
    res_user = regex_user.match(user_name)

    #- - - - - - - - - - - - Password
    regex_pass = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
    pass_word = txt_pass.get()
    res_pass = regex_pass.search(pass_word)

    #- - - - - - - - - - - - Address
    regex_add = re.compile('[@_!#$%^&*()<>?\|}{~:]')
    add_ress = txt_address.get()
    res_add = regex_add.search(add_ress)

    #- - - - - - - - - - - - Id
    idno = random.randint(10000000,90000000)
    id_no = str(idno)

    #- - - - - - - - - - - - Gender
    do = txt_dob.get()

    if(txt_name.get() == "" or txt_email.get() == "" or txt_address.get() == "" or txt_contact.get() == "" or txt_dob.get() == "" or txt_user.get() == "" or txt_pass.get() == ""):
        messagebox.showerror("Error","Fill all the Fields")
    elif(res == None):
        messagebox.showerror("Error","Invalid Name")
    elif(res_email == None):
        messagebox.showerror("Error","Invalid Email")
    elif(res_phone == None):
        messagebox.showerror("Error","Invalid Phone No")
    elif(res_user == None):
        messagebox.showerror("Error","Invalid Username")
    elif(res_pass == None):
        messagebox.showerror("Error","Invalid Password")
    elif(var.get()== 0):
        messagebox.showerror("Error","Please Select Your Gender !!")
    elif(res_add != None):
        messagebox.showerror("Error","Invalid Address Format")
    elif(var1.get() == 0):
        if var.get() == 1:
            a = "Male"
        elif var.get() == 2:
            a = "Female"
        elif var.get() == 3:
            a = "Others"
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id_no,name,mail,add_ress,a,phone,user_name,pass_word,do))
            con.commit()
            con.close()
            messagebox.showinfo("Success" , "You Have Registered Successfully !!!")
            txt_name.delete(0,END)
            txt_email.delete(0,END)
            txt_address.delete(0,END)
            txt_contact.delete(0,END)
            txt_dob.delete(0,END)
            txt_user.delete(0,END)
            txt_pass.delete(0,END)
        except Exception as e:
            messagebox.showerror("Error :- ",e)
    elif(var1.get() == 1):
        if var.get() == 1:
            a = "Male"
        elif var.get() == 2:
            a = "Female"
        elif var.get() == 3:
            a = "Others"
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("insert into admin values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id_no,name,mail,add_ress,a,phone,user_name,pass_word,do))
            con.commit()
            con.close()
            messagebox.showinfo("Success" , "You Have Registered Successfully !!!")
            txt_name.delete(0,END)
            txt_email.delete(0,END)
            txt_address.delete(0,END)
            txt_contact.delete(0,END)
            txt_dob.delete(0,END)
            txt_user.delete(0,END)
            txt_pass.delete(0,END)
        except Exception as e:
            messagebox.showerror("Error" , "Error :- ",e)
#- - - - - - - - - - - - - - - - - - - - -Images
#lbl_frame1 = LabelFrame(root , bg = "white" , bd = 0)
#lbl_frame1.place(x=200 , y=0 , relwidth=1 , height=60)

bg = ImageTk.PhotoImage(file="images/back.jpg")
back = Label(root , image = bg).place(x = 250 , y = 60 , relwidth = 1 , relheight = 1)

pic_attend = Label(root , bg = "white")
pic_attend.place(x=0,y=0,width=200,height=60)

##img_at = Image.open("attend.png")
im_at = ImageTk.PhotoImage(file="attend.png")
pic_attend.config(image = im_at)
pic_attend.image = im_at

head = Label(root , text = "    Attendance Management System" , font = ("times new roman",28,"bold") , bg = "white" , fg = "black").place(x=200 , y=7)

clock = Label(root , font = ("times new roman",15) , bg = "white" , fg = "black")
clock.place(x= 920 , y=25) 
clock_time()

date_lbl = Label(root , font = ("times new roman",15) , bg = "white" , fg = "black")
date_lbl.place(x=1010 , y=25)
date_today()

side = ImageTk.PhotoImage(file="images/side.png")
side1 = Label(root , image = side).place(x = 80 , y = 130 , width = 374 , height = 460)

#- - - - - - - - - - - - - - - - - - - - -Frame 1
frame1 = Frame(root , bg = "white")
frame1.place(x = 450 , y = 130 , width = 700 , height = 460)

#- - - - - - - - - - - - - - - - - - - - -Frame Components
title = Label(frame1 , text = "REGISTER HERE" , font = ("times new roman",20,"bold") , bg = "white" , fg = "green").place(x = 50 , y = 30)

name = Label(frame1 , text = "Full Name" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x = 50 , y = 100)
txt_name = Entry(frame1 , font = ("times new roman",15) , bg = "lightgray")
txt_name.place(x = 50 , y = 130 , width = 250)

email = Label(frame1 , text = "Email Id" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x = 370 , y = 100)
txt_email = Entry(frame1 , font = ("times new roman",15) , bg = "lightgray")
txt_email.place(x = 370 , y = 130 , width = 250)

address = Label(frame1 , text = "Address" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x = 50 , y = 170)
txt_address = Entry(frame1 , font = ("times new roman",15) , bg = "lightgray")
txt_address.place(x = 50 , y = 200 , width = 250)

var = IntVar()
gender = Label(frame1 , text = "Gender" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x = 370 , y = 170)
gen_male = Radiobutton(frame1 , text = "Male" , variable = var , value = 1 , bg = "white" , font  = ("times new roman",12)).place(x = 370 , y = 200)
gen_female = Radiobutton(frame1 , text = "Female" , variable = var , value = 2 , bg = "white" , font  = ("times new roman",12)).place(x = 440 , y = 200)
gen_others = Radiobutton(frame1 , text = "Others" , variable = var , value = 3 , bg = "white" , font  = ("times new roman",12)).place(x = 520 , y = 200)

contact = Label(frame1 , text = "Contact" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x = 50 , y = 240)
txt_contact = Entry(frame1 , font = ("times new roman",15) , bg = "lightgray")
txt_contact.place(x = 50 , y = 270 , width = 250)

dob = Label(frame1 , text = "Date of Birth" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x = 370 , y = 240)
txt_dob = Entry(frame1 , font = ("times new roman",15) , bg = "lightgray")
txt_dob.place(x = 370 , y = 270 , width = 250)

username = Label(frame1 , text = "Username" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x = 50 , y = 310)
txt_user = Entry(frame1 , font = ("times new roman",15) , bg = "lightgray")
txt_user.place(x = 50 , y = 340 , width = 250)
tip.bind_widget(txt_user , balloonmsg = "Username should be 8-20 characters long \n No _ or . at the beginning \n No __ or _. or ._ or .. inside the username \n No _ or . at the end")

password = Label(frame1 , text = "Password" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x = 370 , y = 310)
txt_pass = Entry(frame1 , font = ("times new roman",15,"bold") , bg = "lightgray" , show = "*")
txt_pass.place(x = 370 , y = 340 , width = 250)
tip.bind_widget(txt_pass , balloonmsg = "Should have at least one number. \n Should have at least one uppercase and one lowercase character. \n Should have at least one special symbol. \n Should be between 6 to 20 characters long.")

#- - - - - - - - - - - - - - - - - - - - - -Buttons
var1 = IntVar()
rd1 = Radiobutton(frame1 , text = "User" , value = 0 , variable = var1 , font = ("times new roman",15,"bold") , bg = "white")
rd1.place(x=50,y=375)
rd2 = Radiobutton(frame1 , text = "Admin" , value = 1 , variable = var1 , font = ("times new roman",15,"bold") , bg = "white")
rd2.place(x=140,y=375)

cal_img = ImageTk.PhotoImage(file = "images/cal.jpg")
cal_btn = Button(frame1 , image = cal_img , cursor = "hand2" , command = show_cal , bd=0)
cal_btn.place(x = 622 , y = 270)
tip.bind_widget(cal_btn , balloonmsg = "Select Date of Birth")

btn = ImageTk.PhotoImage(file = "images/button.png")
reg_btn = Button(frame1 , image = btn , bd = 0 , cursor = "hand2" , command = main_function).place(x = 50 , y = 420)

sign_btn = Button(root , text = "Sign In" , font = ("times new roman",20), bg = "white" , bd = 0 , cursor = "hand2" , command = login).place(x = 200 , y = 480 , width = 130 , height = 40) 

root.mainloop()   #Starting the main window
