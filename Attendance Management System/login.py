from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
import pymysql
from tkinter import messagebox,ttk
import re

root = Tk()
root.title("Attendance Management System Using QR Code")
##w = root.winfo_screenwidth()
##h = root.winfo_screenheight()
root.geometry("1280x860+0+0")
root.resizable(0,0)
##%dx%d" % (w,h)

#Forget Password 

def clock_time():
    curr_time = time.strftime("%H:%M:%S")
    clock.config(text ="[" + curr_time + "]")
    clock.after(200,clock_time)

def date_today():
    curr_date = time.strftime("%d-%m-%Y")
    date_lbl.config(text = "[" + curr_date + "]")

def regis():
    root.destroy()
    import register

def login_validation():
    name = txt1.get()
    passwd = txt2.get()
    if(txt1.get() == "" or txt2.get() == ""):
        messagebox.showerror("Error","Fill all the Fields")
    elif var.get()== 0:
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select * from user where username = %s and password = %s",(name,passwd))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error","Username or password not found !!")
            else:
                #print(row)
                messagebox.showinfo("Success","Login Successful !!!")
                file = open("username_user.txt","w")
                file.write(name)
                file.close()
                root.destroy()
                import user_window
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",e)
    elif var.get()== 1:
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select * from admin where username = %s and password = %s",(name,passwd))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error","Username or password not found !!")
            else:
                #print(row)
                messagebox.showinfo("Success","Login Successful !!!")
                file = open("username_admin.txt","w")
                file.write(name)
                file.close()
                root.destroy()
                import admin_window
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",e)

def forget_password():
    forget = Toplevel()
    forget.title("Forget Password")
    forget.geometry("350x400+490+155")
    forget.focus_force()
    forget.config(bg="white")
    forget.resizable(0,0)
    forget.grab_set()

    heading = Label(forget , text = "Forget Password" , font = ("times new roman",20,"bold") , bg = "white" , fg = "red").place(x=0,y=10,relwidth=1,height=50)

    uname = Label(forget , text = "Username" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x=50 , y =100)
    txt_username = Entry(forget , font = ("times new roman",15) , bg = "lightgray")
    txt_username.place(x=50 , y=130 , width=250)

    old_password = Label(forget , text = "Old Password" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x=50 , y=170)
    txt_old_pass = Entry(forget , font = ("times new roman",15) , show = '*' ,bg = "lightgray")
    txt_old_pass.place(x=50 , y=200 , width=250)

    new_password = Label(forget , text = "New Password" , font = ("times new roman",15,"bold") , bg = "white" , fg = "gray").place(x=50 , y=240)
    txt_new_pass = Entry(forget , font = ("times new roman",15) , show = '*' , bg = "lightgray")
    txt_new_pass.place(x=50 , y=270 , width = 250)

    var1 = IntVar()
    rd1 = Radiobutton(forget , text = "User" , value = 0 , variable = var1 , font = ("times new roman",15,"bold") , bg = "white")
    rd1.place(x=60,y=300)
    rd2 = Radiobutton(forget , text = "Admin" , value = 1 , variable = var1 , font = ("times new roman",15,"bold") , bg = "white")
    rd2.place(x=150,y=300)

    def update_pass():
        regex_pass = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
        new_pass = txt_new_pass.get()
        res_pass = regex_pass.search(new_pass)
        user = txt_username.get()

        if(txt_username.get()== "" or txt_old_pass.get()== "" or txt_new_pass.get()==""):
            messagebox.showerror("Error","Fill all the Fields")
            txt_username.delete(0,END)
            txt_old_pass.delete(0,END)
            txt_new_pass.delete(0,END)
        elif(txt_old_pass.get() == txt_new_pass.get()):
            messagebox.showerror("Error","Old and new password cannot be same")
            txt_username.delete(0,END)
            txt_old_pass.delete(0,END)
            txt_new_pass.delete(0,END)
        elif(res_pass == None):
            messagebox.showerror("Error","New password doesn't match the given criteria")
            txt_username.delete(0,END)
            txt_old_pass.delete(0,END)
            txt_new_pass.delete(0,END)
        else:
            if(var1.get() == 0):
                try:
                    con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                    cur = con.cursor()
                    cur.execute("update user set password = %s where username = %s",(new_pass,user))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password Changed Successfully !!")
                    txt_username.delete(0,END)
                    txt_old_pass.delete(0,END)
                    txt_new_pass.delete(0,END)
                except Exception as e:
                    messagebox.showerror("Error",e)
            elif(var1.get() == 1):
                try:
                    con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                    cur = con.cursor()
                    cur.execute("update admin set password = %s where username = %s",(new_pass,user))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password Changed Successfully !!")
                    txt_username.delete(0,END)
                    txt_old_pass.delete(0,END)
                    txt_new_pass.delete(0,END)
                except Exception as e:
                    messagebox.showerror("Error",e)
    change_password = Button(forget , text = "Change Password" , font = ("times new roman",15,"bold") , bg = "green" , fg = "white" , cursor = "hand2" , command = update_pass).place(x=90 , y=340 , width=160 , height=35)
        
