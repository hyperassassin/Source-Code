from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

def clear_data():
    form.set("")
    name.set("")
    course.set("")
    sem.set("")
    var.set("")
    email.set("")
    address.set("")
    contact.set("")

def insert_data():
    if (form.get()=="" or name.get()=="" or course.get()=="" or sem.get()=="" or var.get()=="" or email.get()=="" or address.get()=="" or contact.get()==""):
        messagebox.showerror("Python","Fill All The Entry Fields")
    else:
        try:
            con = sqlite3.connect("register_database.db")
            cursor = con.cursor()
            insert_query = """INSERT INTO register(form,name,course,sem,gender,email,address,contact)VALUES(?,?,?,?,?,?,?,?);"""
            data_tuple = (form.get(),name.get(),course.get(),sem.get(),var.get(),email.get(),address.get(),contact.get())
            cursor.execute(insert_query,data_tuple)
            con.commit()
            con.close()
            messagebox.showinfo("Python","Data Is Inserted")
            fetch_data()
            clear_data()
        except sqlite3.Error as error:
            messagebox.showerror("Python","Error is :- "+ str(error))

def update_data():
    if (form.get()=="" or name.get()=="" or course.get()=="" or sem.get()=="" or var.get()=="" or email.get()=="" or address.get()=="" or contact.get()==""):
        messagebox.showerror("Python","Fill All The Entry Fields")
    else:
        try:
            con = sqlite3.connect("register_database.db")
            cursor = con.cursor()
            update_query = """UPDATE register set form=?,name=?,course=?,sem=?,gender=?,email=?,address=?,contact=? WHERE form=?;"""
            data_tuple = (form.get(),name.get(),course.get(),sem.get(),var.get(),email.get(),address.get(),contact.get(),form.get())
            cursor.execute(update_query,data_tuple)
            con.commit()
            con.close()
            messagebox.showinfo("Python","Data Is Updated")
            fetch_data()
            clear_data()
        except sqlite3.Error as error:
            messagebox.showerror("Python","Error is :- "+  str(error))

def fetch_data():
    try:
        con = sqlite3.connect("register_database.db")
        cursor = con.cursor()
        select_query = """SELECT * from register;"""
        cursor.execute(select_query)
        data =cursor.fetchall()
        if len(data) != 0:
            table.delete(*table.get_children())
            for row in data:
                table.insert('',END,values=row)
            con.commit()
            con.close()
    except:
        pass

root = Tk()
root.title(" Registration Form ")
root.geometry("470x460")
root.resizable(0,0)
root.configure(background = "Salmon")

#-------------Variables-------------#
form = IntVar()
form.set("")
name = StringVar()
course = StringVar()
sem = StringVar()
email = StringVar()
address = StringVar()
contact = IntVar()
contact.set("")

#---------------------Labels------------------------#
form1 = Label(root,text = " Form No :- ",bg="Salmon").grid(row = 0 , column = 0 , padx = 5 , pady = 5)
name1 = Label(root,text = " Name :- ",bg="Salmon").grid(row = 1 , column = 0, padx = 5 , pady = 5)
course1 = Label(root,text = " Course :- ",bg="Salmon").grid(row = 2 , column = 0, padx = 5 , pady = 5)
sem1 = Label(root,text = " Semester :- ",bg="Salmon").grid(row = 3 , column = 0, padx = 5 , pady = 5)
gender1 = Label(root,text = " Gender :- ",bg="Salmon").grid(row = 4 , column = 0, padx = 5 , pady = 5)
email1 = Label(root,text = " Email  Id :- ",bg="Salmon").grid(row = 6 , column = 0, padx = 5 , pady = 5)
address1 = Label(root,text = " Address :- ",bg="Salmon").grid(row = 7 , column = 0, padx = 5 , pady = 5)
contact1 = Label(root,text = " Contact No :- ",bg="Salmon").grid(row = 8 , column = 0, padx = 5 , pady = 5)

#--------------------Entry--------------------#
form_field = Entry(root , textvariable = form)
form_field.grid(row = 0 , column = 1)

name_field = Entry(root , textvariable = name)
name_field.grid(row = 1 , column = 1)

course_field = Entry(root , textvariable = course)
course_field.grid(row = 2 , column = 1)

sem_field = Entry(root , textvariable = sem)
sem_field.grid(row = 3 , column = 1)

email_field = Entry(root , textvariable = email)
email_field.grid(row = 6 , column = 1)

address_field = Entry(root , textvariable = address)
address_field.grid(row = 7 , column = 1)
                   
contact_field = Entry(root , textvariable = contact)
contact_field.grid(row = 8 , column = 1)

#--------------------Button--------------------#
submit = Button(root , text = " Insert Data ", bg="Salmon" , command = insert_data).grid(row = 9 , column = 0 , padx = 5 , pady = 5)
update = Button(root , text = " Update Data ", bg="Salmon" , command = update_data).grid(row = 9 , column = 1 , padx = 5 , pady = 5)

#---Variables---#
var = StringVar()
var1 = StringVar()
var2 = IntVar()
var2.set("")
var3 = IntVar()
var3.set("")

table = ttk.Treeview(root , columns = ("form","name","course","sem","gender","email","address","contact"))

table.heading("form",text="Form No")
table.heading("name",text="Name")
table.heading("course",text="Course")
table.heading("sem",text="Sem")
table.heading("gender",text="Gender")
table.heading("email",text="Email")
table.heading("address",text="Address")
table.heading("contact",text="Contact")

table["show"] = 'headings'
table.column("form",width=5)
table.column("name",width=15)
table.column("course",width=10)
table.column("sem",width=10)
table.column("gender",width=10)
table.column("email",width=25)
table.column("address",width=15)
table.column("contact",width=15)

table.place(x=0,y=300,width=470,height=160)
fetch_data()

#---------------------------Combobox------------------------------#
combo =ttk.Combobox(root,textvariable = var,width = 17)
combo['values'] = ("Male","Female","Other")
combo.grid(row = 4 , column = 1, padx = 5 , pady = 5)

root.mainloop()
