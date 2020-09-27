from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

#-----------------------------------------Functions--------------------------------------------------------#
def save_data():
    if name.get()=="" or roll.get()=="" or course.get()=="" or age.get()=="" or dob.get()=="":
        messagebox.showerror("Python","Fill All The Entry Fields")
    else:
        try:
            conn = sqlite3.connect("student.db")
            cursor = conn.cursor()
            insert_query = """INSERT INTO details(name,roll,course,age,dob)VALUES(?,?,?,?,?);"""
            data_tuple = (name.get(),roll.get(),course.get(),age.get(),dob.get())
            cursor.execute(insert_query,data_tuple)
            conn.commit()
            conn.close()
            messagebox.showinfo("Python","Data Is Inserted")
            clear_data()
            fetch_data()
        except sqlite3.Error as error:
            messagebox.showerror("Python","Error is :- "+ str(error))

def update_data():
    try:
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        update_query = """UPDATE details set name=?,roll=?,course=?,age=?,dob=? WHERE roll=?;"""
        data = (name.get(),roll.get(),course.get(),age.get(),dob.get(),search.get())
        cursor.execute(update_query,data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Python","Data is Updated")
        clear_data()
        fetch_data()
        search1["text"] = " Search " 
    except sqlite3.Error as error:
        messagebox.showerror("Python","Error is :- " + str(error))

def delete_data():
    try:
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM details WHERE roll = " + search.get())
        conn.commit()
        conn.close()
        messagebox.showinfo("Python","Data is Deleted")
        x = table.get_children()
        for item in x:
            table.delete(item)
        fetch_data()
        clear_data()
        search1["text"] = " Search "
    except sqlite3.Error as error:
        messagebox.showerror("Python","Error is :- " + str(error))
        
def clear_data():
    name.set("")
    roll.set("")
    course.set("")
    age.set("")
    dob.set("")
    search.set("")

def search_data():
    condition = True
    if(condition):
        try:
            conn = sqlite3.connect("student.db")
            cursor = conn.cursor()
            search_query = "SELECT * from details where roll = " + str(search.get())
            cursor.execute(search_query)
            search_data = cursor.fetchone()
            conn.commit()
            cursor.close

            if search_data != None:
                table.delete(*table.get_children())
                table.insert('',END, values=search_data)
                condition = False
                search1['text'] = "SHOW ALL"
            else:
                messagebox.showerror("Python","No Such Data Exist")
        except sqlite3.Error as error:
            messagebox.showerror("Python","Error is :- " + str(error))
    else:
        conditon = True
        search1["text"] = " Search "
        fetch_data()

def fetch_data():
    try:
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        select_query = """SELECT * from details"""
        cursor.execute(select_query)
        data = cursor.fetchall()
        if len(data) != 0:
            table.delete(*table.get_children())
            for row in data:
                table.insert('',END,values=row)
            con.commit()
            cursor.close()
    except:
        pass

def get_cursor(event):
    cursor_row = table.focus()
    content = table.item(cursor_row)
    row = content['values']
    name.set(row[0])
    roll.set(row[1])
    course.set(row[2])
    age.set(row[3])
    dob.set(row[4])
    search.set(row[1])

#-----------------Main Frame----------------#
root = Tk()
root.title(" Student Management Project ")
root.geometry("430x385")
root.resizable(0,0)
root.configure(background = "grey")

#-------variables-------#
search = StringVar()
name = StringVar()
roll = IntVar()
roll.set("")
course = StringVar()
age = IntVar()
age.set("")
dob = StringVar()

#--------------------------------------------Labels-----------------------------------------------------------#
frame = LabelFrame(root , text = " Enter data here " , fg = "black" , bg = "salmon")
frame.place(x=0 , y=0 , width=300 , height=235)

name1 = Label(frame , text = " Name :- " , width = 15 , font = ('arial',10,'bold'), bg = "salmon")
name1.grid(row = 0 , column = 0 , ipadx=10 , ipady=10)

roll1 = Label(frame , text = " Roll No :- " , width = 15 , font = ('arial',10,'bold'), bg = "salmon")
roll1.grid(row = 1 , column = 0 , ipadx = 10 , ipady = 10)

course1 = Label(frame , text = " Course :- " , width =15 , font = ('arial',10,'bold'), bg = "salmon")
course1.grid(row = 2 , column = 0 , ipadx = 10 , ipady = 10)

age1 = Label(frame , text = " Age :- " , width = 15 , font = ('arial',10,'bold'), bg = "salmon")
age1.grid(row = 3 , column = 0 , ipadx = 10 , ipady = 10)

dob1 = Label(frame , text = " DOB :- ", width = 15 , font = ('arial',10,'bold'), bg = "salmon")
dob1.grid(row = 4 , column = 0, ipadx = 10 , ipady = 10)

#------------------------------------Entry Box-----------------------------------------#
e = Entry(frame , width = 20 , textvariable = name , bg = "salmon" , relief = SUNKEN)
e.grid(row = 0 , column = 1 , ipadx=10 , ipady=10)

e1 = Entry(frame , width = 20 , textvariable = roll , bg = "salmon" , relief = SUNKEN)
e1.grid(row = 1 , column = 1 , ipadx = 10 , ipady = 10)

e2 = Entry(frame , width = 20 , textvariable = course , bg = "salmon" , relief = SUNKEN)
e2.grid(row = 2 , column = 1 , ipadx = 10 , ipady = 10)

e3 = Entry(frame , width = 20 , textvariable = age , bg = "salmon" , relief = SUNKEN)
e3.grid(row = 3 , column = 1 , ipadx = 10 , ipady = 10)

e4 = Entry(frame , width = 20 , textvariable = dob , bg = "salmon" , relief = SUNKEN)
e4.grid(row = 4 , column = 1 , ipadx = 10 , ipady = 10)

#------------------------------------------Buttons-----------------------------------------------#
frame1 = LabelFrame(root , text = " Operations " , fg = "black" , bg = "salmon")
frame1.place(x=300 , y=0 , width=130 , height=235)

save = Button(frame1 , text = " Save " , width=9 , font = ('arial',10,'bold') , bd = 3 , command = save_data , bg = "salmon" , relief = RAISED)
save.grid(row = 0 , column = 2 ,ipadx = 10 , padx = 12 , pady = 4)

update = Button(frame1 , text = " Update " , width=9 , font = ('arial',10,'bold') , bd = 3 , bg = "salmon" , command = update_data)
update.grid(row = 1 , column = 2 ,ipadx = 10 , padx = 12 , pady = 4)

delete = Button(frame1 , text = " Delete " , width=9 , font = ('arial',10,'bold') , bd = 3 , bg = "salmon" , command = delete_data)
delete.grid(row = 2 , column = 2 ,ipadx = 10 , padx = 12 , pady = 4)

clear = Button(frame1 , text = " Clear " , width=9 , font = ('arial',10,'bold') , bg = "salmon" , bd = 3 , command = clear_data)
clear.grid(row = 3 , column = 2 ,ipadx = 10 , padx = 12 , pady = 4)

entry_search = Entry(frame1 , width = 10 , font = ('arial',10,'bold') , bd = 3 , textvariable = search , bg = "salmon" , relief = SUNKEN)
entry_search.grid(row = 4 , column = 2 , ipadx = 10 , padx = 12 , pady = 2)

search1 = Button(frame1 , text = " Search " , width=9 , font = ('arial',10,'bold') , bg = "salmon" , bd = 3 , command = search_data)
search1.grid(row = 5 , column = 2 ,ipadx = 10 , padx = 12 , pady = 4)

#---------------------------------Scrollbar-------------------------------------#
scroll = Scrollbar(root , orient=VERTICAL , bg="salmon" , bd=3)
scroll.place(x=410,y=235,height=150)

#---------------------------------------------------------View The Data-----------------------------------------------------------#
table = ttk.Treeview(root , columns =("name" , "roll" , "course" , "age" , "dob") , yscrollcommand = scroll.set)
scroll.config(command = table.yview)

table.heading("name",text = "Name")
table.heading("roll",text = "Roll No")
table.heading("course",text = "Course")
table.heading("age",text = "Age")
table.heading("dob",text = "D.O.B")

table["show"] = 'headings'
table.column("name",width=20)
table.column("roll",width=5)
table.column("course",width=10)
table.column("age",width=10)
table.column("dob",width=10)

table.place(x=0,y=235,width=410,height=150)
table.bind('<ButtonRelease-1>',get_cursor)
fetch_data()

root.mainloop()
