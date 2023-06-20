from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
path = "/Users/chengege/Downloads/"
user = "root"
password = "ABC200104.0090u"

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
        self.todoF_photo = ImageTk.PhotoImage(Image.open(path + "todoF.png").resize((1000, 640)))
        Label(self.todo_frame, image=self.todoF_photo).pack()

        # task box
        self.task_box = Listbox(self.todo_frame,
                                font=("Calibri", 40, "italic", "bold"),
                                height=8,
                                bd=0,
                                width=16)
        self.task_box.place(x=30, y=190)

        # new task
        self.new_task = Text(self.todo_frame,
                             font=("Calibri", 30, "bold"),
                             bd=0,
                             height=5,
                             width=18)

        self.new_task.place(x=560, y=200)

        btn_txt = (
            'History',
            'Add',
            'Delete',
            'Complete'
        )

        btn_command = (
            self.show_history,
            self.add_task,
            self.delete_task,
            lambda: self.mark_as_complete(self.task_box.get(ACTIVE))
        )

        for i in range(len(btn_txt)):
            Button(
                self.todo_frame,
                text=btn_txt[i],
                font=("Calibri", 40, "bold"),
                bd=0,
                height=1,
                width=10,
                bg=HOT_PINK,
                fg=WHITE,
                command=btn_command[i]
            ).place(x=600, y=320 + i * 100)

    def create_history_frame(self):
        self.history_frame = Frame(self.root, bg=WHITE_PINK)
        # history_frame.pack(side=tk.BOTTOM)
        self.history_frame.propagate(False)
        self.history_frame.configure(width=1000, height=640)
        Label(self.history_frame, image=self.todoF_photo).pack()

        # Create a Listbox to display the completed tasks
        self.completed_tasks_box = Listbox(
            self.history_frame,
            font=("Calibri", 40, "italic", "bold"),
            height=8,
            bd=0,
            width=16
        )
        self.completed_tasks_box.place(x=30, y=190)

        Button(
            self.history_frame,
            text="Back",
            font=("Calibri", 40, "bold"),
            bd=0,
            height=1,
            width=10,
            bg=HOT_PINK,
            fg=WHITE,
            command=self.go_back
        ).place(x=600, y=320)

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


        
