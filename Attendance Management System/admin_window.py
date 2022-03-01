from tkinter import *
import time
from tkinter import ttk,messagebox
import cv2
from pyzbar.pyzbar import decode
from PIL import Image,ImageTk,ImageDraw,ImageFont,ImageOps
import pymysql
import random
import qrcode
import os
from datetime import date
from tkcalendar import *
from dateutil.parser import parse
from openpyxl import Workbook
from openpyxl.styles import NamedStyle,Font,Border,Side,Alignment

root = Tk()
root.title("Admin Window")
##w = root.winfo_screenwidth()
##h = root.winfo_screenheight()
##print(w,h)
root.geometry("1280x860+0+0")
root.resizable(0,0)
##"%dx%d" %(w,h)

def show_frame1():                                              ##Dashboard Function##
    frame = Frame(root , bg = "royalblue3")
    frame.place(x = 0 , y = 100 , relwidth = 1 , relheight = 1)

    #- - - - - - - - - - - - - Total Department 
    total_dep = Label(frame , text = "Total Department" , font =("times new roman",16,"bold") , bg = "dodgerblue2" , fg = "white" , bd = 5 , relief = RIDGE)
    total_dep.place(x=100 , y=50 , width=300 , height=40)

    white_dept_lbl = Label(frame , bg = "white" , bd = 5 , relief = RIDGE)
    white_dept_lbl.place(x=100 , y=90 , width=300 , height=190)

    total_lbl1 = Label(frame , text = "Total " , font =("times new roman",30,"bold") , bg = "white")
    total_lbl1.place(x=140 , y=120)

    count1 = Label(frame , text = "[0]" , font =("times new roman",30,"bold") , bg = "white")
    count1.place(x=250 , y=120)

    dep_lbl = Label(frame , text = "Department" , font =("times new roman","30","bold") , bg = "white")
    dep_lbl.place(x=140 , y=175)

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select count(*) from department")
        data = cur.fetchall()
        count1.config(text = data)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)
    #- - - - - - - - - - - - - Total Users
    total_user = Label(frame , text = "Total Users" , font =("times new roman",16,"bold") , bg = "dodgerblue2" , fg = "white" , bd = 5 , relief = RIDGE)
    total_user.place(x=500 , y=50 , width=300 , height=40)

    white_user_lbl = Label(frame , bg = "white" , bd = 5 , relief = RIDGE)
    white_user_lbl.place(x=500 , y=90 , width=300 , height=190)

    total_lbl2 = Label(frame , text = "Total " , font =("times new roman",30,"bold") , bg = "white")
    total_lbl2.place(x=550 , y=120)

    count2 = Label(frame , text = "[0]" , font =("times new roman",30,"bold") , bg = "white")
    count2.place(x=660 , y=120)

    use_lbl = Label(frame , text = "Users" , font =("times new roman","30","bold") , bg = "white")
    use_lbl.place(x=550 , y=175)

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select count(*) from user")
        data = cur.fetchall()
        count2.config(text = data)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)

    #- - - - - - - - - - - - - Total Leave
    total_leave = Label(frame , text = "Users On Leave" , font =("times new roman",16,"bold") , bg = "dodgerblue2" , fg = "white" , bd = 5 , relief = RIDGE)
    total_leave.place(x=900 , y=50 , width=300 , height=40)

    white_leave_lbl = Label(frame , bg = "white" , bd = 5 , relief = RIDGE)
    white_leave_lbl.place(x=900 , y=90 , width=300 , height=190)

    total_lbl3 = Label(frame , text = "Total " , font =("times new roman",30,"bold") , bg = "white")
    total_lbl3.place(x=930 , y=120)

    count3 = Label(frame , text = "[0]" , font =("times new roman",30,"bold") , bg = "white")
    count3.place(x=1040 , y=120)

    leave_lbl = Label(frame , text = "Users On Leave" , font =("times new roman","30","bold") , bg = "white")
    leave_lbl.place(x=915 , y=175)

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select count(*) from `leave` where leave_status = %s",("ON LEAVE"))
        data = cur.fetchall()
        count3.config(text = data)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)

    #- - - - - - - - - - - - - Total Id Card
    total_id = Label(frame , text = "ID Cards" , font =("times new roman",16,"bold") , bg = "dodgerblue2" , fg = "white" , bd = 5 , relief = RIDGE)
    total_id.place(x=100 , y=330 , width=300 , height=40)

    white_id_lbl = Label(frame , bg = "white" , bd = 5 , relief = RIDGE)
    white_id_lbl.place(x=100 , y=370 , width=300 , height=190)

    total_lbl4 = Label(frame , text = "Total " , font =("times new roman",30,"bold") , bg = "white")
    total_lbl4.place(x=140 , y=400)

    count4 = Label(frame , text = "[0]" , font =("times new roman",30,"bold") , bg = "white")
    count4.place(x=250 , y=400)

    id_lbl = Label(frame , text = "Id Cards" , font =("times new roman","30","bold") , bg = "white")
    id_lbl.place(x=140 , y=460)

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select count(*) from id_card")
        data = cur.fetchall()
        count4.config(text = data)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)

    #- - - - - - - - - - - - - Today Attendance
    today_attend = Label(frame , text = "Today's Attendance" , font =("times new roman",16,"bold") , bg = "dodgerblue2" , fg = "white" , bd = 5 , relief = RIDGE)
    today_attend.place(x=500 , y=330 , width=300 , height=40)

    white_attend_lbl = Label(frame , bg = "white" , bd = 5 , relief = RIDGE)
    white_attend_lbl.place(x=500 , y=370 , width=300 , height=190)

    total_lbl5 = Label(frame , text = "Total " , font =("times new roman",30,"bold") , bg = "white")
    total_lbl5.place(x=530 , y=400)

    count5 = Label(frame , text = "[0]" , font =("times new roman",30,"bold") , bg = "white")
    count5.place(x=640 , y=400)

    attend_lbl = Label(frame , text = "Users Present" , font =("times new roman",30,"bold") , bg = "white")
    attend_lbl.place(x=530 , y=460)

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        da = date.today()
        cur.execute("select count(*) from attendance where attend_date = %s and attendance_type = 'PRESENT'",(da))
        data = cur.fetchall()
        count5.config(text = data)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)

    #- - - - - - - - - - - - - Company About
    comp_ab = Label(frame , text = "About Us" , font =("times new roman",16,"bold") , bg = "dodgerblue2" , fg = "white" , bd = 5 , relief = RIDGE)
    comp_ab.place(x=900 , y=330 , width=300 , height=40)

    white_comp_lbl = Label(frame , bg = "white" , bd = 5 , relief = RIDGE)
    white_comp_lbl.place(x=900 , y=370 , width=300 , height=190)

    develop_lbl = Label(frame , text = "Python Project \n\n Developed By MacSoft Pvt Ltd. \n\n Contact :- 9875462154" , font =("times new roman",15,"bold") , bg = "white").place(x=910 , y=390 , height=155)
    
