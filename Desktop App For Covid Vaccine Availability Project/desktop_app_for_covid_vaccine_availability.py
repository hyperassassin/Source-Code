from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pytz
import requests

software_version = "v1.1"
IST = pytz.timezone('Asia/Kolkata')

root = Tk()
root.geometry("700x480+400+200")
root.title(f"Vaccine Availability Checker {software_version}")
root.iconbitmap("syringe.ico")
root.resizable(0,0)
root.config(background = "#293241")

top_left_bg = "#5c4ce1"
top_right_bg = "#867ae9"

f1 = Frame(root , height = 120 , width = 180 , bg = top_left_bg , bd = 1 , relief = FLAT)
f1.place(x = 0 , y = 0)

f2 = Frame(root , height = 120 , width = 520 , bg = top_right_bg , bd = 1 , relief = FLAT)
f2.place(x = 180 , y = 0)

f3 = Frame(root , height = 30 , width = 700 , bg = "black" , bd = 1 , relief = RAISED)
f3.place(x = 0 , y = 120)

lbl_date = Label(text = "Current Date" , bg = top_left_bg , font = "Verdana 12 bold")
lbl_date.place(x = 20 , y = 40)

lbl_time = Label(text = "Current Time" , bg = top_left_bg , font = "Verdana 12")
lbl_time.place(x = 20 , y = 60)

lbl_pincode = Label(text = "Pincode" , bg = top_right_bg , font = "Verdana 11")
lbl_pincode.place(x = 220 , y = 15)

date_lbl = Label(text = "Date" , bg = top_right_bg , font = "Verdana 11")
date_lbl.place(x = 380 , y = 15)

lbl_dateformat = Label(text = "[dd-mm-yyyy]" , bg = top_right_bg , font = "Verdana 7")
lbl_dateformat.place(x = 420 , y = 18)

lbl_search_vac = Label(text = "Search \nAvailable Vaccine" , bg = top_right_bg , font = "Verdana 8")
lbl_search_vac.place(x = 570 , y = 70)

lbl_head_result = Label(text = " Status       \tCentre-Name\t              Age-Group    Vaccine       Dose_1     Dose_2     Total", bg = 'black', fg='white', font = 'Verdana 8 bold')
lbl_head_result.place(x = 10 , y =125)

