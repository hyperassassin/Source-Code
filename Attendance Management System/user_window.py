from tkinter import *
import time
from PIL import ImageTk
from tkinter import messagebox,ttk
from dateutil.parser import parse
import pymysql
import cv2
from pyzbar.pyzbar import decode
from datetime import date
from tkcalendar import *

root = Tk()
root.title("User Window")
##w = root.winfo_screenwidth()
##h = root.winfo_screenheight()
root.geometry("1113x860+0+0")
root.resizable(0,0)

def showframe1():
    frame1 = Frame(root , bg = "white")
    frame1.place(x = 0 , y = 100 , relwidth = 1 , relheight = 1)

def showframe2():
    frame2 = Frame(root , bg = "white")
    frame2.place(x = 0 , y = 100 , relwidth = 1 , relheight = 1)

    edit_frame = LabelFrame(frame2 , bg = "white")
    edit_frame.place(x=60 , y=360 , width=198 , height = 43)

    update_control = LabelFrame(frame2 , text = "Update Controls" , font =("times new roman",14,"bold") , bg = "white")
    
    update_frame = LabelFrame(frame2 , text = "Update Your Details" , font =("times new roman",14,"bold") , bg = "white")

    #- - - - - - - - - - - - - - Frame Components
    id_v = IntVar()
    id_v.set("")
    name_v = StringVar()
    email_v = StringVar()
    address_v = StringVar()
    contact_v = IntVar()
    contact_v.set("")
    dob_v = StringVar()
    
    id_lbl = Label(frame2 , text = "ID            : " , font =("times new roman",15,"bold") , bg = "white").place(x=60,y=50)
    id_txt = Label(frame2 , text = "" , font =("times new roman",15,"bold") , bg = "white" , textvariable = id_v)
    id_txt.place(x=170,y=50)

    name_lbl = Label(frame2 , text = "Name      : " , font =("times new roman",15,"bold") , bg = "white").place(x=60,y=100)
    name_txt = Label(frame2 , text = "" , font =("times new roman",15,"bold") , bg = "white" , textvariable = name_v)
    name_txt.place(x=170,y=100)

    email_lbl = Label(frame2 , text = "Email      : " ,font =("times new roman",15,"bold") , bg = "white").place(x=60,y=150)
    email_txt = Label(frame2 , text = "" , font =("times new roman",15,"bold") , bg = "white" , textvariable = email_v)
    email_txt.place(x=170,y=150)

    dob_lbl = Label(frame2 , text = "D.O.B     : " , font =("times new roman",15,"bold") , bg = "white").place(x=60,y=200)
    dob_txt = Label(frame2 , text = "" , font =("times new roman",15,"bold") , bg = "white" , textvariable = dob_v)
    dob_txt.place(x=170,y=200)

    con_lbl = Label(frame2 , text = "Contact  : " , font =("times new roman",15,"bold") , bg = "white").place(x=60,y=250)
    con_txt = Label(frame2 , text = "" , font =("times new roman",15,"bold") , bg = "white" , textvariable = contact_v)
    con_txt.place(x=170,y=250)

    add_lbl = Label(frame2 , text = "Address  : " , font =("times new roman",15,"bold") , bg = "white").place(x=60,y=300)
    add_txt = Label(frame2 , text = "" , font =("times new roman",15,"bold") , bg = "white" , textvariable = address_v)
    add_txt.place(x=170,y=300)

    def edit_data():
        file = open("username_user.txt","r")
        verify = file.read()
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select id from user where username = %s",(verify))
            data = cur.fetchone()
            id_v.set(data)

            cur.execute("select name from user where username = %s",(verify))
            data1 = cur.fetchone()
            dat = ''.join(data1)
            name_v.set(dat)

            cur.execute("select email from user where username = %s",(verify))
            data2 = cur.fetchone()
            dat1 = ''.join(data2)
            email_v.set(dat1)

            cur.execute("select dob from user where username = %s",(verify))
            data3 = cur.fetchone()
            dob_v.set(data3)

            cur.execute("select contact from user where username = %s",(verify))
            data4 = cur.fetchone()
            res = int(''.join(map(str,data4)))    #tuple to int
            contact_v.set(res)

            cur.execute("select address from user where username = %s",(verify))
            data5 = cur.fetchone()
            dat5 = ''.join(data5)
            address_v.set(dat5)
        except Exception as e:
            messagebox.showerror("Error",e)
    edit_data()

    def edit_btn_det():
        update_frame.place(x=25,y=500,width=1020,height=140)
        update_control.place(x=25 , y=420 , width=1020 , height=70)
        b = name_v.get()
        c = email_v.get()
        e = contact_v.get()
        f = address_v.get()
        name_var.set(b)
        email_var.set(c)
        db = dob_txt['text']
        dob_var.set(db)
        con_var.set(e)
        add_var.set(f)
        name_up_txt.config(state = DISABLED)
        email_up_txt.config(state = DISABLED)
        dob_up_txt.config(state = DISABLED)
        con_up_txt.config(state = DISABLED)
        add_up_txt.config(state = DISABLED)

    #- - - - - - - - - - - - - - LabelFrame 1 Components
    edit_det = Button(edit_frame , text = " Edit Details " , font =("times new roman",15,"bold") , bg = "red" , fg = "white" , command = edit_btn_det).place(x=7,y=3,width=180,height=32)

    def show_cal():
        global cal_window
        cal_window = Toplevel()
        cal_window.title("Select Date")
        width = 250
        height = 230
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight()
        x = 1020
        y = 560
        cal_window.resizable(0, 0)
        cal_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        cal_frame = Frame(cal_window)
        cal_frame.pack()
        cal = Calendar(cal_frame , selectmode = "day" , year = 2021 , month = 3 , day = 9)
        cal.pack()
        def check():
            a = cal.get_date()
            date_obj = parse(a)
            b = date_obj.date()
            if dob_up_txt.get() == "":
                dob_up_txt.insert(0,str(b))
            else:
                dob_up_txt.delete(0,END)
                dob_up_txt.insert(0,str(b))
        ok = Button(cal_frame , text = "Ok" , command = check) 
        ok.pack(pady = 10)

    #- - - - - - - - - - - - - - Update Controls Components
    rd_var = IntVar()

    def update_radiobtn():
        if(rd_var.get() == 0):
            print("Name")
            name_up_txt.config(state = NORMAL)
            email_up_txt.config(state = DISABLED)
            dob_up_txt.config(state = DISABLED)
            con_up_txt.config(state = DISABLED)
            add_up_txt.config(state = DISABLED)
        elif(rd_var.get() == 1):
            print("Email")
            email_up_txt.config(state = NORMAL)
            name_up_txt.config(state = DISABLED)
            dob_up_txt.config(state = DISABLED)
            con_up_txt.config(state = DISABLED)
            add_up_txt.config(state = DISABLED)
        elif(rd_var.get() == 2):
            print("D.O.B")
            name_up_txt.config(state = DISABLED)
            email_up_txt.config(state = DISABLED)
            dob_up_txt.config(state = NORMAL)
            con_up_txt.config(state = DISABLED)
            add_up_txt.config(state = DISABLED)
        elif(rd_var.get() == 3):
            print("Contact")
            name_up_txt.config(state = DISABLED)
            email_up_txt.config(state = DISABLED)
            dob_up_txt.config(state = DISABLED)
            con_up_txt.config(state = NORMAL)
            add_up_txt.config(state = DISABLED)
        elif(rd_var.get() == 4):
            print("Address")
            name_up_txt.config(state = DISABLED)
            email_up_txt.config(state = DISABLED)
            dob_up_txt.config(state = DISABLED)
            con_up_txt.config(state = DISABLED)
            add_up_txt.config(state = NORMAL)
            
    name_rd = Radiobutton(update_control , text = "Name" , font =("times new roman",15,"bold") , bg = "white" , value = 0 , variable = rd_var)
    name_rd.place(x=10 , y=0)

    email_rd = Radiobutton(update_control , text = "Email Id" , font =("times new roman",15,"bold") , bg = "white" , value = 1 , variable = rd_var)
    email_rd.place(x=110 , y=0)

    dob_rd = Radiobutton(update_control , text = "D.O.B" , font =("times new roman",15,"bold") , bg = "white" , value = 2 , variable = rd_var)
    dob_rd.place(x=233 , y=0)

    con_rd = Radiobutton(update_control , text = "Contact No" , font =("times new roman",15,"bold") , bg = "white" , value = 3 , variable = rd_var)
    con_rd.place(x=340 , y=0)

    add_rd = Radiobutton(update_control , text = "Address" , font =("times new roman",15,"bold") , bg = "white" , value = 4 , variable = rd_var)
    add_rd.place(x=480 , y=0)

    up_b = Button(update_control , text = "Update" , font =("times new roman",15) , bg = "red" , fg = "white" , bd = 3 , command = update_radiobtn).place(x=650 , y=0 , width=130 , height=32)

    #- - - - - - - - - - - - - - LabelFrame 2 Components
    name_var = StringVar()
    email_var = StringVar()
    dob_var = StringVar()
    con_var = IntVar()
    con_var.set("")
    add_var = StringVar()
    
    name_up_lbl = Label(update_frame , text = "Name : " , font =("times new roman",15,"bold") , bg = "white").place(x=20,y=10)
    name_up_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , textvariable = name_var)
    name_up_txt.place(x=95,y=12)

    email_up_lbl = Label(update_frame , text = "Email : " ,font =("times new roman",15,"bold") , bg = "white").place(x=330,y=10)
    email_up_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , textvariable = email_var)
    email_up_txt.place(x=410,y=12)

    dob_up_lbl = Label(update_frame , text = "D.O.B : " , font =("times new roman",15,"bold") , bg = "white").place(x=640,y=10)
    dob_up_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , textvariable = dob_var)
    dob_up_txt.place(x=730,y=12)

    cal_img = ImageTk.PhotoImage(file = "images/cal.jpg")
    cal_btn = Button(update_frame , text = "      " , cursor = "hand2" , command = show_cal , bd=1)
    cal_btn.place(x=945,y=13)

    con_up_lbl = Label(update_frame , text = "Contact : " , font =("times new roman",15,"bold") , bg = "white").place(x=20,y=60)
    con_up_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , textvariable = con_var)
    con_up_txt.place(x=115,y=62)

    add_up_lbl = Label(update_frame , text = "Address  : " , font =("times new roman",15,"bold") , bg = "white").place(x=350,y=60)
    add_up_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , textvariable = add_var)
    add_up_txt.place(x=450,y=62)

    def update():
        if(name_up_txt['state'] == NORMAL):
            regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',re.IGNORECASE)
            name = name_up_txt.get()
            res = regex_name.search(name)
            if(res == None):
                messagebox.showerror("Error","Invalid Name")
            else:
                uid = id_txt['text']
                n = name_up_txt.get()
                try:
                    con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                    cur = con.cursor()
                    cur.execute("update user set name = %s where id = %s",(n,uid))
                    con.commit()
                    messagebox.showinfo("Success","Name Has Been Updated")
                    cur.close()
                    con.close()
                except Exception as e:
                    messagebox.showerror("Error",e)
        elif(email_up_txt['state'] == NORMAL):
            regex_email = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
            mail = email_up_txt.get()
            res_email = regex_email.search(mail)
            if(res_email == None):
                messagebox.showerror("Error","Invalid Email")
            else:
                uid = id_txt['text']
                e = email_up_txt.get()
                try:
                    con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                    cur = con.cursor()
                    cur.execute("update user set email = %s where id = %s",(e,uid))
                    con.commit()
                    messagebox.showinfo("Success","Email Has Been Updated")
                    cur.close()
                    con.close()
                except Exception as e:
                    messagebox.showerror("Error",e)
        elif(dob_up_txt['state'] == NORMAL):
            uid = id_txt['text']
            d = dob_up_txt.get()
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                cur.execute("update user set dob = %s where id = %s",(d,uid))
                con.commit()
                messagebox.showinfo("Success","D.O.B Has Been Updated")
                cur.close()
                con.close()
            except Exception as e:
                messagebox.showerror("Error",e)
        elif(con_up_txt['state'] == NORMAL):
            regex_phone = re.compile("^[7-9]\d{9}$")
            phone = con_up_txt.get()
            res_phone = regex_phone.match(phone)
            if(res_phone == None):
                messagebox.showerror("Error","Invalid Contact")
            else:
                uid = id_txt['text']
                c = con_up_txt.get()
                try:
                    con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                    cur = con.cursor()
                    cur.execute("update user set contact = %s where id = %s",(c,uid))
                    con.commit()
                    messagebox.showinfo("Success","Contact Has Been Updated")
                    cur.close()
                    con.close()
                except Exception as e:
                    messagebox.showerror("Error",e)
        elif(add_up_txt['state'] == NORMAL):
            regex_add = re.compile('[@_!#$%^&*()<>?\|}{~:]')
            add_ress = add_up_txt.get()
            res_add = regex_add.search(add_ress)
            if(res_add != None):
                messagebox.showerror("Error","Invalid Address")
            else:
                uid = id_txt['text']
                a = add_up_txt.get()
                try:
                    con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                    cur = con.cursor()
                    cur.execute("update user set address = %s where id = %s",(a,uid))
                    con.commit()
                    messagebox.showinfo("Success","Address Has Been Updated")
                    cur.close()
                    con.close()
                except Exception as e:
                    messagebox.showerror("Error",e)

    update_btn = Button(update_frame , text = " Update " , font =("times new roman",15,"bold") , bg = "red" , fg = "white" , bd = 3 , command = update).place(x=720,y=60,width=160,height=32)

