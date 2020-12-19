import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
    root = Tk()
    width = 500
    height = 700
    text_area = Text(root)
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff = 0)
    edit_menu = Menu(menu_bar, tearoff = 0)
    help_menu = Menu(menu_bar, tearoff = 0)
    cmd_menu = Menu(menu_bar, tearoff = 0)
    #Add Scroll Bar
    scroll_bar = Scrollbar(text_area)
    file = None

    def __init__(self,**kwargs):
        try:
            self.root.wm_iconbitmap("note.ico")
        except:
            pass
        try:
            self.width = kwargs['width']
        except KeyError:
            pass
        try:
            self.height = kwargs['height']
        except KeyError:
            pass
        self.root.title("Untitled-Notepad")
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        left = (screenwidth / 2) - (self.width / 2)
        top = (screenheight / 2) - (self.height / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.width , self.height , left , top))
        self.root.grid_rowconfigure(0 , weight = 1)
        self.root.grid_columnconfigure(0 , weight = 1)
        self.text_area.grid(sticky = N + E + S + W)

        #For File Menu
        self.file_menu.add_command(label = "New" , command = self.newFile)
        self.file_menu.add_command(label = "Open" , command = self.openFile)
        self.file_menu.add_command(label = "Save" , command = self.saveFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit" , command = self.quit_app)
        self.menu_bar.add_cascade(label = "File" , menu = self.file_menu)

        #For Edit Menu
        self.edit_menu.add_command(label = "Cut" , command = self.cut)
        self.edit_menu.add_command(label = "Copy" , command = self.copy)
        self.edit_menu.add_command(label = "Paste" , command = self.paste)
        self.menu_bar.add_cascade(label = "Edit" , menu = self.edit_menu)

        #For Help Menu
        self.help_menu.add_command(label = "About Notepad" , command = self.show_about)
        self.cmd_menu.add_command(label = "About Commands" , command = self.show_cmd)
        self.menu_bar.add_cascade(label = "Commands" , menu = self.cmd_menu)
        self.menu_bar.add_cascade(label = "Help" , menu = self.help_menu)

        self.root.config(menu = self.menu_bar)
        self.scroll_bar.pack(side = RIGHT , fill = Y)
        self.scroll_bar.config(command = self.text_area.yview)
        self.text_area.config(yscrollcommand = self.scroll_bar.set)

    def quit_app(self):
            self.root.destroy()

    def show_about(self):
            showinfo("About Notepad","Simple Text Editor Built Using Python 3.7")

    def show_cmd(self):
            showinfo("Notepad","Just Another TextPad \n Copyright \n with BSD license you can use it")
            
    def openFile(self):
            self.file = askopenfilename(defaultextension = ".txt" , filetypes = [("All Files" , "*.*") , ("Text Documents","*.txt")])
            if self.file == "":
                self.file = None
            else:
                self.root.title(os.path.basename(self.file) + " - Notepad")
                self.text_area.delete(1.0 , END)
                file = open(self.file , "r")
                self.text_area.insert(1.0 , file.read())
                file.close()

    def newFile(self):
            self.root.title("Untitled Notepad")
            self.file = None
            self.text_area.delete(1.0 , END)

    def saveFile(self):
            if self.file == None:
                self.file = asksaveasfilename(initialfile = 'Untitled.txt' , defaultextension = ".txt" , filetypes = [("All Files","*.*") , ("Text Documents","*.txt")])
                if self.file == "":
                    self.file = None
                else:
                    file = open(self.file , "w")
                    file.write(self.text_area.get(1.0 , END))
                    file.close()
                    self.root.title(os.path.basename(self.file) + " - Notepad")
            else:
                file = open(self.file , "w")
                file.write(self.text_area.get(1.0 , END))
                file.close()

    def cut(self):
            self.text_area.event_generate("<<Cut>>")

    def copy(self):
            self.text_area.event_generate("<<Copy>>")

    def paste(self):
            self.text_area.event_generate("<<Paste>>")

    def run(self):
            self.root.mainloop()

notepad = Notepad(width = 600 , height = 400)
notepad.run()

        
        
        