def show_frame2():                                              ##Manage Department Function##
    #- - - - - - - - - - - Frame 1
    frame1 = Frame(root , bg = "white")
    frame1.place(x = 0 , y = 100 , relwidth = 1 , relheight = 1)

    #- - - - - - - - - - - LabelFrame
    dept_manage = LabelFrame(frame1 , text = "Department Management" , bg = "white" , font = ("times new roman",14,"bold"))
    dept_manage.place(x=160 , y=100 , width=930 , height=290)

    up_dep_frame = LabelFrame(frame1 , text = "Update Details" , bg = "white" , font =("times new roman",14,"bold"))

    btn_frame = LabelFrame(dept_manage)
    btn_frame.place(x=15 , y=200 , width = 510 , height = 50)

    table_frame = LabelFrame(dept_manage)
    table_frame.place(x=600 , y=50 , width=300 , height = 210)

    def search():
        selected = combo.get()
        if selected == "Search by ...":
            messagebox.showinfo("Info","Select The Criteria Of Search")
        if selected == "Name":
            text = txt_combo.get()
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                cur.execute("select * from department where name = %s",(text))
                result = cur.fetchall()
                if len(result) != 0:
                    table.delete(*table.get_children())
                    for row in result:
                        table.insert('',END,values=row)
                if not result:
                    messagebox.showerror("Error","No Data Found")
                cur.close()
                con.close()
            except Exception as e:
                messagebox.showerror("Error",e)

    def showall():
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select * from department")
            result = cur.fetchall()
            if len(result) != 0:
                table.delete(*table.get_children())
                for row in result:
                    table.insert('',END,values=row)
            if not result:
                messagebox.showerror("Error","No Data Found")
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",e)
            
    #- - - - - - - - - - - LabelFrame 1 Components 
    combo = ttk.Combobox(dept_manage , font = ("times new roman",15) , state = "readonly" , justify = CENTER)
    combo.place(x=5 , y=10)
    combo['values'] = ("Search by ..." , "Name")
    combo.current(0)
    txt_c = StringVar()
    txt_combo = Entry(dept_manage , font = ("times new roman",15) , bg = "lightyellow" , bd = 2 , textvariable = txt_c)
    txt_combo.place(x=235 , y=10)
    search_btn = Button(dept_manage , text = "Search" , font =("times new roman",15,"bold") , bg = "yellow" , command = search).place(x=450 , y=7 , width=140 , height=35)
    show_btn = Button(dept_manage , text = "Show All" , font =("times new roman",15,"bold") , bg = "blue" , fg = "white" , command = showall).place(x=600 ,y=7 , width=140 , height=35)
    name = Label(dept_manage , text = "Department Name" , font =("times new roman",18,"bold") , bg = "white").place(x = 235 , y = 80)
    name_var = StringVar()
    name_txt = Entry(dept_manage , font =("times new roman",15) , textvariable = name_var , bg = "lightgray" , bd = 2)
    name_txt.place(x=220 , y = 125 , width = 230)

    def add_depart():
        if(name_txt.get() == ""):
            messagebox.showerror("Error","Enter Name To Add Department")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                name_dep = str(name_txt.get())
                cur.execute("insert into department(`name`)values(%s)",(name_dep))
                con.commit()
                fetch_data()
                count()
                cur.close()
                con.close()
                messagebox.showinfo("Success","Department Added Successfully")
                name_var.set("")
            except Exception as e:
                messagebox.showerror("Error",e)

    def clear_fields():
        name_var.set("")
        d_id.set("")
        d_name.set("")
        txt_c.set("")

    def update_dep():
        if(dep_name_txt.get() == "" or dep_id_txt.get() == ""):
            messagebox.showerror("Error","Select Data From Table")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                name_dep = str(dep_name_txt.get())
                id_dep = dep_id_txt.get()
                cur.execute("update department set name = %s where id = %s",(name_dep,id_dep))
                con.commit()
                fetch_data()
                count()
                cur.close()
                con.close()
                messagebox.showinfo("Success","Department Name Updated SuccessFully")
                d_id.set("")
                d_name.set("")
            except Exception as e:
                messagebox.showerror("Error",e)

    def delete_dep():
        if(name_txt.get() == ""):
            messagebox.showerror("Error","Enter Name To Delete Department")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                name_dep = str(name_txt.get())
                cur.execute("delete from department where name = %s",(name_dep))
                con.commit()
                cur.close()
                con.close()
                fetch_data()
                count()
                messagebox.showinfo("Success","Department Deleted SuccessFully")
                name_var.set("")
            except Exception as e:
                messagebox.showerror("Error",e)