def showframe3():
    frame3 = Frame(root , bg = "white")
    frame3.place(x = 0 , y = 100 , relwidth = 1 , relheight = 1)

    search_frame = LabelFrame(frame3)
    search_frame.place(x=25 , y=20 , width=700 , height=100)

    table_frame = LabelFrame(frame3 , bg = "white")
    table_frame.place(x=25 , y=130 , width=1255 , height = 300)

    panel_frame = LabelFrame(frame3)
    panel_frame.place(x=725 , y=20 , width=383 , height=100)

    update_frame = LabelFrame(frame3 , text = "Update Attendance Details" , font =("times new roman",14,"bold") , bg = "white")

    def today():
        to = date.today()
        file = open("username_user.txt","r")
        verify = file.read()
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select id from user where username = %s",(verify))
            data1 = cur.fetchone()
            res = int(''.join(map(str,data1)))
            
            cur.execute("select * from attendance where attend_date = %s and user_id = %s",(to,res))
            data = cur.fetchall()
            if len(data) != 0:
                table.delete(*table.get_children())
                for row in data:
                    table.insert('',END,values=row)
            if not data:
                messagebox.showerror("Error","No Data Found")
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",e)
    
    def showall():
        file = open("username_user.txt","r")
        verify = file.read()
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select id from user where username = %s",(verify))
            data1 = cur.fetchone()
            res = int(''.join(map(str,data1)))
            
            cur.execute("select * from attendance where user_id = %s",(res))
            data = cur.fetchall()
            if len(data) != 0:
                table.delete(*table.get_children())
                for row in data:
                    table.insert('',END,values=row)
            if not data:
                messagebox.showerror("Error","No Data Found")
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",e)

    def date_range():
        a = en_ex.get()
        b = en_ex1.get()
        file = open("username_user.txt","r")
        verify = file.read()
        if(en_ex.get() == "" or en_ex1.get() == ""):
            messagebox.showerror("Error","Select The Dates To Search The Data")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                cur.execute("select id from user where username = %s",(verify))
                data1 = cur.fetchone()
                res = int(''.join(map(str,data1)))

                # select * from attendance where user_id = 83952162 and attend_date between "2021-03-09" and "2021-03-10"; 
                cur.execute("select * from attendance where user_id = %s and attend_date between %s and %s",(res,a,b))
                data = cur.fetchall()
                if len(data) != 0:
                    table.delete(*table.get_children())
                    for row in data:
                        table.insert('',END,values=row)
                if not data:
                    messagebox.showerror("Error","No Data Found")
                cur.close()
                con.close()
            except Exception as e:
                messagebox.showerror("Error",e)
            
    def show_cal():
        global cal_window
        cal_window = Toplevel()
        cal_window.title("Select Date")
        width = 250
        height = 230
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight()
        x = 425
        y = 162
        cal_window.resizable(0, 0)
        cal_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        cal_frame = Frame(cal_window)
        cal_frame.pack()
        cal = Calendar(cal_frame , selectmode = "day" , year = 2021 , month = 3 , day = 9)
        cal.pack()
        def check():
            a = cal.get_date()
            date_obj = parse(a)
            b = date_obj.date()
            if en_ex.get() == "":
                en_ex.insert(0,str(b))
            else:
                en_ex.delete(0,END)
                en_ex.insert(0,str(b))
        ok = Button(cal_frame , text = "Ok" , command = check) 
        ok.pack(pady = 10)

    def show_cal1():
        global cal_window
        cal_window = Toplevel()
        cal_window.title("Select Date")
        width = 250
        height = 230
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight()
        x = 640
        y = 162
        cal_window.resizable(0, 0)
        cal_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        cal_frame = Frame(cal_window)
        cal_frame.pack()
        cal = Calendar(cal_frame , selectmode = "day" , year = 2021 , month = 3 , day = 9)
        cal.pack()
        def check():
            a = cal.get_date()
            date_obj = parse(a)
            b = date_obj.date()
            if en_ex1.get() == "":
                en_ex1.insert(0,str(b))
            else:
                en_ex1.delete(0,END)
                en_ex1.insert(0,str(b))
        ok = Button(cal_frame , text = "Ok" , command = check) 
        ok.pack(pady = 10)

    data_search = Button(search_frame , text = "Search" , font =("times new roman",14) , bd = 3 , command = date_range).place(x=170 , y=50 , width=100  , height=30)
    today_btn = Button(search_frame , text = "Today" , font =("times new roman",14,"bold") , bg = "blue" , command = today , bd = 3).place(x=285 , y=50 , width=100 , height=30)
    show_btn = Button(search_frame , text = "Show All" , font =("times new roman",14,"bold") , bg = "green" , command = showall , bd = 3).place(x=400 , y=50 , width=100 , height=30)

    date_lbl = Label(search_frame , text = "Date (yyyy-mm-dd)  From : " , font =("times new roman",14,"bold")).place(x=6 , y=10)
    en_ex = Entry(search_frame , font =("times new roman",12))
    en_ex.place(x=240 , y=11 , width=115 , height=25)

    cal_img = ImageTk.PhotoImage(file = "images/cal.jpg")
    cal_btn = Button(search_frame , text = "      " , cursor = "hand2" , command = show_cal , bd=1)
    cal_btn.place(x=365,y=11)

    to_lbl = Label(search_frame , text = "To : " , font =("times new roman",14,"bold")).place(x=400 , y=10)
    en_ex1 = Entry(search_frame , font =("times new roman",12))
    en_ex1.place(x=450 , y=11 , width=115 , height=25)

    cale_btn = Button(search_frame , text = "      " , cursor = "hand2" , command = show_cal1 , bd=1)
    cale_btn.place(x=575,y=11)
    
    total_pr = Label(panel_frame , bg = "darkblue").place(x=0,y=0,width=193,height=95)
    disp_pr = Label(panel_frame , text = "Total Present" , font =("times new roman",17,"bold") , bg = "darkblue" , fg = "white").place(x=25,y=20)
    count1 = Label(panel_frame , text = "[0]" , font = ("times new roman",17,"bold") , bg = "darkblue" , fg = "white")
    count1.place(x=77 , y=50)

    total_ab = Label(panel_frame , bg = "darkgreen").place(x=190,y=0,width=187,height=95)
    disp_ab = Label(panel_frame , text = "Total Absent" , font =("times new roman",17,"bold") , bg = "darkgreen" , fg = "white").place(x=218,y=20)
    count2 = Label(panel_frame , text = "[0]" , font =("times new roman",17,"bold") , bg = "darkgreen" , fg = "white")
    count2.place(x=265 , y=50)
    
    def data_attend():
        file = open("username_user.txt","r")
        verify = file.read()
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select id from user where username = %s",(verify))
            data1 = cur.fetchone()
            res = int(''.join(map(str,data1)))

            cur.execute("select count(*) from attendance where user_id = %s and attendance_type = 'PRESENT'",(res))
            data = cur.fetchone()
            dat = int(''.join(map(str,data)))
            res1 = str(dat)
            count1.config(text = "[" + res1 + "]")

            cur.execute("select count(*) from attendance where user_id = %s and attendance_type = 'ABSENT'",(res))
            data2 = cur.fetchone()
            dat1 = int(''.join(map(str,data2)))
            res2 = str(dat1)
            count2.config(text = "[" + res2 + "]")
            
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",e)
    data_attend()

    scroll = Scrollbar(table_frame , orient=VERTICAL , bd=3)   #ScrollBar
    scroll.place(x=1066,y=0, height=278)

    scroll_bar = Scrollbar(table_frame , orient=HORIZONTAL , bd=3)
    scroll_bar.place(x=0 , y=278 , width = 1083)

    table = ttk.Treeview(table_frame , columns = ("id","user_id","name","attendance","date","time") ,yscrollcommand = scroll.set , xscrollcommand = scroll_bar.set)   #Table
    scroll.config(command = table.yview)
    scroll_bar.config(command = table.xview)

    table.heading("id",text = "ID")
    table.heading("user_id",text = "User Id")
    table.heading("name",text = "Name")
    table.heading("attendance",text = "Attendance")
    table.heading("date",text = "Date")
    table.heading("time",text = "Time")

    table["show"] = 'headings'
    table.column("id",width=10)
    table.column("user_id",width=20)
    table.column("name",width=20)
    table.column("attendance",width=20)
    table.column("date",width=20)
    table.column("time",width=20)

    table.place(x=0, y=0, width=1065 , height=278)

    def fetch_data():
        file = open("username_user.txt","r")
        verify = file.read()
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select id from user where username = %s",(verify))
            data = cur.fetchone()
            res = int(''.join(map(str,data)))
            
            cur.execute("select * from attendance where user_id = %s",(res))
            data1 = cur.fetchall()
            if len(data1) != 0:
                table.delete(*table.get_children())
                for row in data1:
                    table.insert('',END,values=row)
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",e)
    fetch_data()

    def update():
        if(status.get() == " "):
            messagebox.showerror("Error","Select The Status To Update")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                a = status.get()
                b = id_v.get()
                cur.execute("update attendance set attendance_type = %s where id = %s",(a,b))
                con.commit()
                messagebox.showinfo("Info","Your Attendance Has Been Updated")
                fetch_data()
                cur.close()
                con.close()
                id_var.set("")
                uname_var.set("")
                udate_var.set("")
                status.set("")
            except Exception as e:
                messagebox.showerror("Error",e)

    id_var = IntVar()
    id_var.set("")
    id_v = IntVar()
    id_v.set("")
    uname_var = StringVar()
    udate_var = StringVar()

    u_at_id = Label(update_frame , text = "dss" , font =("times new roman",15,"bold") , bg = "white" , textvariable = id_v)
    
    u_id = Label(update_frame , text = "User ID " , font =("times new roman",15,"bold") , bg = "white").place(x=20 , y=17)
    u_id_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , state = DISABLED , textvariable = id_var)
    u_id_txt.place(x=110 , y=17)

    u_name = Label(update_frame , text = "Name " , font =("times new roman",15,"bold") , bg = "white").place(x=350 , y=17)
    u_name_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , state = DISABLED , textvariable = uname_var)
    u_name_txt.place(x=425 , y=17)

    u_date = Label(update_frame , text = "Date" , font =("times new roman",15,"bold") , bg = "white").place(x=350 , y=67)
    u_date_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , state = DISABLED , textvariable = udate_var)
    u_date_txt.place(x=425 , y=67)

    status_lbl = Label(update_frame , text = "Status" , font =("times new roman",15,"bold") , bg = "white").place(x=20 , y=67)
    status = ttk.Combobox(update_frame , font = ("times new roman",14) , state = "readonly" , justify = CENTER)
    status.place(x=110 , y=67)
    status['values'] = (" " , "PRESENT","ABSENT")
    status.current(0)

    update_btn = Button(update_frame , text = "Update" , font =("times new roman",15) , bg = "lightgreen" , command = update).place(x=680,y=13,width=150,height=35)

    def get_cursor(event):
        update_frame.place(x=25 , y=450 , width=1080 , height=140)
        cursor_row = table.focus()
        content = table.item(cursor_row)
        row = content['values']
        id_v.set(row[0])
        id_var.set(row[1])
        uname_var.set(row[2])
        udate_var.set(row[4])
        status.set(row[3])
        
    table.bind("<ButtonRelease-1>",get_cursor)
