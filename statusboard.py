import tkinter as tk
from tkinter import ttk, messagebox
import googletrans as gt
import textblob as tb
from PIL import ImageTk, Image

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
        self.image_label = tk.Label(self, image=self.open_photo)
        self.image_label.pack()


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
        self.todoF_photo = None
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
        todo_frame = tk.Frame(self.main, bg=WHITE_PINK)
        todo_frame.pack(side=tk.BOTTOM)
        todo_frame.propagate(False)
        todo_frame.configure(width=1000, height=640)
        todoF_image = Image.open(path + "todoF.png")
        todoF_image = todoF_image.resize((1000, 640))
        self.todoF_photo = ImageTk.PhotoImage(todoF_image)
        todoF_label = tk.Label(todo_frame, image=self.todoF_photo)
        todoF_label.pack()

        #task box
        task_box = tk.Listbox(todo_frame,
                        font=("Calibri", 40, "italic", "bold"),
                        height=8,
                        bd=0,
                        width=16)

        task_box.place(x=30, y=190)

        #new task
        new_task = tk.Text(todo_frame,
                        font=("Calibri", 30, "bold"),
                        bd=0,
                        height=5,
                        width=18)

        new_task.place(x=560, y=200)

        #add task function
        def add_task():
            tasks = new_task.get(1.0, tk.END)
            task_box.insert(tk.END, tasks)
            with open("tasks.txt", "a") as file:
                file.write(tasks)
                file.seek(0)
                file.close()
            new_task.delete(1.0, tk.END)

        #delete task function
        def delete_task():
            deleted = task_box.curselection()
            look = task_box.get(deleted)
            with open("tasks.txt", "r+") as file:
                new_file = file.readlines()
                file.seek(0)
                for line in new_file:
                    task = str(look)
                    if task not in line:
                        file.write(line)
                file.truncate()
            task_box.delete(deleted)

        with open("tasks.txt", "r") as f:
            read = f.readlines()
            for i in read:
                ready = i.split()
                task_box.insert(tk.END, ready)
            f.close()

        #add button
        add_button = tk.Button(todo_frame,
                               text = "Add",
                               font=("Calibri", 40, "bold"),
                               bd=0,
                               height=1,
                               width=10,
                               bg=HOT_PINK,
                               fg=WHITE,
                               command=add_task)

        add_button.place(x=600, y=420)

        #delete button
        delete_button = tk.Button(todo_frame,
                               text = "Delete",
                               font=("Calibri", 40, "bold"),
                               bd=0,
                               height=1,
                               width=10,
                               bg=HOT_PINK,
                               fg=WHITE,
                               command=delete_task)

        delete_button.place(x=600, y=520)
                                                                                         
 
    def chat_page(self):
        chat_frame = tk.Frame(self.main, bg=WHITE_PINK)
        chat_frame.pack(side=tk.BOTTOM)
        chat_frame.propagate(False)
        chat_frame.configure(width=1000, height=640)
        lb3 = tk.Label(chat_frame,text = "CHAT", font=("Calibri", 30, "bold"))
        lb3.pack()

    def translate_page(self):
        translate_frame = tk.Frame(self.main, bg=WHITE_PINK)
        translate_frame.pack(side=tk.BOTTOM)
        translate_frame.propagate(False)
        translate_frame.configure(width=1000, height=640)

        languages = gt.LANGUAGES
        lan_list = list(languages.values())

        #originial text
        original_text = tk.Text(translate_frame,
                             font=("Calibri", 20),
                             height=16,
                             width=30)

        original_text.place(x=30, y=20)
              
        #translated text
        translated_text = tk.Text(translate_frame,
                                  font=("Calibri", 20),
                                  height=16,
                                  width=30)

        translated_text.place(x=530, y=20)

        #original combobox
        original_combo = ttk.Combobox(translate_frame,
                                     width=30,
                                     value=lan_list)

        original_combo.current(1)
        original_combo.place(x=70, y=430)

        #translated combobox
        translated_combo = ttk.Combobox(translate_frame,
                                        width=30,
                                        value=lan_list)

        translated_combo.current(1)
        translated_combo.place(x=570, y=430)

        #clear button
        clear_button = tk.Button(translate_frame,
                                 text="Clear",
                                 font=("Calibri", 40, "bold"),
                                 bd=0,
                                 bg=HOT_PINK,
                                 fg=WHITE,
                                 command=lambda: clear())

        clear_button.place(x=400, y=550)

        #translate button
        translate_button = tk.Button(translate_frame,
                                     text = "Translate",
                                     font=("Calibri", 40, "bold"),
                                     bd=0,
                                     bg=HOT_PINK,
                                     fg=WHITE,
                                     command=lambda: translate())

        translate_button.place(x=360, y=480)

        #translate function
        def translate():
            translated_text.delete(1.0, tk.END)
            try:
                for key, value in languages.items():
                    if (value == original_combo.get()):
                        from_language = key

                for key, value in languages.items():
                    if (value == translated_combo.get()):
                        to_language = key

                text = tb.TextBlob(original_text.get(1.0, tk.END))
                text = text.translate(from_lang=from_language, to=to_language)
                translated_text.insert(1.0, text)
            except Exception as e:
                messagebox.showerror("Translator", e)


        #clear function
        def clear():
            original_text.delete(1.0, tk.END)
            translated_text.delete(1.0, tk.END)

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