##  #- - - - - - - - - - - LabelFrame 1.1 Components
    d_id = IntVar()
    d_id.set("")
    d_name = StringVar()
    dep_id = Label(up_dep_frame , text="ID : " , font =("times new roman",15,"bold") , bg = "white")
    dep_id.place(x=8 , y=9)
    dep_id_txt = Entry(up_dep_frame , font =("times new roman",15) , bg = "white" , textvariable = d_id , state = DISABLED)
    dep_id_txt.place(x=55 , y=10)

    dep_name = Label(up_dep_frame , text = "Name : " , font =("times new roman",15,"bold") , bg = "white")
    dep_name.place(x=265 , y=9)
    dep_name_txt = Entry(up_dep_frame , font =("times new roman",15) , bg = "white" , textvariable = d_name , state = DISABLED)
    dep_name_txt.place(x=340 , y=10)
                     
    #- - - - - - - - - - - LabelFrame 2 Components
    add_bt = Button(btn_frame , text = "Add" , bg = "green" , fg = "white" , bd = 2 , font =("times new roman",15) , command = add_depart).place(x=4 , y=4 , width = 120 , height = 35)
    update_bt = Button(btn_frame , text = "Update" , bg = "green" , fg = "white" , bd = 2 , font =("times new roman",15) , command = update_dep)
    update_bt.place(x=130 , y=4 , width = 120 , height = 35)
    delete_bt = Button(btn_frame , text = "Delete" , bg = "green" , fg = "white" , bd = 2 , font =("times new roman",15) , command = delete_dep)
    delete_bt.place(x=255 , y=4 , width = 120 , height = 35)
    clear_bt = Button(btn_frame , text = "Clear" , bg = "green" , fg = "white" , bd = 2 , font =("times new roman",15) , command = clear_fields).place(x=380 , y=4 , width = 120 , height = 35)

    def count():
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select count(*) from department")
            data = cur.fetchone()
            dat = data[0]
            #print(dat)
            if dat == 0:
                update_bt.config(state=DISABLED)
                delete_bt.config(state=DISABLED)
            else:
                update_bt.config(state=NORMAL)
                delete_bt.config(state=NORMAL)
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",e)
    count()
        
    #- - - - - - - - - - - LabelFrame 3 Components
    scroll = Scrollbar(table_frame , orient=VERTICAL, bd=3)
    scroll.place(x=277,y=0,height=205)
    table = ttk.Treeview(table_frame , columns=("id","name") , yscrollcommand = scroll.set)
    scroll.config(command = table.yview)

    table.heading("id",text = "Id")
    table.heading("name",text ="Name")

    table["show"] = 'headings'
    table.column("id",width=10)
    table.column("name",width=10)

    table.place(x=0 , y=0 , width=275 , height=205)

    def fetch_data():
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select * from department")
            data = cur.fetchall()
            if len(data) != 0:
                table.delete(*table.get_children())
                for row in data:
                    table.insert('',END,values=row)
            if not data:
                messagebox.showerror("Error","No Data Found")
            cur.close()
            con.close()
        except:
            messagebox.showerror("Error","Error :- "+e)
    fetch_data()
    
    def get_cursor(event):
        dep_name_txt.config(state = NORMAL)
        cursor_row = table.focus()
        content = table.item(cursor_row)
        row = content['values']
        d_id.set(row[0])
        name_var.set(row[1])
        d_name.set(row[1])
        count()
        up_dep_frame.place(x=160 , y=400 , width=590 , height=80)
    table.bind('<ButtonRelease-1>',get_cursor)