def show_frame4():                                          ##Take Attendance Function##
    capture = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
    font = cv2.FONT_HERSHEY_PLAIN
    received_data = None

    while True:
        _,frame = capture.read()
        decoded_data = decode(frame)
        try:
            data = decoded_data[0][0]
            if data != received_data:
                a = (str(data,'utf-8'))
                cv2.putText(frame,str(data),(50,50),font,2,(255,0,0),3)
                received_data = data
                messagebox.showinfo("Success","Your Attendance Has Been Recorded")
        except:
            pass
        cv2.imshow("Take Attendance",frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select name from user where id = %s",(a))
        data = cur.fetchall()
        print(data)
        da = date.today()
        curr_time = time.strftime("%H:%M:%S")
        pre = "PRESENT"
        cur.execute("insert into attendance(`user_id`,`name`,`attendance_type`,`attend_date`,`time`)values(%s,%s,%s,%s,%s)",(a,data,pre,da,curr_time))
        print(data)
        con.commit()
        cur.close()
        con.close()
    except UnboundLocalError as e:
        pass
    except Exception as e:
        messagebox.showerror("Error","Only User can record attendance in this login")

def showframe5():
    frame5 = Frame(root , bg = "white")
    frame5.place(x = 0 , y = 100 , relwidth = 1 , relheight = 1)

    apply_leave = LabelFrame(frame5 , bg = "white")
    apply_leave.place(x=170 , y=400 , width=198 , height=43)

    chk_stat = LabelFrame(frame5 , bg = "white")
    chk_stat.place(x=670 , y=400 , width=198 , height=43)

    clear_bt = LabelFrame(frame5 , bg = "white")
    clear_bt.place(x=420 , y=400 , width=198 , height=43)
    
    def show_cal():
        global cal_window
        cal_window = Toplevel()
        cal_window.title("Select Date")
        width = 250
        height = 230
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight()
        x = 425
        y = 162
        cal_window.resizable(0, 0)
        cal_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        cal_frame = Frame(cal_window)
        cal_frame.pack()
        cal = Calendar(cal_frame , selectmode = "day" , year = 2021 , month = 3 , day = 9)
        cal.pack()
        def check():
            a = cal.get_date()
            date_obj = parse(a)
            b = date_obj.date()
            if l_to_txt.get() == "":
                l_to_txt.insert(0,str(b))
            else:
                l_to_txt.delete(0,END)
                l_to_txt.insert(0,str(b))
        ok = Button(cal_frame , text = "Ok" , command = check) 
        ok.pack(pady = 10)

    def show_cal1():
        global cal_window
        cal_window = Toplevel()
        cal_window.title("Select Date")
        width = 250
        height = 230
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight()
        x = 610
        y = 162
        cal_window.resizable(0, 0)
        cal_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        cal_frame = Frame(cal_window)
        cal_frame.pack()
        cal = Calendar(cal_frame , selectmode = "day" , year = 2021 , month = 3 , day = 9)
        cal.pack()
        def check():
            a = cal.get_date()
            date_obj = parse(a)
            b = date_obj.date()
            if l_from_txt.get() == "":
                l_from_txt.insert(0,str(b))
            else:
                l_from_txt.delete(0,END)
                l_from_txt.insert(0,str(b))
        ok = Button(cal_frame , text = "Ok" , command = check) 
        ok.pack(pady = 10)

    def apply():
        uid = id_lbl['text']
        lt = l_type_txt.get()
        ldt = l_to_txt.get()
        ldf = l_from_txt.get()
        des = des_txt.get("1.0",END)
        if lt == " ":
            messagebox.showerror("Error","Select Type of Leave")
        elif ldt == "" or ldf == "" or des_txt.get("1.0",END) == "\n":
            messagebox.showerror("Error","Fill all the Fields")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                cur.execute("insert into `leave`(user_id,leave_type,leave_status,leave_to,leave_from,description) values(%s,%s,%s,%s,%s,%s)",(uid,lt,"ON LEAVE",ldt,ldf,des))
                con.commit()
                messagebox.showinfo("Success","Leave Applied")
                cur.close()
                con.close()
            except Exception as e:
                messagebox.showerror("Error",e)

    def status():
        uid = id_lbl['text']
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select leave_to from `leave` where user_id = %s",(uid))
            data = cur.fetchone()           #Tuple > print(type(data))
            a = str(data[0])                #Str > print(type(a))
            a1 = parse(a)                   #Date > print(type(a1))
            b1 = a1.date()
            print("b1 :- " , b1)

            cur.execute("select leave_from from `leave` where user_id = %s",(uid))
            data1 = cur.fetchone()
            bstr = str(data1[0])
            adat = parse(bstr)
            b2 = adat.date()
            print("b2 :- " , b2)
            diff = (b1-b2).days
            print(diff)

            tod = date.today()
            a = ((b1-tod).days)         #Last Date Of Leave - Today's Date

            if (a == 0 or a < 0):
                print("Your Leave Days Has Exhausted")
                stat = "LEAVE DAYS EXHAUSTED"
                cur.execute("update `leave` set leave_status = %s where user_id = %s",(stat,uid))
                con.commit()
                l_status_txt.config(text = stat)
                cur.close()
                con.close()
            else:
                a1 = str(a)
                messagebox.showinfo("Info","You Have " + a1 + " Days Left of Leave")
                cur.execute("select leave_status from `leave` where user_id = %s",(uid))
                data = cur.fetchone()
                dat = ''.join(data)
                l_status_txt.config(text = dat)
                cur.close()
                con.close()
        except Exception as e:
            messagebox.showerror("Error","No Active Leave Found !!")

    def clear():
        l_type_txt.set("")
        l_status_txt.config(text = "")
        l_to1.set("")
        l_fr.set("")
        des_txt.delete("1.0",END)
    
    title_label = Label(frame5 , text = "User ID    :  " , font =("times new roman",15,"bold") , bg = "white").place(x=170,y=40)
    id_lbl = Label(frame5 , text = "" , font =("times new roman",15,"bold") , bg = "white")
    id_lbl.place(x=290,y=40)

    titl_label = Label(frame5 , text = "Name    : " , font =("times new roman",15,"bold") , bg = "white").place(x=400,y=40)
    name_label = Label(frame5 , text = "" , font =("times new roman",15,"bold") , bg = "white")
    name_label.place(x=500,y=40)

    #variables
    lstat = StringVar()
    l_to1 = StringVar()
    l_fr = StringVar()
    
    l_type = Label(frame5 , text = "Leave Type  : " , font =("times new roman",15,"bold") , bg = "white").place(x=70,y=120)
    l_type_txt = ttk.Combobox(frame5 , font = ("times new roman",15) , state = "readonly" , justify = CENTER)     #Combobox
    l_type_txt.place(x=210,y=120,width=205)
    l_type_txt['values'] = (" " , "Medical" , "Personal" , "Other")
    l_type_txt.current(0)

    l_status = Label(frame5 , text = "Leave Status  : " , font =("times new roman",15,"bold") , bg = "white").place(x=530,y=120)
    l_status_txt = Label(frame5 , text = " " ,font =("times new roman",15) , bg = "white")
    l_status_txt.place(x=680,y=120)

    l_to = Label(frame5 , text = "Leave To      : " , font =("times new roman",15,"bold") , bg = "white").place(x=70,y=180)
    l_to_txt = Entry(frame5 , font =("times new roman",15) , bg = "white" , bd = 2 , textvariable = l_to1)
    l_to_txt.place(x=210,y=180)

    #cal_img = ImageTk.PhotoImage(file = "images/cal.jpg")
    cal_btn = Button(frame5 , text = "      " , cursor = "hand2" , bd=1 , command = show_cal)
    cal_btn.place(x=425,y=182)

    l_from = Label(frame5 , text = "Leave From    : " , font =("times new roman",15,"bold") , bg = "white").place(x=530,y=180)
    l_from_txt = Entry(frame5 , font =("times new roman",15) , bg = "white" , bd = 2 , textvariable = l_fr)
    l_from_txt.place(x=680,y=180)

    cale_btn = Button(frame5 , text = "      " , cursor = "hand2" , bd=1 , command = show_cal1)
    cale_btn.place(x=895,y=182)
        
    des = Label(frame5 , text = "Description  : " , font =("times new roman",15,"bold") , bg = "white").place(x=140,y=240)
    des_txt = Text(frame5 , font = ("times new roman",15) , bg = "white" , bd = 2 , height = 5 , width = 50)
    des_txt.place(x=270,y=240)

    app_leave = Button(apply_leave , text = "Apply Leave" , font=("times new roman",15,"bold") , bg = "red" , fg = "white" , command = apply)  #Button
    app_leave.place(x=7 , y=3 , width = 180 , height = 32)

    check_stat = Button(chk_stat , text = "Check Status" , font =("times new roman",15,"bold") , bg = "red" , fg = "white" , command = status)
    check_stat.place(x=7,y=3,width=180,height=32)

    clear_f = Button(clear_bt , text = "Clear Fields" , font =("times new roman",15,"bold") , bg = "red" , fg = "white" , command = clear)
    clear_f.place(x=7,y=3,width=180,height=32)
    
    file = open("username_user.txt","r")
    verify = file.read()
    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select id from user where username = %s",(verify))
        data = cur.fetchone()
        id_lbl.config(text = data)
        cur.execute("select name from user where username = %s",(verify))
        data1 = cur.fetchone()
        dat = ''.join(data1)
        name_label.config(text = dat)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)

