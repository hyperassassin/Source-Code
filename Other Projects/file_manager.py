from tkinter import *
from PIL import ImageTk, Image
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


def open_window():
    read = easygui.fileopenbox()
    return read

def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo("Confirmation","File Not Found !!!")

def copy_file():
    source1 = open_window()
    dest1 = filedialog.askdirectory()
    shutil.copy(source1,dest1)
    mb.showinfo("Confirmation","File Copied !!!")

def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
        mb.showinfo("Confirmation","File Deleted !!!")
    else:
        mb.showinfo("Confirmation","File Not Found !!!")

def rename_file():
    chFile = open_window()
    path1 = os.path.dirname(chFile)
    extend = os.path.splitext(chFile)[1]
    print("Enter new name for the chosen file")
    new = input()
    path = os.path.join(path1,new+extend)
    print(path)
    os.rename(chFile,path)
    mb.showinfo("Confirmation","File Renamed !!!")

def move_file():
    source = open_window()
    dest = filedialog.askdirectory()
    if(source == dest):
        mb.showinfo("Confirmation","Source and Destination are same")
    else:
        shutil.move(source,dest)
        mb.showinfo("Confirmation","File Moved !!!")

def make_folder():
    newFold = filedialog.askdirectory()
    print("Enter name of new folder")
    new = input()
    path = os.path.join(newFold,new)
    os.mkdir(path)
    mb.showinfo("Confirmation","Folder Created !!!")

def remove_folder():
    delFold = filedialog.askdirectory()
    os.rmdir(delFold)
    mb.showinfo("Confirmation","Folder Deleted !!!")

def list_files():
    folderList = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderList))
    i = 0
    print("Files in ",folderList," folder are :- ")
    while(i < len(sortlist)):
        print(sortlist[i] + '\n')
        i += 1

root = Tk()
root.geometry("490x300")
root.title(" File Manager In Python !!! ")
root.configure(background="Salmon")

l1 = Label(root , text = " File Manager " , font=("Helvetica",16), fg = "blue" , bg = "Salmon")
l1.grid(row = 0 , column = 1)

b1 = Button(root , text = " Open a File " , font=("Helvetica",10 ,"bold") , width = 20 , command = open_file)
b1.grid(row = 1 , column = 0)

b2 = Button(root , text = " Copy a File " , font=("Helvetica",10 ,"bold") , width = 20 , command = copy_file)
b2.grid(row = 2 , column = 0)

b3 = Button(root , text = " Delete a File " , font=("Helvetica",10 ,"bold") , width = 20 , command = delete_file)
b3.grid(row = 3 , column = 0)

b4 = Button(root , text = " Rename a File " , font=("Helvetica",10 ,"bold") , width = 20 , command = rename_file)
b4.grid(row = 4 , column = 0)

b5 = Button(root , text = " Move a File " , font=("Helvetica",10 ,"bold") , width = 20 , command = move_file)
b5.grid(row = 1 , column = 2)

b6 = Button(root , text = " Make a Folder " , font=("Helvetica",10 ,"bold") , width = 20 , command = make_folder)
b6.grid(row = 2 , column = 2)

b7 = Button(root , text = " Remove a Folder" , font=("Helvetica",10 ,"bold") , width = 20 , command = remove_folder)
b7.grid(row = 3 , column = 2)

b8 = Button(root , text = " List all Files in Directory " , font=("Helvetica",10 ,"bold") , width = 20 , command = list_files)
b8.grid(row = 4 , column = 2)

b9 = Button(root , text = "Exit " , font=("Helvetica",10 ,"bold") , width = 10 , command = exit)
b9.grid(row = 5 , column = 1)

root.mainloop()