def show_frame3():                                              ##Generate ID Card Function##
    #- - - - - - - - - - Frame 2
    frame2 = Frame(root , bg = "white")
    frame2.place(x = 0 , y = 100 , relwidth = 1 , relheight = 1)

    #- - - - - - - - - - LabelFrame
    generate = LabelFrame(frame2 , bg = "white")
    generate.place(x=0 , y=8 , relwidth = 1 , height = 300)

    search_frame = LabelFrame(generate , bg = "white")
    search_frame.place(x=10 , y=5 , width=880 , height=40)

    id_generate = LabelFrame(generate , bg = "white")
    id_generate.place(x=950 , y=5 , width=198 , height=43)

    tab_frame = LabelFrame(generate , bg = "white")
    tab_frame.place(x=10 , y=55 , width = 1250 , height = 230)

    photo_frame = LabelFrame(frame2 , bg = "white")
    photo_frame.place(x=0 , y=310 , relwidth=1 , relheight=1)

    in_photo_frame = LabelFrame(photo_frame , bg = "white")
    in_photo_frame.place(x=965 , y=4 , width=300 , height=350)

    edit_frame = LabelFrame(photo_frame , bg = "white")
    edit_frame.place(x=330 , y=230 , width=198 , height = 43)

    def search():
        drop = search_combo.get()
        if drop == "Select Option":
            messagebox.showinfo("Info","Select Criteria For Search")
        if drop == "ID":
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                id_search = txt_search.get()
                cur.execute("select id,name,address,contact,dob from user where id = %s",(id_search))
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
        if drop == "Name":
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                name = txt_search.get()
                cur.execute("select id,name,address,contact,dob from user where name = %s",(name))
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
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select id,name,address,contact,dob from user")
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

    def clear():
        search_var.set("")
        id_var.set("")
        name_var.set("")
        con_var.set("")
        add_var.set("")
        dob_var.set("")

    #- - - - - - - - - - LabelFrame 2 Components
    search_lbl = Label(search_frame , text = "Search By" , font=("times new roman",15,"bold") ,bg = "white").place(x=4 , y=3)   #Label
    search_combo = ttk.Combobox(search_frame , font = ("times new roman",15) , state = "readonly" , justify = CENTER)     #Combobox
    search_combo.place(x=110 , y=3 , width = 200)
    search_combo['values'] = ("Select Option" , "ID" , "Name")
    search_combo.current(0)
    search_var = StringVar()
    txt_search = Entry(search_frame , font = ("times new roman",15) , bg = "lightyellow" , bd = 2 , textvariable = search_var)   #Entry Field
    txt_search.place(x=325 , y=3)
    search_btn = Button(search_frame , text = "Search" , font =("times new roman",15,"bold") , bg = "yellow" , command = search).place(x=550 , y=2 , width=100 , height=30)  #Button 1
    clear_btn = Button(search_frame , text = "Clear" , font =("times new roman",15,"bold") , bg = "blue" , fg = "white" , command = clear).place(x=660 ,y=2 , width=100 , height=30)  #Button 2
    show_btn = Button(search_frame , text = "Show All" , font =("times new roman",15,"bold") , bg = "green" , fg = "white" , command = showall).place(x=770 ,y=2 , width=100 , height=30)  #Button 3

    def qr_code():
        if(id_txt.get()== "" or name_txt.get()== "" or con_txt.get()== "" or add_txt.get()== "" or dob_txt.get()== ""):
            messagebox.showerror("Error","Select Data From The Table !!")
        else:
           img = Image.new('RGB',(286,336),(255,255,255))
           draw = ImageDraw.Draw(img)

           (x,y) = (70,7)
           heading = "Block Pvt Ltd."
           msg = str(heading)
           color = 'rgb(0,0,0)'
           font = ImageFont.truetype('arial.ttf',size=23)
           draw.text((x,y),msg,fill = color , font = font)
           
           (x,y) = (30,135)
           idno = id_txt.get()
           no = idno
           msg = str("Id :- " + str(idno))
           color = 'rgb(0,0,0)'
           font = ImageFont.truetype('arial.ttf',size = 20)
           draw.text((x,y),msg,fill = color , font = font)

           (x,y) = (30,170)
           msg = name_txt.get()
           name = msg
           msg = str('Name : ' + str(msg))
           color = 'rgb(0,0,0)'
           font = ImageFont.truetype('arial.ttf',size=20)
           draw.text((x,y),msg,fill = color , font = font)

           (x,y) = (30,205)
           msg = con_txt.get()
           msg = str("Mobile No :- " + str(msg))
           color = 'rgb(0,0,0)'
           draw.text((x,y),msg,fill = color , font = font)

           (x,y) = (30,240)
           msg = add_txt.get()
           msg = str("Address :- " + str(msg))
           color = 'rgb(0,0,0)'
           draw.text((x,y),msg,fill = color , font = font)

           (x,y) = (30,275)
           msg = dob_txt.get()
           msg = str("D.O.B :- " + str(msg))
           color = 'rgb(0,0,0)'
           draw.text((x,y),msg,fill = color , font = font)
           
           img.save('images/id.png')

           image = qrcode.QRCode(box_size = 3)
           a = no
           image.add_data(a)
           image.make(fit = True)
           qr = image.make_image()
           qr.save('images/qr.png')
           til = Image.open('images/id.png')
           im = Image.open('images/qr.png')
           til.paste(im,(95,35))
           til.save('images/final.png')

           a = Image.open("images/final.png")
           color = "black"
           border = (2,2,2,2)
           new_img = ImageOps.expand(a,border=border,fill=color)
           ap = 'id_card/'+ name + '.png'
           new_img.save(ap)
           new_img.show()

           id_txt.config(state = DISABLED)
           name_txt.config(state = DISABLED)
           add_txt.config(state = DISABLED)
           con_txt.config(state = DISABLED)
           dob_txt.config(state = DISABLED)

           pic_label = Label(in_photo_frame)
           pic_label.place(x=4 , y=4 , width=286 , height=336)

           list_of_file = os.listdir("F:/Attendance_management_system/id_card")
##           print(list_of_file)
           l_name = name_txt.get()
           ex = l_name + '.png'
           if ex in list_of_file:
               au = 'id_card/'+ name + '.png'
