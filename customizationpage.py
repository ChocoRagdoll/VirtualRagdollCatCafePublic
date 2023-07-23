import os
import tkinter as tk
from tkinter import Button, filedialog
from PIL import ImageTk, Image
# import mysql.connector


BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
LIGHT_PINK = "#fef3f4"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
GREY = "#968b8a"

class CustomizationPage:
    def __init__(self, main, cat_body):
        self.main = main
        self.cat_body = cat_body
        self.photo_images = []

        self.cust_page()
      

    def cust_page(self):
        self.cust_frame = tk.Frame(self.main, bg=WHITE_PINK)
        self.cust_frame.pack(side=tk.BOTTOM)
        self.cust_frame.propagate(False)
        self.cust_frame.configure(width=1000, height=640)
        lb5 = tk.Label(self.cust_frame,text = "CUSTOMIZATION", font=("Calibri", 30, "bold"))
        lb5.pack()

        
        tail_button = self.create_button("tail_cust.png", 1, 600, 400)
        blink_button = self.create_button("blink_cust.png", 2, 350, 200)
        walkl_button = self.create_button("walkl_cust.png", 3, 100, 200)
        walkr_button = self.create_button("walkr_cust.png", 4, 600, 200)
        fed_button = self.create_button("fed_cust.png", 5, 100, 400)
        headpat_button = self.create_button("headpat_cust.png", 6, 350, 400)
        
    def create_button(self, filename, n, x, y):
        image_1 = Image.open(self.file_path(filename))
        image_1 = image_1.resize((240, 90))
        self.photo_1 = ImageTk.PhotoImage(image_1)
        self.photo_images.append(self.photo_1)

        return Button(self.cust_frame,
                    image=self.photo_1,
                    command=lambda: self.upload_gif(n)).place(x=x, y=y)

    def upload_gif(self, n):
        # Open a file dialog and store the path to the selected file
        gif_path = filedialog.askopenfilename(filetypes=(("GIF files", "*.gif"), 
                                                         ("All files", "*.*")))
        if gif_path:
            # set the GIF
            self.cat_body.set_gif(gif_path, n)

        
    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path