def logout():                                               ##Logout Function##
    msg = messagebox.askyesno("Confirm","Confirm Logout")
    print(msg)
    if msg == True:
        root.destroy()
    import login

def exit_cmd():
    msg = messagebox.askyesno("Confirm","Are you sure you want to exit ?")
    print(msg)
    if msg == True:
        exit(0)

def clock_time():
    curr_time = time.strftime("%H:%M:%S")
    clock.config(text ="[" + curr_time + "]")
    clock.after(200,clock_time)

def date_today():
    curr_date = time.strftime("%d-%m-%Y")
    date_lbl.config(text = "[" + curr_date + "]")

pic_attend = Label(root , bg = "white")
pic_attend.place(x=0,y=0,width=200,height = 60)

im_at = ImageTk.PhotoImage(file="attend.png")
pic_attend.config(image=im_at)
pic_attend.image = im_at

lbl_frame1 = LabelFrame(root , bg="white" , relief = RAISED , bd = 0)
lbl_frame1.place(x=200 , y=0 , relwidth=1 , height=60)
head = Label(lbl_frame1 , text = "Attendance Management System" , font = ("times new roman",28,"bold") , bg = "white").place(x=0 , y=7)
wel = Label(lbl_frame1 , text = "Welcome , " , font = ("times new roman",15) , bg = "white").place(x=545 , y = 28)
wel_name = Label(lbl_frame1 , text = "" , font = ("times new roman",15) , bg = "white" , fg = "black")
wel_name.place(x=635 , y=28)