##               print(au)
               pil_img = Image.open(au)
               tk_img = ImageTk.PhotoImage(image=pil_img)
               pic_label.config(image = tk_img)
               pic_label.image = tk_img

           try:
               con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
               cur = con.cursor()
               i = id_txt.get()
               n = name_txt.get()
               c = con_txt.get()
               a = add_txt.get()
               d = dob_txt.get()
               cur.execute("insert into id_card(user_id,name,contact,address,dob)values(%s,%s,%s,%s,%s)",(i,n,c,a,d))
               con.commit()
               cur.close()
               con.close()
           except Exception as e:
                messagebox.showerror("Error",e)
           
           id_var.set("")
           name_var.set("")
           con_var.set("")
           add_var.set("")
           dob_var.set("")

    #- - - - - - - - - - LabelFrame 3 Components
    id_btn = Button(id_generate , text = "Generate Id Card" , command = qr_code , font=("times new roman",15,"bold") , bg = "red" , fg = "white")  #Button
    id_btn.place(x=7 , y=3 , width = 180 , height = 32)

    #- - - - - - - - - - LabelFrame 4 Components
    scroll = Scrollbar(tab_frame , orient=VERTICAL, bd=3)   #ScrollBar
    scroll.place(x=1228,y=0, height=225) 
    table = ttk.Treeview(tab_frame , columns = ("id","name","address","contact","dob") ,yscrollcommand = scroll.set)   #Table
    scroll.config(command = table.yview)

    table.heading("id",text = "Id")
    table.heading("name",text = "Name")
    table.heading("address",text = "Address")
    table.heading("contact",text = "Mobile No")
    table.heading("dob",text = "D.O.B")

    table["show"] = 'headings'
    table.column("id",width=20)
    table.column("name",width=20)
    table.column("address",width=20)
    table.column("contact",width=20)
    table.column("dob",width=20)
    
    table.place(x=0, y=0, width=1226 , height=225)

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select id,name,address,contact,dob from user")
        data = cur.fetchall()
        if len(data) != 0:
            table.delete(*table.get_children())
            for row in data:
                table.insert('',END,values=row)
            con.commit()
            cur.close()
            con.close()
    except:
        messagebox.showerror("Error",e)

    id_var = IntVar()
    id_var.set("")
    name_var = StringVar()
    add_var = StringVar()
    con_var = IntVar()
    con_var.set("")
    dob_var = StringVar()
    #- - - - - - - - - - LabelFrame 5 Components
    id_lbl = Label(photo_frame , text = "Id" , font = ("times new roman",15,"bold") , bg = "white").place(x=5 , y=10)
    id_txt = Entry(photo_frame , font = ("times new roman",15) , textvariable = id_var , bg = "white" , bd = 2 , state = DISABLED)
    id_txt.place(x=70 , y=10)

    name_lbl = Label(photo_frame , text = "Name" , font = ("times new roman",15,"bold") , bg = "white").place(x=320 , y=10)
    name_txt = Entry(photo_frame , font = ("times new roman",15) , textvariable = name_var , bg = "white" , bd = 2 , state = DISABLED)
    name_txt.place(x=400 , y=10)

    add_lbl = Label(photo_frame , text = "Address" , font = ("times new roman",15,"bold") , bg = "white").place(x=650 , y=10)
    add_txt = Entry(photo_frame , font = ("times new roman",15) , textvariable = add_var , bg = "white" , bd = 2 , state = DISABLED)
    add_txt.place(x=750 , y=10)

    con_lbl = Label(photo_frame , text = "Mobile No" , font = ("times new roman",15,"bold") , bg = "white").place(x=170 , y=80)
    con_txt = Entry(photo_frame , font = ("times new roman",15) , textvariable = con_var  , bg = "white" , bd = 2 , state = DISABLED)
    con_txt.place(x=280 , y=80)

    dob_lbl = Label(photo_frame , text = "D.O.B" , font = ("times new roman",15,"bold") , bg = "white").place(x=550 , y=80)
    dob_txt = Entry(photo_frame , font = ("times new roman",15) , textvariable = dob_var  , bg = "white" , bd = 2 , state = DISABLED)
    dob_txt.place(x=635 , y=80)

    def edit_details():
        name_txt.config(state = NORMAL)
        add_txt.config(state = NORMAL)
        con_txt.config(state = NORMAL)
        dob_txt.config(state = NORMAL)

    #- - - - - - - - - - LabelFrame 7 Components
    edit_btn = Button(edit_frame , text = "Edit Details" , font=("times new roman",15,"bold") , command = edit_details , bg = "red" , fg = "white")
    edit_btn.place(x=7 , y=3 , width = 180 , height = 32)

    def get_cursor(event):
        cursor_row = table.focus()
        content = table.item(cursor_row)
        row = content['values']
        id_var.set(row[0])
        name_var.set(row[1])
        add_var.set(row[2])
        con_var.set(row[3])
        dob_var.set(row[4])

    table.bind('<ButtonRelease-1>',get_cursor)
        
