from tkinter import *
from tkinter import messagebox
import random
import re
import time

class bill_app:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Billing System")
        self.root.resizable(0,0)
        title = Label(self.root,text = "BILLING SYSTEM",bd=12,relief=RIDGE,font=("times new roman",20),bg="#A569BD",fg="white").place(x = 0 , y = 0 , width = 1350)

        clock = Label(self.root,font = ("times new roman",17),bg="#A569BD",fg="white")
        clock.place(x = 1180 , y = 12)
        def clock_time():
            curr_time = time.strftime("%H:%M:%S")
            clock.config(text = "Time : " + curr_time)
            clock.after(200,clock_time)
        clock_time()

        date_lbl = Label(root , font = ("times new roman",17) , bg = "#A569BD" , fg = "white")
        date_lbl.place(x = 16 , y = 12)
        def date_time():
            curr_date = time.strftime("%d-%m-%Y")
            date_lbl.config(text = "Date : " + curr_date)
        date_time()

        #===================Variables=================#
        self.nutella = IntVar()
        self.noodles = IntVar()
        self.lays = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.nam = IntVar()
        self.atta = IntVar()
        self.pasta = IntVar()
        self.rice = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.dal = IntVar()
        self.tea = IntVar()
        self.soap = IntVar()
        self.shampoo = IntVar()
        self.body = IntVar()
        self.cream = IntVar()
        self.foam = IntVar()
        self.mask = IntVar()
        self.hand = IntVar()
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.contact = StringVar()
        self.billno = StringVar()
        
        #==================Customer Details Frame================#
        details = LabelFrame(self.root , text = "Customer Details" , font = ("times new roman",12) , bg = "#A569BD" , fg = "white" , relief = GROOVE , bd = 10)
        details.place(x=0,y=80,relwidth=1)

        cust_name = Label(details , text = "Customer Name" , font = ("times new roman",14) , bg = "#A569BD" , fg = "white").grid(row = 0 , column = 0 , padx = 15)
        cust_entry = Entry(details , borderwidth = 4 , width = 30 , textvariable = self.c_name).grid(row = 0 , column = 1 , pady = 4)

        cust_con = Label(details , text = "Contact No " , font = ("times new roman",14) , bg = "#A569BD" , fg = "white").grid(row = 0 , column = 2 , padx = 12)
        con_entry = Entry(details , borderwidth = 4 , width = 30 , textvariable = self.contact).grid(row = 0 , column = 3 , pady = 4)

        bill_no = Label(details , text = "Bill No " , font = ("times new roman",14) , bg = "#A569BD" , fg = "white").grid(row = 0 , column = 4 , padx = 13)
        bill_en = Entry(details , borderwidth = 4 , width = 30 , textvariable = self.billno , state = DISABLED).grid(row = 0 , column = 5 , pady = 4)
        
        #==================Snacks Frame================#
        snacks = LabelFrame(self.root , text = "Snacks" , font = ("Arial Black",12) , bg = "#E5B4F3" , fg = "#6C3483" , relief = GROOVE , bd = 10)
        snacks.place(x=5,y=180,height=380,width=325)

        item1=Label(snacks,text="Nutella Choco Spread",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.nutella).grid(row=0,column=1,padx=10)

        item2 = Label(snacks , text = "Noodles (1 Pack) " , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 1 , column = 0 , pady = 11)
        item2_entry = Entry(snacks , borderwidth = 2 , width = 15 , textvariable = self.noodles).grid(row = 1 , column = 1 , padx = 10)

        item3 = Label(snacks , text = "Chips (10 Rs) " , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 2 , column = 0 , pady = 11)
        item3_entry = Entry(snacks , borderwidth = 2 , width = 15 , textvariable = self.lays).grid(row = 2 , column = 1 , padx = 10)

        item4 = Label(snacks , text = "Biscuit (10 Rs) " , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 3 , column = 0 , pady = 11)
        item4_entry = Entry(snacks , borderwidth = 2 , width = 15 , textvariable = self.oreo).grid(row = 3 , column = 1 , padx = 10)

        item5 = Label(snacks , text = "Muffins " , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 4 , column = 0 , pady = 11)
        item5_entry = Entry(snacks , borderwidth = 2 , width = 15 , textvariable = self.muffin).grid(row = 4 , column = 1 , padx = 10)

        item6 = Label(snacks , text = "Chocolate " , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 5 , column = 0 , pady = 11)
        item6_entry = Entry(snacks , borderwidth = 2 , width = 15 , textvariable = self.silk).grid(row = 5 , column = 1 , padx = 10)

        item7 = Label(snacks , text = "Namkeen (15 Rs) " , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 6 , column = 0 , pady = 11)
        item7_entry = Entry(snacks , borderwidth = 2 , width = 15 , textvariable = self.nam).grid(row = 6 , column = 1 , padx = 10)

        #==================Grocery Frame================#
        grocery = LabelFrame(self.root , text = "Grocery" , font = ("Arial Black",12) , bg = "#E5B4F3" , fg = "#6C3483" , relief = GROOVE , bd = 10)
        grocery.place(x=340,y=180,height=380,width=325)

        item8 = Label(grocery , text = "Aashirvaad Atta (10 kg)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 0 , column = 0 , pady = 11)
        item8_entry = Entry(grocery , borderwidth = 2 , width = 14 , textvariable = self.atta).grid(row = 0 , column = 1 , padx = 10)

        item9 = Label(grocery , text = "Pasta (1 kg)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 1 , column = 0 , pady = 11)
        item9_entry = Entry(grocery , borderwidth = 2 , width = 14 , textvariable = self.pasta).grid(row = 1 , column = 1 , padx = 10)

        item10 = Label(grocery , text = "Rice (5 kg)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 2 , column = 0 , pady = 11)
        item10_entry = Entry(grocery , borderwidth = 2 , width = 14 , textvariable = self.rice).grid(row = 2 , column = 1 , padx = 10)

        item11 = Label(grocery , text = "Oil (1 ltr)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 3 , column = 0 , pady = 11)
        item11_entry = Entry(grocery , borderwidth = 2 , width = 14 , textvariable = self.oil).grid(row = 3 , column = 1 , padx = 10)

        item12 = Label(grocery , text = "Sugar (1 kg)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 4 , column = 0 , pady = 11)
        item12_entry = Entry(grocery , borderwidth = 2 , width = 14 , textvariable = self.sugar).grid(row = 4 , column = 1 , padx = 10)

        item13 = Label(grocery , text = "Dal (1 kg)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 5 , column = 0 , pady = 11)
        item13_entry = Entry(grocery , borderwidth = 2 , width = 14 , textvariable = self.dal).grid(row = 5 , column = 1 , padx = 10)

        item14 = Label(grocery , text = "Tea Powder (1 kg)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 6 , column = 0 , pady = 11)
        item14_entry = Entry(grocery , borderwidth = 2 , width = 14 , textvariable = self.tea).grid(row = 6 , column = 1 , padx = 10)

        #=============Beauty & Hygine===============#
        hygine = LabelFrame(self.root , text = "Beauty & Hygine" , font = ("Arial Black",12) , relief = GROOVE , bd = 10 , bg = "#E5B4F3" , fg = "#6C3483")
        hygine.place(x=677,y=180,height=380,width=325)

        item15 = Label(hygine , text = "Bath Soap" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 0 , column = 0 , pady = 11)
        item15_entry = Entry(hygine , borderwidth = 2 , width = 15 , textvariable = self.soap).grid(row = 0 , column = 1 , padx = 10)

        item16 = Label(hygine , text = "Shampoo (650 ml)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 1 , column = 0 , pady = 11)
        item16_entry = Entry(hygine , borderwidth = 2 , width = 15 , textvariable = self.shampoo).grid(row = 1 , column = 1 , padx = 10)

        item17 = Label(hygine , text = "Body Lotion" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 2 , column = 0 , pady = 11)
        item17_entry = Entry(hygine , borderwidth = 2 , width = 15 , textvariable = self.body).grid(row = 2 , column = 1 , padx = 10)

        item18 = Label(hygine , text = "Face Cream" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 3 , column = 0 , pady = 11)
        item18_entry = Entry(hygine , borderwidth = 2 , width = 15 , textvariable = self.cream).grid(row = 3 , column = 1 , padx = 10)

        item19 = Label(hygine , text = "Shaving Foam" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 4 , column = 0 , pady = 11)
        item19_entry = Entry(hygine , borderwidth = 2 , width = 15 , textvariable = self.foam).grid(row = 4 , column = 1 , padx = 10)

        item20 = Label(hygine , text = "Mask (1 piece)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 5 , column = 0 , pady = 11)
        item20_entry = Entry(hygine , borderwidth = 2 , width = 15 , textvariable = self.mask).grid(row = 5 , column = 1 , padx = 10)

        item21 = Label(hygine , text = "Hand Sanitizer (100 ml)" , font = ("Arial Black",11) , bg = "#E5B4F3" , fg = "#6C3483").grid(row = 6 , column = 0 , pady = 11)
        item21_entry = Entry(hygine , borderwidth = 2 , width = 15 , textvariable = self.hand).grid(row = 6 , column = 1 , padx = 10)

        #==============Bill Area==============#
        billarea = Frame(self.root , bd = 10 , relief = GROOVE , bg = "#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)

        bill_title = Label(billarea , text = "Bill Area" , font = ("Arial Black",17) , bd = 7 , relief = GROOVE , bg = "#E5B4F3" , fg = "#6C3483").pack(fill = X)

        scrol_y = Scrollbar(billarea , orient = VERTICAL)
        self.txtarea = Text(billarea , yscrollcommand = scrol_y.set)
        scrol_y.pack(side = RIGHT , fill = Y)
        scrol_y.config(command = self.txtarea.yview)
        self.txtarea.pack(fill = BOTH , expand = 1)

        #===============Billing Menu===========#
        billing_menu = LabelFrame(self.root , text = "Billing Summary" , font = ("Arial Black",12) , relief = GROOVE , bd = 10 , bg = "#A569BD" , fg = "white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)

        total_snacks = Label(billing_menu , text = "Total Snacks Price" , font = ("Arial Black",11) , bg = "#A569BD" , fg = "white").grid(row = 0 , column = 0)
        total_snacks_entry = Entry(billing_menu , borderwidth = 2 , width = 30 , textvariable = self.total_sna).grid(row = 0 , column = 1 , padx = 10 , pady = 7)

        total_grocery = Label(billing_menu , text = "Total Grocery Price" , font = ("Arial Black",11) , bg = "#A569BD" , fg = "white").grid(row = 1 , column = 0)
        total_grocery_entry = Entry(billing_menu , borderwidth = 2 , width = 30 , textvariable = self.total_gro).grid(row = 1 , column = 1 , padx = 10 , pady = 7)

        total_hygine = Label(billing_menu , text = "Total Hygine Price" , font = ("Arial Black",11) , bg = "#A569BD" , fg = "white").grid(row = 2 , column = 0)
        total_hygine_entry = Entry(billing_menu , borderwidth = 2 , width = 30 , textvariable = self.total_hyg).grid(row = 2 , column = 1 , padx = 10 , pady = 7)

        tax_snacks = Label(billing_menu , text = "Snacks Tax" , font = ("Arial Black",11) , bg = "#A569BD" , fg = "white").grid(row = 0 , column = 2)
        tax_snacks_entry = Entry(billing_menu , borderwidth = 2 , width = 30 , textvariable = self.a).grid(row = 0 , column = 3 , padx = 10 , pady = 7)

        tax_grocery = Label(billing_menu , text = "Grocery Tax" , font = ("Arial Black",11) , bg = "#A569BD" , fg = "white").grid(row = 1 , column = 2)
        tax_grocery_entry = Entry(billing_menu , borderwidth = 2 , width = 30 , textvariable = self.b).grid(row = 1 , column = 3 , padx = 10 , pady = 7)

        tax_hygine = Label(billing_menu , text = "Hygine Tax" , font = ("Arial Black",11) , bg = "#A569BD" , fg = "white").grid(row = 2 , column = 2)
        tax_hygine_entry = Entry(billing_menu , borderwidth = 2 , width = 30 , textvariable = self.c).grid(row = 2 , column = 3 , padx = 10 , pady = 7)

        button_frame = Frame(billing_menu , bd = 7 , relief = GROOVE , bg = "#6C3483")
        button_frame.place(x=830,width=480,height=95)

        button_total = Button(button_frame , text = "Total Bill" , font = ("Arial Black",15) , bd = 5 , bg = "#E5B4F3" , fg = "#6C3483" , command = lambda:total(self)).grid(row = 0 , column = 0 , padx = 12 , pady = 13)
        button_clear = Button(button_frame , text = "Clear Field" , font = ("Arial Black",15) , bd = 5 , bg = "#E5B4F3" , fg = "#6C3483" , command = lambda:clear(self)).grid(row = 0 , column = 1 , padx = 10 , pady = 13)
        button_exit = Button(button_frame , text = "Exit" , font = ("Arial Black",15) , bd = 5 , bg = "#E5B4F3" , fg = "#6C3483" , width = 8 , command = lambda:exit1(self)).grid(row = 0 , column = 2 , padx = 10 , pady = 13)

        intro(self)

def total(self):
    regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',re.IGNORECASE)
    name = self.c_name.get()
    res = regex_name.search(name)

    regex_phone = re.compile("^[7-9]\d{9}$")
    phone = self.contact.get()
    res_phone = regex_phone.match(phone)

    if (self.c_name.get() == "" or self.contact.get() == ""):
        messagebox.showerror("Error","Fill All the Details")
    elif(res == None):
        messagebox.showerror("Error","Enter Valid Name")
    elif(res_phone == None):
        messagebox.showerror("Error","Invalid Contact Number")
    else:
        x = random.randint(1000,9999)
        self.billno.set(str(x))

        self.nu = self.nutella.get()*120     #Snacks Bill Amt
        self.no = self.noodles.get()*40
        self.la = self.lays.get()*10
        self.ore = self.oreo.get()*20
        self.mu = self.muffin.get()*30
        self.si = self.silk.get()*120
        self.na = self.nam.get()*25
        total_snacks_price = (self.nu + self.no + self.la + self.ore + self.mu + self.si + self.na)
        self.total_sna.set(str(total_snacks_price) + " Rs")
        self.a.set(str(round(total_snacks_price*0.05,3)) + " Rs")

        self.at = self.atta.get()*500        #Grocery Bill Amt
        self.pa = self.pasta.get()*120
        self.oi = self.oil.get()*120
        self.ri = self.rice.get()*160
        self.su = self.sugar.get()*40
        self.te = self.tea.get()*480
        self.da = self.dal.get()*80
        total_grocery_price = (self.at + self.pa + self.oi + self.ri + self.su + self.te + self.da)
        self.total_gro.set(str(total_grocery_price) + " Rs")
        self.b.set(str(round(total_grocery_price*0.01,3)) + " Rs")

        self.so = self.soap.get()*50
        self.sh = self.shampoo.get()*180
        self.cr = self.cream.get()*130
        self.lo = self.body.get()*500
        self.fo = self.foam.get()*90
        self.ma = self.mask.get()*50
        self.sa = self.hand.get()*50

        total_hygine_price = (self.so + self.sh + self.cr + self.lo + self.fo + self.ma + self.sa)
        self.total_hyg.set(str(total_hygine_price) + " Rs")
        self.c.set(str(round(total_hygine_price*0.10,3)) + " Rs")

        self.total_all_bill = (total_snacks_price + total_grocery_price + total_hygine_price + (round(total_grocery_price*0.01,3)) + (round(total_hygine_price*0.10,3)) + (round(total_snacks_price*0.05,3)))
        self.total_all_bil = str(self.total_all_bill) + " Rs"
        billarea(self)

def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO SUPER MARKET \n\t Phone-No. 7889234091")
    curr_time = time.strftime("%H:%M:%S")
    curr_date = time.strftime("%d-%m-%Y")
    self.txtarea.insert(END,"\n\nTime : "+curr_time +"\t\t  Date : " + curr_date + "\n")
    self.txtarea.insert(END,"\n====================================")
    self.txtarea.insert(END,f"\nBill No. : {self.billno.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No : {self.contact.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")

def billarea(self):
    intro(self)
    if self.nutella.get() != 0:
        self.txtarea.insert(END,f"Nutella\t\t {self.nutella.get()} \t {self.nu}\n")
    if self.noodles.get() != 0:
        self.txtarea.insert(END,f"Noodles\t\t {self.noodles.get()} \t {self.no}\n")
    if self.lays.get() != 0:
        self.txtarea.insert(END,f"Lays\t\t {self.lays.get()} \t {self.la}\n")
    if self.oreo.get() != 0:
        self.txtarea.insert(END,f"Oreo\t\t {self.oreo.get()} \t {self.ore}\n")
    if self.muffin.get() != 0:
        self.txtarea.insert(END,f"Muffins\t\t {self.muffin.get()} \t {self.mu}\n")
    if self.silk.get() != 0:
        self.txtarea.insert(END,f"Silk\t\t {self.silk.get()} \t {self.si}\n")
    if self.nam.get() != 0:
        self.txtarea.insert(END,f"Namkeen\t\t {self.nam.get()} \t {self.na}\n")
    if self.atta.get() != 0:
        self.txtarea.insert(END,f"Atta\t\t {self.atta.get()} \t {self.at}\n")
    if self.pasta.get() != 0:
        self.txtarea.insert(END,f"Pasta\t\t {self.pasta.get()} \t {self.pa}\n")
    if self.rice.get() != 0:
        self.txtarea.insert(END,f"Rice\t\t {self.rice.get()} \t {self.ri}\n")
    if self.oil.get() != 0:
        self.txtarea.insert(END,f"Oil\t\t {self.oil.get()} \t {self.oi}\n")
    if self.sugar.get() != 0:
        self.txtarea.insert(END,f"Sugar\t\t {self.sugar.get()} \t {self.su}\n")
    if self.dal.get() != 0:
        self.txtarea.insert(END,f"Dal\t\t {self.dal.get()} \t {self.da}\n")
    if self.tea.get() != 0:
        self.txtarea.insert(END,f"Tea\t\t {self.tea.get()} \t {self.te}\n")
    if self.soap.get() != 0:
        self.txtarea.insert(END,f"Soap\t\t {self.soap.get()} \t {self.so}\n")
    if self.shampoo.get() != 0:
        self.txtarea.insert(END,f"Shampoo\t\t {self.shampoo.get()} \t {self.sh}\n")
    if self.body.get() != 0:
        self.txtarea.insert(END,f"Lotion\t\t {self.body.get()} \t {self.lo}\n")
    if self.cream.get() != 0:
        self.txtarea.insert(END,f"Cream\t\t {self.cream.get()} \t {self.cr}\n")
    if self.foam.get() != 0:
        self.txtarea.insert(END,f"Foam\t\t {self.foam.get()} \t {self.fo}\n")
    if self.mask.get() != 0:
        self.txtarea.insert(END,f"Mask\t\t {self.mask.get()} \t {self.ma}\n")
    if self.hand.get() != 0:
        self.txtarea.insert(END,f"Sanitizer\t\t {self.hand.get()} \t {self.sa}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get() != "0.0 Rs":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get() != "0.0 Rs":
        self.txtarea.insert(END,f"Total Grocery Tax : {self.b.get()}\n")
    if self.c.get() != "0.0 Rs":
        self.txtarea.insert(END,f"Total Beauty&Hygine Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")

def clear(self):
    self.txtarea.delete(12.0,END)
    self.nutella.set(0)
    self.noodles.set(0)
    self.lays.set(0)
    self.oreo.set(0)
    self.muffin.set(0)
    self.silk.set(0)
    self.nam.set(0)
    self.atta.set(0)
    self.pasta.set(0)
    self.rice.set(0)
    self.oil.set(0)
    self.sugar.set(0)
    self.dal.set(0)
    self.tea.set(0)
    self.soap.set(0)
    self.shampoo.set(0)
    self.body.set(0)
    self.cream.set(0)
    self.foam.set(0)
    self.mask.set(0)
    self.hand.set(0)
    self.total_sna.set(0)
    self.total_gro.set(0)
    self.total_hyg.set(0)
    self.a.set(0)
    self.b.set(0)
    self.c.set(0)
    self.c_name.set("")
    self.billno.set("")
    self.contact.set("")

def exit1(self):
    self.root.destroy()

root = Tk()
obj = bill_app(root)
root.mainloop()
