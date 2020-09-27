from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

def clear_data():
    fname.set("")
    lname.set("")
    evar.set("")
    convar.set("")
    addvar.set("")

def insert_data():
    if(fname.get()=="" or lname.get()=="" or evar.get()=="" or convar.get()=="" or addvar.get()==""):
       messagebox.showerror("Python","Fill All The Entry Fields")
    else:
        try:
            con = sqlite3.connect("contact.db")
            cursor = con.cursor()
            insert_query = """INSERT INTO contact(fname,lname,email,contact,address)VALUES(?,?,?,?,?);"""
            data_tuple = (fname.get(),lname.get(),evar.get(),convar.get(),addvar.get())
            cursor.execute(insert_query,data_tuple)
            con.commit()
            con.close()
            messagebox.showinfo("Python","Contact Saved")
            fetch_data()
            clear_data()
        except sqlite3.Error as error:
            messagebox.showerror("Python","Error is :- "+ str(error))

def fetch_data():
    try:
        con = sqlite3.connect("contact.db")
        cursor = con.cursor()
        select_query = """SELECT * from contact;"""
        cursor.execute(select_query)
        data = cursor.fetchall()
        if len(data) != 0:
            table.delete(*table.get_children())
            for row in data:
                table.insert('',END,values=row)
            con.commit()
            con.close()
    except:
        pass

def update_data():
    if(fname.get()=="" or lname.get()=="" or evar.get()=="" or convar.get()=="" or addvar.get()==""):
       messagebox.showerror("Python","Fill All The Entry Fields")
    else:
        try:
            con = sqlite3.connect("contact.db")
            cursor = con.cursor()
            update_query = """UPDATE contact set fname=?,lname=?,email=?,contact=?,address=? WHERE fname=?;"""
            data_tuple = (fname.get(),lname.get(),evar.get(),convar.get(),addvar.get(),fname.get())
            cursor.execute(update_query,data_tuple)
            con.commit()
            con.close()
            messagebox.showinfo("Python","Contact Updated")
            fetch_data()
            clear_data()
        except sqlite3.Error as error:
            messagebox.showerror("Python","Error is :- "+ str(error))

root = Tk()
root.title(" Contact List ")
root.geometry("405x410")
root.resizable(0,0)
root.configure(background="Grey")

#==========VARIABLES=========#
fname = StringVar()
lname = StringVar()
evar = StringVar()
convar = StringVar()
addvar = StringVar()

#===========FRAMES===========#
title_form = Frame(root)
title_form.pack()

form = Frame(root, bg = "Grey")
form.pack()

#===========LABELS============#
title = Label(title_form , text = " Contact Management " , font = ('arial',16) , bg = "orange", width = 300)
title.pack(fill=X)

first_name = Label(form , text = "First Name :- " , font = ("arial",14) ,bd =4 , bg = "Grey", width = 10)
first_name.grid(row = 0 , sticky = W)

last_name = Label(form , text = "Last Name :- " , font = ("arial",14) , bd = 4 , bg = "Grey", width = 10)
last_name.grid(row = 1 , sticky = W)

email = Label(form , text = "Email Id :- " , font = ("arial",14) , bd = 4 , bg = "Grey" , width = 10)
email.grid(row = 2 , sticky = W)

contact = Label(form , text = "Contact No :- " , font = ("arial",14) , bd = 4 , bg = "Grey", width = 10)
contact.grid(row = 3 , sticky = W)

address = Label(form , text = "Address :- " , font = ("arial",14) , bd = 4 , bg = "Grey", width = 10)
address.grid(row = 4 , sticky = W)

#============ENTRY==============#
first = Entry(form , textvariable = fname , font = ("arial",14) , relief = SUNKEN ,bd=3)
first.grid(row = 0 , column = 1)

last = Entry(form , textvariable = lname , font = ("arial",14) , relief = SUNKEN ,bd=3)
last.grid(row = 1 , column = 1)

email1 = Entry(form , textvariable = evar , font = ("arial",14) , relief = SUNKEN ,bd=3)
email1.grid(row = 2 , column = 1)

contact1 = Entry(form , textvariable = convar , font = ("arial",14) , relief = SUNKEN ,bd=3)
contact1.grid(row = 3 , column = 1)

address1 = Entry(form , textvariable = addvar , font = ("arial",14) , relief = SUNKEN ,bd=3)
address1.grid(row = 4 , column = 1)

#===========BUTTONS==============#
btn_add = Button(form , text = "Save" , width = 10 , command = insert_data , bg = "Grey")
btn_add.grid(row = 6 , column = 0 , pady = 10)

btn_update = Button(form , text = "Update" , width = 10 , bg = "Grey" , command = update_data)
btn_update.place(x=110,y=170)

btn_exit = Button(form , text = "Exit" , width = 10 , command = exit , bg = "Grey")
btn_exit.place(x=200,y=170)

#===========VIEW THE DATA===========#
table = ttk.Treeview(root , columns = ("fname","lname","email","contact","address"))

table.heading("fname",text = "First Name")
table.heading("lname",text = "Last Name")
table.heading("email",text = "Email Id")
table.heading("contact",text = "Contact No")
table.heading("address",text = "Address")

table["show"] = 'headings'
table.column("fname",width=15)
table.column("lname",width=15)
table.column("email",width=25)
table.column("contact",width=10)
table.column("address",width=15)

table.place(x=0,y=250,width=410,height=160)

root.mainloop()