def show_frame4():                                                  ##View Attendance Function##
    #- - - - - - - - - - - - Frame 4
    frame3 = Frame(root , bg = "white")
    frame3.place(x = 0 , y = 100 , relwidth = 1 , relheight = 1)

    #- - - - - - - - - - - - LabelFrame
    search_frame = LabelFrame(frame3)
    search_frame.place(x=25 , y=20 , width=700 , height=100)

    panel_frame = LabelFrame(frame3)
    panel_frame.place(x=725 , y=20 , width=555 , height=100)

    table_frame = LabelFrame(frame3 , bg = "white")
    table_frame.place(x=25 , y=130 , width=1255 , height = 300)

    update_frame = LabelFrame(frame3 , text = "Update Attendance Details" , font =("times new roman",14,"bold") , bg = "white")

    rep_fr = Label(frame3 , text = "Generate Report" , font =("times new roman",15,"bold") , bg = "white").place(x=25 , y=620)

    rep_btn_fr = LabelFrame(frame3 , bg = "white")
    rep_btn_fr.place(x=190 , y=615 , width=404 , height=43)
    
    #- - - - - - - - - - - - LabelFrame 1 Components
    def search():
        if(emp_txt.get() == ""):
            messagebox.showerror("Error","Type To Search")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                a = emp_txt.get()
                cur.execute("select * from attendance where user_id = %s",(a))
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
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select * from attendance")
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

    def today():
        to = date.today()
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select * from attendance where attend_date = %s",(to))
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
            if en_ex1.get() == "":
                en_ex1.insert(0,str(b))
            else:
                en_ex1.delete(0,END)
                en_ex1.insert(0,str(b))
        ok = Button(cal_frame , text = "Ok" , command = check) 
        ok.pack(pady = 10)

    def date_range():
        a = en_ex.get()
        b = en_ex1.get()
        if(en_ex.get() == "" or en_ex1.get() == ""):
            messagebox.showerror("Error","Select The Dates To Search The Data")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                
                # select * from attendance where user_id = 83952162 and attend_date between "2021-03-09" and "2021-03-10"; 
                cur.execute("select * from attendance where attend_date between %s and %s",(a,b))
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
    
    emp_label = Label(search_frame , text = "User Id " , font =("times new roman",16,"bold")).place(x=6 , y=4)
    emp_txt = Entry(search_frame , font =("times new roman",15) , bg = "white" , bd = 2)
    emp_txt.place(x=90 , y=4)

    search_btn = Button(search_frame , text = "Search" , font =("times new roman",14,"bold") , bg = "yellow" , command = search , bd = 3).place(x=312 , y=3 , width=100 , height=30)
    today_btn = Button(search_frame , text = "Today" , font =("times new roman",14,"bold") , bg = "blue" , command = today , bd = 3).place(x=435 , y=3 , width=100 , height=30)
    show_btn = Button(search_frame , text = "Show All" , font =("times new roman",14,"bold") , bg = "green" , command = showall , bd = 3).place(x=555 , y=3 , width=100 , height=30)

    date_lbl = Label(search_frame , text = "Date (yyyy-mm-dd)  From : " , font =("times new roman",14,"bold")).place(x=6 , y=50)
    en_ex = Entry(search_frame , font =("times new roman",12))
    en_ex.place(x=240 , y=52 , width=115 , height=25)

    cal_img = ImageTk.PhotoImage(file = "images/cal.jpg")
    cal_btn = Button(search_frame , text = "    " , cursor = "hand2" , bd=1 , command = show_cal)
    cal_btn.place(x=360,y=52)

    to_lbl = Label(search_frame , text = "To : " , font =("times new roman",14,"bold")).place(x=388 , y=52)
    en_ex1 = Entry(search_frame , font =("times new roman",12))
    en_ex1.place(x=435 , y=52 , width=115 , height=25)

    cale_btn = Button(search_frame , text = "    " , cursor = "hand2" , bd=1 , command = show_cal1)
    cale_btn.place(x=556,y=52)
    
    data_search = Button(search_frame , text = "Search" , font =("times new roman",14) , bd = 3 , command = date_range).place(x=585 , y=50 , width=105  , height=30)

    #- - - - - - - - - - - - LabelFrame 2 Components
    total_ab = Label(panel_frame , bg = "darkblue").place(x=0,y=0,width=135,height=95)
    disp_ab = Label(panel_frame , text = "Total Absent" , font =("times new roman",17,"bold") , bg = "darkblue" , fg = "white").place(x=1,y=20)
    count1 = Label(panel_frame , text = "[0]" , font = ("times new roman",17,"bold") , bg = "darkblue" , fg = "white")
    count1.place(x=50 , y=50)

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select count(*) from attendance where attendance_type = %s",("ABSENT"))
        data = cur.fetchone()
        count1.config(text = data)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)


    total_le = Label(panel_frame , bg = "purple").place(x=135,y=0,width=135,height=95)
    disp_le = Label(panel_frame , text = "Total Leave" , font =("times new roman",17,"bold") , bg = "purple" , fg = "white").place(x=140,y=20)
    count2 = Label(panel_frame , text = "[0]" , font =("times new roman",17,"bold") , bg = "purple" , fg = "white")
    count2.place(x=185 , y=50)
    def leave_count():
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select count(*) from `leave` where leave_status = %s",("ON LEAVE"))
            data1 = cur.fetchone()
            count2.config(text = data1)
            cur.close()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",e)
    leave_count()
    total_pr = Label(panel_frame , bg = "darkgreen").place(x=270,y=0,width=142,height=95)
    disp_pr = Label(panel_frame , text = "Total Present" , font =("times new roman",17,"bold") , bg = "darkgreen" , fg = "white").place(x=270,y=20)
    count3 = Label(panel_frame , text = "[0]" , font =("times new roman",17,"bold") , bg = "darkgreen" , fg = "white")
    count3.place(x=320 , y=50)

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select count(*) from attendance where attendance_type = %s",("PRESENT"))
        data = cur.fetchone()
        count3.config(text = data)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)

    total_day = Label(panel_frame , bg = "lightblue").place(x=412,y=0,width=137,height=95)
    disp_day = Label(panel_frame , text = "Total Days" , font =("times new roman",17,"bold") , bg = "lightblue" , fg = "white").place(x=420,y=20)
    count4 = Label(panel_frame , text = "[0]" , font =("times new roman",17,"bold") , bg = "lightblue" , fg = "white")
    count4.place(x=460 , y=50)

    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select count(*) from attendance")
        data = cur.fetchone()
        count4.config(text = data)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)
    
    #- - - - - - - - - - - - LabelFrame 3 Components
    scroll = Scrollbar(table_frame , orient=VERTICAL , bd=3)   #ScrollBar
    scroll.place(x=1232,y=0, height=295)

    scroll_bar = Scrollbar(table_frame , orient=HORIZONTAL , bd=3)
    scroll_bar.place(x=0 , y=278 , width = 1230)

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

    table.place(x=0, y=0, width=1230 , height=278)

    def fetch_data():
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            cur.execute("select * from attendance")
            data = cur.fetchall()
            if len(data) != 0:
                table.delete(*table.get_children())
                for row in data:
                    table.insert('',END,values=row)
                con.commit()
                cur.close()
                con.close()
        except Exception as e:
            messagebox.showerror("Error",e)
    fetch_data()
    
    #- - - - - - - - - - - LabelFrame 4 Components
    def update():
        if(status.get() == " "):
            messagebox.showerror("Error","Select The Status To Update")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                a = status.get()
                b = u_id_txt.get()
                cur.execute("update attendance set attendance_type = %s where user_id = %s",(a,b))
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

    def delete():
        if(u_id_txt.get() == ""):
            messagebox.showerror("Error","Select The Data To Delete")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                b = u_id_txt.get()
                cur.execute("delete from attendance where user_id = %s",(b))
                con.commit()
                messagebox.showinfo("Info","Attendance Deleted SuccessFully")
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
    uname_var = StringVar()
    udate_var = StringVar()
    
    u_id = Label(update_frame , text = "User ID " , font =("times new roman",15,"bold") , bg = "white").place(x=20 , y=17)
    u_id_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , state = DISABLED , textvariable = id_var)
    u_id_txt.place(x=110 , y=17)

    u_name = Label(update_frame , text = "Name " , font =("times new roman",15,"bold") , bg = "white").place(x=350 , y=17)
    u_name_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , state = DISABLED , textvariable = uname_var)
    u_name_txt.place(x=425 , y=17)

    u_date = Label(update_frame , text = "Date" , font =("times new roman",15,"bold") , bg = "white").place(x=660 , y=17)
    u_date_txt = Entry(update_frame , font =("times new roman",15) , bg = "white" , bd = 2 , state = DISABLED , textvariable = udate_var)
    u_date_txt.place(x=730 , y=17)

    status_lbl = Label(update_frame , text = "Status" , font =("times new roman",15,"bold") , bg = "white").place(x=20 , y=67)
    status = ttk.Combobox(update_frame , font = ("times new roman",14) , state = "readonly" , justify = CENTER)
    status.place(x=110 , y=67)
    status['values'] = (" " , "PRESENT","ABSENT")
    status.current(0)

    update_btn = Button(update_frame , text = "Update" , font =("times new roman",15) , bg = "lightgreen" , command=update).place(x=980 , y=13 , width=150 , height=35)
    delete_btn = Button(update_frame , text = "Delete" , font =("times new roman",15) , bg = "red" , command=delete).place(x=980 , y=64 , width=150 , height=35)

    def get_cursor(event):
        update_frame.place(x=25 , y=450 , width=1240 , height=140)
        cursor_row = table.focus()
        content = table.item(cursor_row)
        row = content['values']
        id_var.set(row[1])
        uname_var.set(row[2])
        udate_var.set(row[4])
        status.set(row[3])
        
    table.bind("<ButtonRelease-1>",get_cursor)

    wb = Workbook()
    sheet = wb.active

    def today_excel():
        try:
            con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
            cur = con.cursor()
            dat = date.today()
            cur.execute("select * from attendance where attend_date = %s",(dat))
            result = cur.fetchall()
            if not result:
                messagebox.showerror("Error","No Attendance Recorded Today")
            else:
                sheet.title = "ATTENDANCE REPORT"
                num_fields = len(cur.description)
                field_names = [i[0] for i in cur.description]
                #print(field_names)
                sheet.append(field_names)
                for row in result:
                    sheet.append(row)
                header = NamedStyle(name="header")
                header.font = Font(bold=True)
                header.border = Border(bottom=Side(border_style="thin"))
                header.alignment = Alignment(horizontal="center", vertical="center")
                header_row = sheet[1]
                for cell in header_row:
                    cell.style = header
                wbname = "attendance_report"
                wb.save(wbname + '.xlsx')
                messagebox.showinfo("Success","Report has been Generated !!")
        except Exception as e:
            messagebox.showerror("Error","Report already generated")

    def date_excel():
        if (en_ex.get() == "" or en_ex1.get() == ""):
            messagebox.showerror("Error","Select Date to Generate Report !!")
        else:
            try:
                con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
                cur = con.cursor()
                dt1 = en_ex.get()
                dt2 = en_ex1.get()
                cur.execute("select * from attendance where attend_date between %s and %s",(dt1,dt2))
                result = cur.fetchall()
                if not result:
                    messagebox.showerror("Error","No Data Found")
                else:
                    sheet.title = "ATTENDANCE REPORT"
                    num_fields = len(cur.description)
                    field_names = [i[0] for i in cur.description]
                    #print(field_names)
                    sheet.append(field_names)
                    for row in result:
                        sheet.append(row)
                    header = NamedStyle(name="header")
                    header.font = Font(bold=True)
                    header.border = Border(bottom=Side(border_style="thin"))
                    header.alignment = Alignment(horizontal="center", vertical="center")
                    header_row = sheet[1]
                    for cell in header_row:
                        cell.style = header
                    wbname = "attendance_date_report"
                    wb.save(wbname + '.xlsx')
                    messagebox.showinfo("Success","Report has been Generated !!")
            except Exception as e:
                messagebox.showerror("Error","Report already generated")

    today_btn = Button(rep_btn_fr , text = "Today's Attendance" , font =("times new roman",15,"bold") , bg = "red" , fg = "white" , command = today_excel).place(x=9 , y=3 , width = 190 , height = 32)
    datewise_btn = Button(rep_btn_fr , text = "Generate Report" , font =("times new roman",15,"bold") , bg = "red" , fg = "white" , bd = 1 , command = date_excel).place(x=210 , y=3 , width = 180 , height = 32)
    
