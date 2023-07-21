import os
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from petexperience import PetExperience

BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
GREY = "#968b8a"
#path = "C:/Chrome Downloads/assets/"
user = "root"
#password = "20020208Xs"
#password = "ABC200104.0090u"

class TodoPage:
    def __init__(self, root, pet_experience, username, password):
        self.root = root
        self.pet_experience = pet_experience
        # user id
        self.current_user_id = 0
        # current task list
        self.current_task_list = []

        # start
        self.init_data()
        self.create_todo_frame()

        # login in 
        self.login_user(username, password)
        # update
        self.update_task_list()
        self.create_history_frame()

    def create_todo_frame(self):
        self.todo_frame = Frame(self.root, bg=WHITE_PINK)
        self.todo_frame.pack(side=BOTTOM)
        self.todo_frame.propagate(False)
        self.todo_frame.configure(width=1000, height=640)

        self.todoF_photo = ImageTk.PhotoImage(Image.open(self.file_path("todoF.png")).resize((1000, 640)))
        # path + "todoF.png"
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

        # add button
        add_image = Image.open(self.file_path("add.png"))
        # path + "add.png"
        add_image = add_image.resize((160, 60))
        self.add_photo = ImageTk.PhotoImage(add_image)

        add_button = Button(self.todo_frame,
                            image=self.add_photo,
                            command=lambda: self.add_task()).place(x=570, y=430)

        # delete button
        delete_image = Image.open(self.file_path("delete.png"))
        # path + "delete.png"
        delete_image = delete_image.resize((160, 60))
        self.delete_photo = ImageTk.PhotoImage(delete_image)

        delete_button = Button(self.todo_frame,
                               image=self.delete_photo,
                               command=lambda: self.delete_task()).place(x=790, y=430)

        # complete button
        complete_image = Image.open(self.file_path("complete.png"))
        # path + "complete.png"
        complete_image = complete_image.resize((180, 50))
        self.complete_photo = ImageTk.PhotoImage(complete_image)

        complete_button = Button(self.todo_frame,
                                 image=self.complete_photo,
                                 command=lambda: self.mark_as_complete(self.task_box.get(ACTIVE))).place(x=560, y=530)

        # history button
        history_image = Image.open(self.file_path("history.png"))
        # path + "history.png"
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
        # path + "historyF.png"
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

        # back button
        back_image = Image.open(self.file_path("back.png"))
        # path + "back.png"
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

        self.completed_tasks_box.delete(0, END)

        self.match_task()
        # Insert completed tasks into the Listbox
        for d in self.current_task_list:
            if d[2] == 1:
                self.completed_tasks_box.insert(END, d[1])

    def init_data(self):
        db_config = {
            'user': 'sql6630612',
            'password': 'VptXF7SRQz',
            'host': 'sql6.freesqldatabase.com',
            'database': 'sql6630612',
            'raise_on_warnings': True
        }

        self.db = mysql.connector.connect(**db_config)
        cursor = self.db.cursor()
        self.db.commit()
    
    # login in using username and password
    def login_user(self, username, password):
        self.current_user_id = 0
        cursor = self.db.cursor()
        cursor.execute(f"select * from users")
        results = cursor.fetchall()
        for values in results:
            sql_username = values[2]
            sql_password = values[3]
            if sql_username == str(username) and sql_password == str(password):
                self.current_user_id = values[0]
                break
    

    # match task with user id
    def match_task(self):
        self.current_task_list.clear()
        cursor = self.db.cursor()
        cursor.execute(f"select * from tasks")
        results = cursor.fetchall()
        for values in results:
            if values[3] == self.current_user_id:
                self.current_task_list.append(values)
        print(self.current_task_list)

    # add tasks for this user
    def add_task(self):
        tasks = self.new_task.get(1.0, END)
        tasks = tasks[:-1]
        self.new_task.delete(1.0, END)
        cursor = self.db.cursor()
        sql = f"insert into tasks (task, userid) values (%s, %s)"
        cursor.execute(sql, (tasks, self.current_user_id))
        self.db.commit()

        # Refresh the task list or update the UI as needed
        self.update_task_list()

    # delete task for this user
    def delete_task(self):
        cursor = self.db.cursor()
        deleted = self.task_box.curselection()
        if len(deleted) <= 0:
            return
        look = self.task_box.get(deleted)
        # Remove task from MySQL database
        query = "DELETE FROM tasks WHERE task = %s and userid = %s"
        cursor.execute(query, (look, self.current_user_id))
        self.db.commit()
        self.task_box.delete(deleted)
        self.update_task_list()

    def mark_as_complete(self, task):
        cursor = self.db.cursor()
        query = "UPDATE tasks SET completed = 1 WHERE task = %s and userid = %s"
        cursor.execute(query, (task, self.current_user_id))
        self.db.commit()
        self.update_task_list()

        # add exp
        self.pet_experience.feed()

    def update_task_list(self):
        # Clear the current task list
        self.task_box.delete(0, END)
        self.match_task()
        # Iterate through the tasks and insert them into the task box
        for d in self.current_task_list:
            if d[2] == 0:
                self.task_box.insert(END, d[1])

    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path

#TodoPage(Tk(), PetExperience(), 123, 123)
      
