import os
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
GREY = "#968b8a"
#path = "C:/Chrome Downloads/assets/"
user = "root"
password = "20020208Xs"

class TodoPage:
    def __init__(self, root):
        self.root = root

        #start
        self.init_data()
        self.create_todo_frame()

        #update
        self.update_task_list()
        self.create_history_frame()

    def create_todo_frame(self):
        self.todo_frame = Frame(self.root, bg=WHITE_PINK)
        self.todo_frame.pack(side=BOTTOM)
        self.todo_frame.propagate(False)
        self.todo_frame.configure(width=1000, height=640)

        self.todoF_photo = ImageTk.PhotoImage(Image.open(self.file_path("todoF.png")).resize((1000, 640)))
        #path + "todoF.png"
        Label(self.todo_frame, image=self.todoF_photo).pack()

        # task box
        self.task_box = Listbox(self.todo_frame,
                                font=("Calibri", 40, "italic", "bold"),
                                height=8,
                                bd=0,
                                width=16)
        self.task_box.place(x=30, y=200)

        # new task
        self.new_task = Text(self.todo_frame,
                             font=("Calibri", 30, "bold"),
                             bd=0,
                             height=5,
                             width=18)

        self.new_task.place(x=560, y=220)

        #add button
        add_image = Image.open(self.file_path("add.png"))
        #path + "add.png"
        add_image = add_image.resize((160, 60))
        self.add_photo = ImageTk.PhotoImage(add_image)
        
        add_button = Button(self.todo_frame,
                            image=self.add_photo,
                            command=lambda: self.add_task()).place(x=570, y=430)

        #delete button
        delete_image = Image.open(self.file_path("delete.png"))
        #path + "delete.png"
        delete_image = delete_image.resize((160, 60))
        self.delete_photo = ImageTk.PhotoImage(delete_image)
        
        delete_button = Button(self.todo_frame,
                               image=self.delete_photo,
                               command=lambda: self.delete_task()).place(x=790, y=430)

        #complete button
        complete_image = Image.open(self.file_path("complete.png"))
        #path + "complete.png"
        complete_image = complete_image.resize((180, 50))
        self.complete_photo = ImageTk.PhotoImage(complete_image)
        
        complete_button = Button(self.todo_frame,
                                 image=self.complete_photo,
                                 command=lambda: self.mark_as_complete(self.task_box.get(ACTIVE))).place(x=560, y=530)

        #history button
        history_image = Image.open(self.file_path("history.png"))
        #path + "history.png"
        history_image = history_image.resize((180, 50))
        self.history_photo = ImageTk.PhotoImage(history_image)
        
        history_button = Button(self.todo_frame,
                                 image=self.history_photo,
                                 command=lambda: self.show_history()).place(x=780, y=530)


    def create_history_frame(self):
        self.history_frame = Frame(self.root, bg=WHITE_PINK)
        self.history_frame.propagate(False)
        self.history_frame.configure(width=1000, height=640)

        self.historyF_photo = ImageTk.PhotoImage(Image.open(self.file_path("historyF.png")).resize((1000, 640)))
        #path + "historyF.png"
        Label(self.history_frame, image=self.historyF_photo).pack()
        

        # Create a Listbox to display the completed tasks
        self.completed_tasks_box = Listbox(
            self.history_frame,
            font=("Calibri", 40, "italic", "bold"),
            height=9,
            bd=0,
            width=20
        )
        self.completed_tasks_box.place(x=50, y=140)

        #back button
        back_image = Image.open(self.file_path("back.png"))
        #path + "back.png"
        back_image = back_image.resize((240, 90))
        self.back_photo = ImageTk.PhotoImage(back_image)
        
        delete_button = Button(self.history_frame,
                               image=self.back_photo,
                               command=lambda: self.go_back()).place(x=670, y=510)

    def go_back(self):
        self.todo_frame.pack(side=BOTTOM)
        self.history_frame.pack_forget()

    def show_history(self):
        self.history_frame.pack(side=BOTTOM)
        self.todo_frame.pack_forget()

        cursor = self.db.cursor()
        cursor.execute('use tasks')

        # Query to retrieve completed tasks
        query = "SELECT task FROM tasks WHERE completed = 1"
        cursor.execute(query)

        # Fetch all the completed tasks
        completed_tasks = cursor.fetchall()

        self.completed_tasks_box.delete(0, END)

        # Insert completed tasks into the Listbox
        for task in completed_tasks:
            self.completed_tasks_box.insert(END, task[0])

    def init_data(self):
        db_config = {
            "host": "localhost",
            "user": user,
            "password": password,
            "database": "tasks",
        }

        self.db = mysql.connector.connect(**db_config)
        cursor = self.db.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            task VARCHAR(255) NOT NULL,
            completed BOOLEAN DEFAULT 0
        )
        """
        cursor.execute(create_table_query)
        self.db.commit()

    def add_task(self):
        tasks = self.new_task.get(1.0, END)
        self.new_task.delete(1.0, END)

        cursor = self.db.cursor()
        cursor.execute('use tasks')
        query = "INSERT INTO tasks (task) VALUES ('%s')" % tasks
        cursor.execute(query)
        self.db.commit()

        # Refresh the task list or update the UI as needed
        self.update_task_list()

    def delete_task(self):
        cursor = self.db.cursor()
        cursor.execute('use tasks')
        deleted = self.task_box.curselection()
        if len(deleted) <= 0:
            return
        look = self.task_box.get(deleted)

        # Remove task from MySQL database
        query = "DELETE FROM tasks WHERE task = %s"
        cursor.execute(query, (look,))
        self.db.commit()
        self.task_box.delete(deleted)
        self.update_task_list()

    def mark_as_complete(self, task):
        cursor = self.db.cursor()
        cursor.execute('use tasks')
        query = "UPDATE tasks SET completed = 1 WHERE task = %s"
        cursor.execute(query, (task,))
        self.db.commit()
        self.update_task_list()

    def update_task_list(self):
        # Clear the current task list
        self.task_box.delete(0, END)

        cursor = self.db.cursor()
        cursor.execute('use tasks')

        cursor.execute("SELECT task FROM tasks where completed = 0")
        tasks_0 = cursor.fetchall()
        # Iterate through the tasks and insert them into the task box
        for t in tasks_0:
            self.task_box.insert(END, t[0])

    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path


#TodoPage(Tk())