def show_frame5():                                          ##Take Attendance Function##
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
        cur.execute("select name from admin where id = %s",(a))
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
        messagebox.showerror("Error","Only Admin Can Record Attendance in this login")
def show_frame6():                                          ##Take Leave Function##
    frame4 = Frame(root , bg = "white")
    frame4.place(x = 0 , y = 100 , relwidth = 1 , relheight = 1)

    apply_leave = LabelFrame(frame4 , bg = "white")
    apply_leave.place(x=170 , y=400 , width=198 , height=43)

    chk_stat = LabelFrame(frame4 , bg = "white")
    chk_stat.place(x=670 , y=400 , width=198 , height=43)

    clear_bt = LabelFrame(frame4 , bg = "white")
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
            a = ((b1-tod).days)  #Last Date Of Leave - Today's Date

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
    
    title_label = Label(frame4 , text = "User ID    :  " , font =("times new roman",15,"bold") , bg = "white").place(x=170,y=40)
    id_lbl = Label(frame4 , text = "" , font =("times new roman",15,"bold") , bg = "white")
    id_lbl.place(x=290,y=40)

    titl_label = Label(frame4 , text = "Name    : " , font =("times new roman",15,"bold") , bg = "white").place(x=400,y=40)
    name_label = Label(frame4 , text = "" , font =("times new roman",15,"bold") , bg = "white")
    name_label.place(x=500,y=40)

    #variables
    lstat = StringVar()
    l_to1 = StringVar()
    l_fr = StringVar()
    
    l_type = Label(frame4 , text = "Leave Type  : " , font =("times new roman",15,"bold") , bg = "white").place(x=70,y=120)
    l_type_txt = ttk.Combobox(frame4 , font = ("times new roman",15) , state = "readonly" , justify = CENTER)     #Combobox
    l_type_txt.place(x=210,y=120,width=205)
    l_type_txt['values'] = (" " , "Medical" , "Personal" , "Other")
    l_type_txt.current(0)

    l_status = Label(frame4 , text = "Leave Status  : " , font =("times new roman",15,"bold") , bg = "white").place(x=530,y=120)
    l_status_txt = Label(frame4 , text = " " ,font =("times new roman",15) , bg = "white")
    l_status_txt.place(x=680,y=120)

    l_to = Label(frame4 , text = "Leave To      : " , font =("times new roman",15,"bold") , bg = "white").place(x=70,y=180)
    l_to_txt = Entry(frame4 , font =("times new roman",15) , bg = "white" , bd = 2 , textvariable = l_to1)
    l_to_txt.place(x=210,y=180)

    #cal_img = ImageTk.PhotoImage(file = "images/cal.jpg")
    cal_btn = Button(frame4 , text = "      " , cursor = "hand2" , bd=1 , command = show_cal)
    cal_btn.place(x=425,y=182)

    l_from = Label(frame4 , text = "Leave From    : " , font =("times new roman",15,"bold") , bg = "white").place(x=530,y=180)
    l_from_txt = Entry(frame4 , font =("times new roman",15) , bg = "white" , bd = 2 , textvariable = l_fr)
    l_from_txt.place(x=680,y=180)

    cale_btn = Button(frame4 , text = "      " , cursor = "hand2" , bd=1 , command = show_cal1)
    cale_btn.place(x=895,y=182)
        
    des = Label(frame4 , text = "Description  : " , font =("times new roman",15,"bold") , bg = "white").place(x=140,y=240)
    des_txt = Text(frame4 , font = ("times new roman",15) , bg = "white" , bd = 2 , height = 5 , width = 50)
    des_txt.place(x=270,y=240)

    app_leave = Button(apply_leave , text = "Apply Leave" , font=("times new roman",15,"bold") , bg = "red" , fg = "white" , command = apply)  #Button
    app_leave.place(x=7 , y=3 , width = 180 , height = 32)

    check_stat = Button(chk_stat , text = "Check Status" , font =("times new roman",15,"bold") , bg = "red" , fg = "white" , command = status)
    check_stat.place(x=7,y=3,width=180,height=32)

    clear_f = Button(clear_bt , text = "Clear Fields" , font =("times new roman",15,"bold") , bg = "red" , fg = "white" , command = clear)
    clear_f.place(x=7,y=3,width=180,height=32)
    
    file = open("username_admin.txt","r")
    verify = file.read()
    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select id from admin where username = %s",(verify))
        data = cur.fetchone()
        id_lbl.config(text = data)
        cur.execute("select name from admin where username = %s",(verify))
        data1 = cur.fetchone()
        dat = ''.join(data1)
        name_label.config(text = dat)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)
