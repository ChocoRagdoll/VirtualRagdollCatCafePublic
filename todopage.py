import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
GREY = "#968b8a"

class TodoPage:
    def __init__(self, main):
        self.main = main

        self.todo_page()

    def todo_page(self):
        self.todo_frame = tk.Frame(self.main, bg=WHITE_PINK)
        self.todo_frame.pack(side=tk.BOTTOM)
        self.todo_frame.propagate(False)
        self.todo_frame.configure(width=1000, height=640)

        todoF_image = Image.open(self.file_path("todoF.png"))
        todoF_image = todoF_image.resize((1000, 640))
        self.todoF_photo = ImageTk.PhotoImage(todoF_image)
        todoF_label = tk.Label(self.todo_frame, image=self.todoF_photo)
        todoF_label.pack()

        #task box
        self.task_box = tk.Listbox(self.todo_frame,
                              font=("Calibri", 40, "italic", "bold"),
                              height=8,
                              bd=0,
                              width=16)

        self.task_box.place(x=30, y=200)

        #new task
        self.new_task = tk.Text(self.todo_frame,
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
                            command=lambda: self.add_task()).place(x=570, y=530)
        
        #delete button
        delete_image = Image.open(self.file_path("delete.png"))
        #path + "delete.png"
        delete_image = delete_image.resize((160, 60))
        self.delete_photo = ImageTk.PhotoImage(delete_image)
        
        delete_button = Button(self.todo_frame,
                               image=self.delete_photo,
                               command=lambda: self.delete_task()).place(x=790, y=530)
        
        with open("tasks.txt", "r") as f:
            read = f.readlines()
            for i in read:
                ready = i.split()
                self.task_box.insert(tk.END, ready)
            f.close()

    #add task function
    def add_task(self):
        tasks = self.new_task.get(1.0, tk.END)
        self.task_box.insert(tk.END, tasks)
        with open("tasks.txt", "a") as file:
            file.write(tasks)
            file.seek(0)
            file.close()
        self.new_task.delete(1.0, tk.END)

    #delete task function
    def delete_task(self):
        deleted = self.task_box.curselection()
        look = self.task_box.get(deleted[0])
        with open("tasks.txt", "r+") as file:
            new_file = file.readlines()
            file.seek(0)
            for line in new_file:
                if look.strip() not in line.strip():  # Partial match
                    file.write(line)
            file.truncate()
        self.task_box.delete(deleted)

    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path


# TodoPage(tk.Tk())

# Usage:
# todo_page = TodoPage(self.main)


'''
    #add task function
    def add_task(self):
        tasks = self.new_task.get(1.0, tk.END)
        self.task_box.insert(tk.END, tasks)
        with open("tasks.txt", "a") as file:
            file.write(tasks)
            file.seek(0)
            file.close()
        self.new_task.delete(1.0, tk.END)

    #delete task function
    def delete_task(self):
        deleted = self.task_box.curselection()
        look = self.task_box.get(deleted)
        with open("tasks.txt", "r+") as file:
            new_file = file.readlines()
            file.seek(0)
            for line in new_file:
                task = str(look)
                if task not in line:
                    file.write(line)
            file.truncate()
        self.task_box.delete(deleted)
       
    #add button
    add_button = tk.Button(todo_frame,
                            text="Add",
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
                                text="Delete",
                                font=("Calibri", 40, "bold"),
                                bd=0,
                                height=1,
                                width=10,
                                bg=HOT_PINK,
                                fg=WHITE,
                                command=delete_task)

    delete_button.place(x=600, y=520)
'''


