import os
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pickle


BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
GREY = "#968b8a"
#path = "/Users/chengege/Downloads/"

class HomePage:
    def __init__(self, root, pet_experience):
        self.root = root
        self.pet_experience = pet_experience

        self.create_home_frame()
        
        self.load_pet_data()
        
        self.update_ui()

        self.pet_experience.register_observer(self)
        
    def create_home_frame(self):
        #background
        self.home_frame = tk.Frame(self.root, bg=WHITE_PINK)
        self.home_frame.pack(side=tk.BOTTOM)
        self.home_frame.propagate(False)
        self.home_frame.configure(width=1000, height=640)
        self.homeF_photo = ImageTk.PhotoImage(Image.open(self.file_path("homeF.png")).resize((1000, 640)))
        tk.Label(self.home_frame, image=self.homeF_photo).pack()

        self.experience_bar = ttk.Progressbar(self.home_frame, length=200, mode="determinate")
        self.experience_bar.place(x=100,y=100)

         # Add two labels to display the current experience level and total experience points
        self.level_label = tk.Label(self.home_frame, text="Level: 1")
        self.level_label.place(x=100,y=200)
        
        self.total_exp_label = tk.Label(self.home_frame, text="Total Experience: 0")
        self.total_exp_label.place(x=150,y=200)
    
    def update_ui(self):
        current_level = self.pet_experience.current_level
        max_experience = self.pet_experience.experience_levels[current_level - 1]
        if current_level == 1:
            min_value = 0
        else:
            min_value = self.pet_experience.experience_levels[current_level - 2]

        normalized_value = (self.pet_experience.experience - min_value) / (max_experience - min_value)
        self.experience_bar["value"] = normalized_value * 100

        # Update the labels with the current experience level and total experience points
        self.level_label.config(text=f"Level: {self.pet_experience.current_level}")
        self.total_exp_label.config(text=f"Total Experience: {self.pet_experience.experience}")

    def load_pet_data(self):
        try:
            with open("pet_data.pkl", "rb") as file:
                pet_data = pickle.load(file)
            self.pet_experience.current_level = pet_data["current_level"]
            self.pet_experience.experience = pet_data["experience"]
        except FileNotFoundError:
            print("No saved pet data found. Starting with a new pet.")
    
    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path  