def clock_time():
    curr_time = time.strftime("%H:%M:%S")
    clock.config(text ="[" + curr_time + "]")
    clock.after(200,clock_time)

def date_today():
    curr_date = time.strftime("%d-%m-%Y")
    date_lbl.config(text = "[" + curr_date + "]")

def logout():                                               ##Logout Function##
    msg = messagebox.askyesno("Confirm","Confirm Logout")
    print(msg)
    if msg == True:
        root.destroy()
        import login
        
####lbl_frame = LabelFrame(root , bg = "blue")
##lbl_frame.place(x=0 , y=0 , width=200 , height=60)

pic_attend = Label(root , bg = "white")
pic_attend.place(x=0,y=0,width=200,height=60)

##img_at = Image.open("attend.png")
im_at = ImageTk.PhotoImage(file="attend.png")
pic_attend.config(image = im_at)
pic_attend.image = im_at


lbl_frame1 = LabelFrame(root , bg = "white" , bd = 0)
lbl_frame1.place(x=200 , y=0 , relwidth=1 , height=60)
head = Label(lbl_frame1 , text = "Attendance Management System" , font = ("times new roman",28,"bold") , bg = "white" , fg = "black").place(x=0 , y=7)
wel = Label(lbl_frame1 , text = "Welcome , " , font = ("times new roman",15) , bg = "white" , fg = "black").place(x=570 , y = 25)
wel_name = Label(lbl_frame1 , text = "" , font = ("times new roman",15) , bg = "white" , fg = "black")
wel_name.place(x=660 , y=25) 

def read_user():
    file = open("username_admin.txt","r")
    verify = file.read()
    try:
        con = pymysql.connect(host='localhost',user='root',password='sagar',db='attendance_management',port=3306)
        cur = con.cursor()
        cur.execute("select name from admin where username = %s",(verify))
        data = cur.fetchone()
        dat = ''.join(data)
        wel_name.config(text = dat)
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Error",e)

read_user()
clock = Label(lbl_frame1 , font = ("times new roman",15) , bg = "white" , fg = "black")
clock.place(x= 800 , y=25) 
clock_time()

date_lbl = Label(lbl_frame1 , font = ("times new roman",15) , bg = "white" , fg = "black")
date_lbl.place(x=890 , y=25)
date_today()

lbl_frame2 = LabelFrame(root , bg = "floralwhite")
lbl_frame2.place(x=0 , y=60 , relwidth = 1 , height = 40)

btn1 = Button(lbl_frame2 , text = "Dashboard" , command = show_frame1 , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5).place(x=0 , y=0 , width = 180, height = 35)
btn2 = Button(lbl_frame2 , text = "Manage Department" , command = show_frame2 , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5).place(x=185 , y=0 , width = 180 , height = 35)
btn3 = Button(lbl_frame2 , text = "Generate Id Card" , command = show_frame3 , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5).place(x=370 , y=0 , width = 180 , height = 35)
btn4 = Button(lbl_frame2 , text = "View Attendance" , command = show_frame4 , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5).place(x=555 , y=0 , width = 180 , height = 35)
btn5 = Button(lbl_frame2 , text = "Take Attendance" , command = show_frame5 , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5).place(x=740 , y=0 , width = 180 , height = 35)
btn6 = Button(lbl_frame2 , text = "Take Leave" , command = show_frame6 , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5).place(x=925 , y=0 , width = 180 , height = 35)
btn7 = Button(lbl_frame2 , text = "Logout" , font = ("times new roman",15) , fg = "white" , bg = "green" , bd = 5 , command = logout).place(x=1108 , y=0 , width = 165 , height = 35)

root.mainloop()
