import os
import sys
import random
import pystray
import threading
import tkinter as tk
from PIL import Image, ImageTk
import send2trash
from tkinterdnd2 import DND_FILES, TkinterDnD
from statusboard import StatusBoard, ControlBar, Main, Functions
#from petexperience import PetExperience

class VirtualRagdollCatcafe(tk.Toplevel):
    def __init__(self, pet_experience):
        super().__init__()

        self.x = 700
        self.y = 50
        self.status = 1
        self.progress = 0
        self.tail_num = [1, 2]
        self.blink_num = [3, 4]
        self.walk_left_num = [5, 6, 9, 10]
        self.walk_right_num = [7, 8, 11, 12]
        self.fed_num = []
        self.headpat_num = []
        self.event_num = random.randrange(1, 3, 1)

        self.assets_folder = os.path.join("assets")
        self.title("Virtual Ragdoll Catcafe")
        self.geometry(f'1024x1024+{self.x}+{self.y}')
        self.offset_x = 0
        self.offset_y = 0

        self.tail_images = self.create_images("tail40.gif")
        self.blink_images = self.create_images("blink50.gif")
        self.walk_left_images = self.create_images("walk left 16 frames.gif")
        self.walk_right_images = self.create_images("walk right 16 frames.gif")
        self.fed_images = self.create_images("tail40.gif")
        self.headpat_images = self.create_images("blink50.gif")

        self.label = tk.Label(self, bd=0, bg='black')

        self.setup_drag_and_drop()
        self.icon_thread = threading.Thread(target=self.setup_system_tray, daemon=True)
        self.icon_thread.start()

        self.config(highlightbackground='black')
        self.overrideredirect(True)
        self.wm_attributes('-transparentcolor', 'black')
        self.label.pack() 

        self.bind("<ButtonPress-1>", self.start_drag)
        self.bind("<B1-Motion>", self.drag)
        self.bind("<Double-Button-1>", self.open_status_board)
        self.image = self.tail_images[0]  # Assign the initial image reference
        self.label.config(image=self.image)
        self.change_event(self.progress, self.status, self.event_num, self.x)
        
        self.pet_experience = pet_experience

        #self.mainloop()

    def create_images(self, filename):
        gif_path = os.path.join(self.assets_folder, filename)
        original_gif = Image.open(gif_path)
        frames = []
        try:
            while True:
                frames.append(original_gif.copy())
                original_gif.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass
        return [ImageTk.PhotoImage(frame) for frame in frames]
    
    def create_images_absolute(self, filepath):
        original_gif = Image.open(filepath)
        frames = []
        try:
            while True:
                frames.append(original_gif.copy())
                original_gif.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass
        return [ImageTk.PhotoImage(frame) for frame in frames]

    def gif_work(self, progress, frames):
        if progress < len(frames) - 1:
            progress += 1
        else:
            progress = 0
            self.event_num = self.get_random_event_num()
        return progress

    def change_event(self, progress, status, event_num, x):
        if event_num in self.tail_num:
            self.status = 0
            frames = self.tail_images
            print('tail')
        elif event_num in self.blink_num:
            self.status = 1
            frames = self.blink_images
            print('blink')
        elif event_num in self.walk_left_num:
            self.status = 2
            frames = self.walk_left_images
            self.x -= 10
            print('walk left')
        elif event_num in self.walk_right_num:
            self.status = 3
            frames = self.walk_right_images
            self.x += 10
            print('walk right')
        elif event_num in self.fed_num:
            self.status = 4
            frames = self.fed_images
            print('fed')
        elif event_num in self.headpat_num:
            self.status = 5
            frames = self.headpat_images
            print('headpat')

        self.progress = self.gif_work(progress, frames)
        self.image = frames[self.progress]  # Assign the current image reference
        self.label.config(image=self.image)
        self.geometry(f'1024x1024+{self.x}+{self.y}')
        self.after(100, self.change_event, self.progress, self.status, self.event_num, self.x)

    def get_random_event_num(self):
        return random.randrange(1, 13, 1)

    def setup_drag_and_drop(self):
        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind('<<Drop>>', self.drop)

    def drop(self, event):
        files = event.widget.tk.splitlist(event.data)
        for file in files:
            self.delete_file(file)
        self.pet_experience.feed()

    def delete_file(self, file_path):
        try:
            '''
            files = event.widget.tk.splitlist(event.data)
                for file in files:
                   self.delete_file(file)
            '''
            # put to recycle bin 
            normalized_path = os.path.normpath(file_path)
            send2trash.send2trash(normalized_path)
            print(f"File '{file_path}' put to recycle bin.")
        except OSError as e:
            print(f"Error deleting file '{file_path}': {e}")

    def open_status_board(self, event):
        # Create an instance of the status board window

        status_board = StatusBoard(self.pet_experience)

        self.status_board = StatusBoard(self.pet_experience, self)


        # Position the status board above the cat
        cat_position = self.cat_label.winfo_rootx(), self.cat_label.winfo_rooty()
        self.status_board.geometry(f"+{cat_position[0]}+{cat_position[1] - self.status_board.winfo_height()}")

    def start_drag(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

    def drag(self, event):
        self.x = event.x_root - self.offset_x
        self.y = event.y_root - self.offset_y
        self.geometry(f"+{self.x}+{self.y}")

    def resize(self, event):
        width = event.width
        height = event.height
        self.geometry(f"{width}x{height}")

    def reposition_cat(self):
        self.x = 700
        self.y = 50
        print("Repositioning cat...")

    def set_gif(self, filepath, n):
        if n == 1:
            self.tail_images = self.create_images_absolute(filepath)
        elif n == 2: 
            self.blink_images = self.create_images_absolute(filepath)
        elif n == 3:
            self.walk_left_images = self.create_images_absolute(filepath)
        elif n == 4:
            self.walk_right_images = self.create_images_absolute(filepath)
        elif n == 5:
            self.fed_images = self.create_images_absolute(filepath)
        elif n == 6:
            self.headpat_images = self.create_images_absolute(filepath)
    
    def setup_system_tray(self):
        def exit_action(icon, item):
            icon.stop()
            self.quit()
            os._exit(0)

        def reposition_action(icon, item):
            self.reposition_cat()

        # Use an existing .ico file for the icon
        icon_image = Image.open(self.file_path("icon.ico"))

        # Create a system tray icon with an 'Exit' option and a 'Recenter' option
        self.icon = pystray.Icon(
            "virtual_cat", 
            icon_image, 
            "Virtual Ragdoll Catcafe", 
            menu=pystray.Menu(
                pystray.MenuItem('Reposition', reposition_action),
                pystray.MenuItem('Exit', exit_action)
            )
        )

        self.icon.run()
    
    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path
    
'''
if __name__ == "__main__":
    root = TkinterDnD.Tk()
    root.withdraw()
    window = VirtualRagdollCatcafe(PetExperience())
    window.bind("<ButtonPress-1>", window.start_drag)
    window.bind("<B1-Motion>", window.drag)
    window.bind("<Configure>", window.resize)
    root.mainloop() 
    '''




        
        
        

        
