import tkinter as tk
from tkinter import ttk, messagebox
import googletrans as gt
import textblob as tb
import os
import random
from PIL import ImageTk, Image
from todopage import TodoPage
from translatepage import TranslatePage
from main import VirtualRagdollCatcafe


BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
path = "/Users/chengege/Downloads/"

class StatusBoard(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Status Board")
        self.geometry("1000x700")

        #control bar
        self.control_bar = ControlBar(self)

        #main frame
        self.main = Main(self)
        
        #options Widge
        self.functions = Functions(self, self.control_bar, self.main)


        #run
        self.mainloop()
        

class ControlBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BABY_PINK)
        self.pack(side=tk.BOTTOM)
        self.pack_propagate(False)
        self.configure(width=1000, height=60)

class Main(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=WHITE_PINK)
        self.pack(side=tk.BOTTOM)
        self.pack_propagate(False)
        self.configure(width=1000, height=640)
        self.open_image = Image.open(path + "open_background.png")
        self.open_image = self.open_image.resize((1000, 640))
        self.open_photo = ImageTk.PhotoImage(self.open_image)
        tk.Label(self, image=self.open_photo).pack()


class Functions(tk.Frame):
    def __init__(self, parent, control_bar, main):
        super().__init__(parent)
        self.control_bar = control_bar
        self.main = main
        self.home_label = None
        self.todo_label = None
        self.chat_label = None
        self.translate_label = None
        self.cust_label = None
        self.home_photo = None
        self.todo_photo = None
        self.chat_photo = None
        self.translate_photo = None
        self.cust_photo = None
        self.translateF_photo = None
        self.trans_photo = None
        self.clear_photo = None
        self.create_tabs()

    def show_label(self, label, page):
        self.hide_label()
        label.config(bg=BROWN)
        self.delete_pages()
        page()

    def hide_label(self):
        if self.home_label:
            self.home_label.config(bg=BABY_PINK)
        if self.todo_label:
            self.todo_label.config(bg=BABY_PINK)
        if self.chat_label:
            self.chat_label.config(bg=BABY_PINK)
        if self.translate_label:
            self.translate_label.config(bg=BABY_PINK)
        if self.cust_label:
            self.cust_label.config(bg=BABY_PINK)
        

    def delete_pages(self):
        for frame in self.main.winfo_children():
            frame.destroy()
    
    def create_tabs(self):
        #home label
        self.home_label = tk.Label(self.control_bar, text = "", bg=BABY_PINK)
        self.home_label.place(x=15, y=50, width=116, height=5)

        #todo list label
        self.todo_label = tk.Label(self.control_bar, text = "", bg=BABY_PINK)
        self.todo_label.place(x=180, y=50, width=116, height=5)

        #chat label
        self.chat_label = tk.Label(self.control_bar, text = "", bg=BABY_PINK)
        self.chat_label.place(x=345, y=50, width=116, height=5)

        #translate label
        self.translate_label = tk.Label(self.control_bar, text = "", bg=BABY_PINK)
        self.translate_label.place(x=510, y=50, width=176, height=5)

        #customisation label
        self.cust_label = tk.Label(self.control_bar, text = "", bg=BABY_PINK)
        self.cust_label.place(x=730, y=50, width=186, height=5)

        #home button
        home_image = Image.open(path + "home.png")
        home_image = home_image.resize((110, 40))
        self.home_photo = ImageTk.PhotoImage(home_image)
        
        home_button = tk.Button(self.control_bar,
                                image=self.home_photo,
                                command=lambda: self.show_label(self.home_label, self.home_page))

        home_button.place(x=15, y=4)                        

        #todo list button
        todo_image = Image.open(path + "todo.png")
        todo_image = todo_image.resize((110, 40))
        self.todo_photo = ImageTk.PhotoImage(todo_image)
        
        todo_button = tk.Button(self.control_bar,
                                image=self.todo_photo,
                                command=lambda: self.show_label(self.todo_label, self.todo_page))

        todo_button.place(x=180, y=4)
        
        #chat button
        chat_image = Image.open(path + "chat.png")
        chat_image = chat_image.resize((110, 40))
        self.chat_photo = ImageTk.PhotoImage(chat_image)
        
        chat_button = tk.Button(self.control_bar,
                                image=self.chat_photo,
                                command=lambda: self.show_label(self.chat_label, self.chat_page))

        chat_button.place(x=345, y=4)

        #translate button
        translate_image = Image.open(path + "translate.png")
        translate_image = translate_image.resize((170, 40))
        self.translate_photo = ImageTk.PhotoImage(translate_image)
        
        translate_button = tk.Button(self.control_bar,
                                image=self.translate_photo,
                                command=lambda: self.show_label(self.translate_label, self.translate_page))

        translate_button.place(x=510, y=4)

        #customisation button
        cust_image = Image.open(path + "customisation.png")
        cust_image = cust_image.resize((180, 40))
        self.cust_photo = ImageTk.PhotoImage(cust_image)
        
        translate_button = tk.Button(self.control_bar,
                                image=self.cust_photo,
                                command=lambda: self.show_label(self.cust_label, self.cust_page))

        translate_button.place(x=730, y=4)

        

    def home_page(self):
        home_frame = tk.Frame(self.main, bg=WHITE_PINK)
        home_frame.pack(side=tk.BOTTOM)
        home_frame.propagate(False)
        home_frame.configure(width=1000, height=640)
        lb = tk.Label(home_frame,text = "HOME", font=("Calibri", 30, "bold"))
        lb.pack()

    #todo list page
    def todo_page(self):
        todo_page = TodoPage(self.main)
        
       
    #chat page                                                                                     
    def chat_page(self):
        chat_frame = tk.Frame(self.main, bg=WHITE_PINK)
        chat_frame.pack(side=tk.BOTTOM)
        chat_frame.propagate(False)
        chat_frame.configure(width=1000, height=640)
        lb3 = tk.Label(chat_frame,text = "CHAT", font=("Calibri", 30, "bold"))
        lb3.pack()

    #translate page
    def translate_page(self):
        translate_page = TranslatePage(self.main)
                       

    #customisation page
    def cust_page(self):
        cust_frame = tk.Frame(self.main, bg=WHITE_PINK)
        cust_frame.pack(side=tk.BOTTOM)
        cust_frame.propagate(False)
        cust_frame.configure(width=1000, height=640)
        lb5 = tk.Label(cust_frame,text = "CUST", font=("Calibri", 30, "bold"))
        lb5.pack()
                                        
        
        
                                  
                                     



      

if __name__ == "__main__":  
    StatusBoard()