pincode_txt_var = StringVar()
result_box_cent = Text(root , height = 20 , width = 30 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_cent.place(x = 75 , y = 152)

result_box_age = Text(root , height = 20 , width = 8 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_age.place(x = 330 , y = 152)

result_box_vacc = Text(root , height = 20 , width = 10 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_vacc.place(x = 400 , y = 152)

result_box_D1 = Text(root , height = 20 , width = 7 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_D1.place(x = 490 , y = 152)

result_box_D2 = Text(root , height = 20 , width = 7 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_D2.place(x = 555 , y = 152)

result_box_D1_D2 = Text(root , height = 20 , width = 7 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_D1_D2.place(x = 630 , y = 152)

pincode_txtbox = Entry(root , width = 11 , bg = "#eaf2ae" , fg = "black" , textvariable = pincode_txt_var , font = "Verdana 11")
#pincode_txtbox['textvariable'] = pincode_txt_var
pincode_txtbox.place(x = 220 , y = 40)

date_txt_var = StringVar()
date_txtbox = Entry(root , width = 11 , bg = "#eaf2ae" , fg = "black" , textvariable = date_txt_var , font = "Verdana 10")
date_txtbox['textvariable'] = date_txt_var
date_txtbox.place(x = 380 , y = 40)

result_box_avl = Text(root , height = 20 , width = 8 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_avl.place(x = 3 , y = 152)

result_box_cent = Text(root , height = 20 , width = 30 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_cent.place(x = 75 , y = 152)

result_box_age = Text(root , height = 20 , width = 8 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_age.place(x = 330 , y = 152)

result_box_vacc = Text(root , height = 20 , width = 10 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_vacc.place(x = 400 , y = 152)

result_box_D1 = Text(root , height = 20 , width = 7 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_D1.place(x = 490 , y = 152)

result_box_D2 = Text(root , height = 20 , width = 7 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_D2.place(x = 555 , y = 152)

result_box_D1_D2 = Text(root , height = 20 , width = 7 , bg = "#293241" , fg = "#ecfcff" , relief = FLAT , font = "Verdana 10")
result_box_D1_D2.place(x = 630 , y = 152)

def fill_pincode_with_radio():
    curr_pincode = get_pincode_ip_service(url)
    pincode_txt_var.set(curr_pincode)

url = "https://ipinfo.io/postal"
def get_pincode_ip_service(url):
    response_pincode = requests.get(url).text
    return response_pincode

def update_clock():
    raw_TS = datetime.now(IST)
    date_now = raw_TS.strftime("%d %b %Y")
    time_now = raw_TS.strftime("%H:%M:%S %p")
    formatted_now = raw_TS.strftime("%d-%m-%Y")
    lbl_date.config(text = date_now)
    lbl_time.config(text = time_now)
    lbl_time.after(1000,update_clock)
    return formatted_now

def insert_today_date():
    formatted_now = update_clock()
    date_txt_var.set(formatted_now)

def refresh_api_call(PINCODE , DATE):
    header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
    request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={PINCODE}&date={DATE}"
    response = requests.get(request_link , headers = header)
    resp_JSON = response.json()
    return resp_JSON

def clear_boxes():
    result_box_avl.delete('1.0',END)
    result_box_cent.delete('1.0',END)
    result_box_age.delete('1.0',END)
    result_box_D1.delete('1.0',END)
    result_box_D2.delete('1.0',END)
    result_box_vacc.delete('1.0',END)
    result_box_D1_D2.delete('1.0',END)

def search_vaccine_avl():
    clear_boxes()
    PINCODE = pincode_txt_var.get()
    DATE = date_txt_var.get()
    resp_JSON = refresh_api_call(PINCODE,DATE)

    try:
        if len(resp_JSON['sessions']) == 0:
            messagebox.showinfo("INFO","Vaccine not yet arrived for the given date")
        for sess in resp_JSON['sessions']:
            age_limit = sess['min_age_limit']
            center_name = sess['name']
            pincode = sess['pincode']
            vaccine_name = sess['vaccine']
            avl_capacity = sess['available_capacity']
            qnty_dose1 = sess['available_capacity_dose1']
            qnty_dose2 = sess['available_capacity_dose2']
            slot_date = sess['date']

            if avl_capacity > 0:
                curr_status = 'Available'
            else:
                curr_status = 'NA'
            
            if age_limit == 45:
                age_grp = '45+'
            else:
                age_grp = '18-44'

            result_box_avl.insert(END,f"{curr_status:^6s}")
            result_box_avl.insert(END,"\n")
            result_box_cent.insert(END,f"{center_name:<30s}")
            result_box_cent.insert(END,"\n")
            result_box_age.insert(END,f"{age_grp:<6s}")
            result_box_age.insert(END,"\n")
            result_box_vacc.insert(END,f"{vaccine_name:<8s}")
            result_box_vacc.insert(END,"\n")
            result_box_D1.insert(END,f"{qnty_dose1:>5}")
            result_box_D1.insert(END,"\n")
            result_box_D2.insert(END,f"{qnty_dose2:>5}")
            result_box_D2.insert(END,"\n")
            result_box_D1_D2.insert(END,f"{avl_capacity:<5}")
            result_box_D1_D2.insert(END,"\n")
    except KeyError as KE:
        messagebox.showerror("ERROR","No Available Center(s) for the given pincode and date")
        print(pincode_txt_var.get())

search_vaccine_image = PhotoImage(file = "search.png")
search_vaccine_btn = Button(root , image = search_vaccine_image , bg = top_right_bg , command = search_vaccine_avl , relief = RAISED)
search_vaccine_btn.place(x = 600 , y = 25 , width = 37)

cur_loc_var = StringVar()
radio_location = Radiobutton(root , text = "Current Location" , bg = top_right_bg , variable = cur_loc_var , value = cur_loc_var , command = fill_pincode_with_radio)
radio_location.place(x = 215 , y = 65)

chkbox_today_var = IntVar()
today_date_chkbox = Checkbutton(root , text = "Today" , bg = top_right_bg , variable = chkbox_today_var , onvalue = 1 , offvalue = 0 , command = insert_today_date)
today_date_chkbox.place(x = 375 , y = 65)

update_clock()   
root.mainloop()