left_lbl = Label(root , bg = "#08A3D2")
left_lbl.place(x=0,y=0 , relheight = 1 , width = 600)

right_lbl = Label(root , bg = "#031F3C")
right_lbl.place(x=600,y=0,relheight = 1 , relwidth = 1)

pic_attend = Label(root , bg = "white")
pic_attend.place(x=0,y=0,width=200,height=60)

##img_at = Image.open("attend.png")
im_at = ImageTk.PhotoImage(file="attend.png")
pic_attend.config(image = im_at)
pic_attend.image = im_at

lbl_frame1 = LabelFrame(root , bg = "white" , bd = 0)
lbl_frame1.place(x=200 , y=0 , relwidth=1 , height=60)
head = Label(lbl_frame1 , text = "    Attendance Management System" , font = ("times new roman",28,"bold") , bg = "white" , fg = "black").place(x=0 , y=7)

clock = Label(lbl_frame1 , font = ("times new roman",15) , bg = "white" , fg = "black")
clock.place(x= 800 , y=25) 
clock_time()

date_lbl = Label(lbl_frame1 , font = ("times new roman",15) , bg = "white" , fg = "black")
date_lbl.place(x=890 , y=25)
date_today()

login_frame = Frame(root , bg = "white")
login_frame.place(x=250,y=150,width=800,height=500)

title = Label(login_frame , text = "LOGIN HERE" , font = ("times new roman",30,"bold") , bg = "white" , fg = "#08A3D2").place(x=250,y=50)

user = Label(login_frame , text = "USERNAME" , font = ("times new roman",18,"bold") , bg = "white" , fg = "gray").place(x=250,y=150)

txt1 = Entry(login_frame , font = ("times new roman",15) , bg = "lightgray")
txt1.place(x=250,y=180,width=350,height=35)

password = Label(login_frame , text = "PASSWORD" , font = ("times new roman",18,"bold") , bg = "white" , fg = "gray").place(x=250,y=250)

txt2 = Entry(login_frame , font = ("times new roman",15) , show = '*' , bg = "lightgray")
txt2.place(x=250,y=280,width=350,height=35)

var = IntVar()
rd1 = Radiobutton(login_frame , text = "User" , value = 0 , variable = var , font = ("times new roman",15,"bold") , bg = "white")
rd1.place(x=250,y=320)
rd2 = Radiobutton(login_frame , text = "Admin" , value = 1 , variable = var , font = ("times new roman",15,"bold") , bg = "white")
rd2.place(x=350,y=320)

reg_btn = Button(login_frame , text = "Register New Account?",bd=0,font = ("times new roman",14), cursor = "hand2" , bg = "white" , fg = "#B00857" , command = regis).place(x=250,y=355)

forget_btn = Button(login_frame , text = "Forget Password?",bd=0,font = ("times new roman",14), cursor = "hand2" , bg = "white" , fg = "#B00857" , command = forget_password).place(x=450,y=355)

login = Button(login_frame , text = "Login",font = ("times new roman",20,"bold") , bg = "#B00857" , fg = "white" , cursor = "hand2" , command = login_validation).place(x=250,y=400,width=180,height=40)

lbl = Label(root , text = "\nClock" , font=("Book Antiqua",25,"bold") , compound = BOTTOM , fg = "white" , bg = "black",bd=0)
lbl.place(x=90 , y=175 , height = 450 , width = 350)

def clock_image(hr,mi,sec):
    clock = Image.new("RGB",(400,400),(0,0,0))
    draw = ImageDraw.Draw(clock)

    bg = Image.open("images/clock1.png")
    bg = bg.resize((300,300) , Image.ANTIALIAS)
    clock.paste(bg,(50,50))

    draw.line((200,200,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill = "#DF005E" , width = 4)

    draw.line((200,200,200+80*sin(radians(mi)),210-80*cos(radians(mi))),fill = "white" , width = 3)

    draw.line((200,200,200+100*sin(radians(sec)),240-100*cos(radians(sec))),fill = "yellow" , width = 2)

    draw.ellipse((195,195,210,210) , fill = "#1AD5D5")

    clock.save("images/clock_new.png")

def working():
    global img
    h = datetime.now().time().hour
    m = datetime.now().time().minute
    s = datetime.now().time().second
    hr = (h/12)*360
    mi = (m/60)*360
    sec = (s/60)*360
    clock_image(hr,mi,sec)
    img = ImageTk.PhotoImage(file="images/clock_new.png")
    lbl.config(image=img)
    lbl.after(200,working)

working()
root.mainloop()