def read_user():
    file = open("username_user.txt","r")
    verify = file.read()
    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select name from user where username = %s",(verify))
        data = cur.fetchone()
        dat = ''.join(data)
        wel_name.config(text = dat)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)

read_user()

clock = Label(lbl_frame1 , font = ("times new roman",15) , bg = "white")
clock.place(x= 700 , y=2)
clock_time()

date_lbl = Label(lbl_frame1 , font = ("times new roman",15) , bg = "white" , fg = "black")
date_lbl.place(x=790 , y=2)
date_today()

lbl_frame2 = LabelFrame(root , bg = "floralwhite")
lbl_frame2.place(x=0 , y=60 , relwidth = 1 , height = 40)


btn1 = Button(lbl_frame2 , text = "Update Your Details" , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5 , command = showframe2).place(x=0 , y=0 , width = 190 , height = 35)
btn2 = Button(lbl_frame2 , text = "View Attendance" , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5 , command = showframe3).place(x=195 , y=0 , width = 180 , height = 35)
btn3 = Button(lbl_frame2 , text = "Take Attendance" , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5 , command = show_frame4).place(x=380 , y=0 , width = 180 , height = 35)
btn4 = Button(lbl_frame2 , text = "Take Leave" , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5 , command = showframe5).place(x=565 , y=0 , width = 180 , height = 35)
btn5 = Button(lbl_frame2 , text = "Logout" , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5 , command = logout).place(x=750 , y=0 , width = 180 , height = 35)
btn6 = Button(lbl_frame2 , text = "Exit" , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5 , command = exit_cmd).place(x=935 , y=0 , width = 170, height = 35)

root.mainloop()
