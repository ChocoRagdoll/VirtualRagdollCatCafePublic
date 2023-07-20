import os
import sys
import random
import tkinter as tk
from PIL import Image, ImageTk
import send2trash
from tkinterdnd2 import DND_FILES, TkinterDnD
from statusboard import StatusBoard, ControlBar, Main, Functions

class VirtualRagdollCatcafe(tk.Toplevel):
    def __init__(self):
        super().__init__()
        
        self.x = 700
        self.y = 50
        self.status = 1
        self.progress = 0
        self.tail_num = [1, 2]
        self.blink_num = [3, 4]
        self.walk_left_num = [5, 6]
        self.walk_right_num = [7, 8]
        self.upcoming3_num = [9, 10]
        self.upcoming4_num = [11, 12]
        self.event_num = random.randrange(1, 3, 1)
        self.assets_folder = os.path.join("assets")

        self.title("Virtual Ragdoll Catcafe")
        self.geometry(f'1024x1024+{self.x}+{self.y}')

        self.tail_images = self.create_images("tail40.gif")
        self.blink_images = self.create_images("blink50.gif")
        self.walk_left_images = self.create_images("walk left 16 frames.gif")
        self.walk_right_images = self.create_images("walk right 16 frames.gif")
        self.upcoming3_images = self.create_images("tail40.gif")
        self.upcoming4_images = self.create_images("blink50.gif")

        self.label = tk.Label(self, bd=0, bg='black')

        self.setup_drag_and_drop()

        self.config(highlightbackground='black')
        self.overrideredirect(True)
        self.wm_attributes('-transparentcolor', 'black')
        self.label.pack() 

        self.bind("<ButtonPress-1>", self.start_drag)
        self.bind("<B1-Motion>", self.drag)
        self.bind("<Configure>", self.resize)
        self.bind("<Double-Button-1>", self.open_status_board)

        self.image = self.tail_images[0]  # Assign the initial image reference
        self.label.config(image=self.image)
        self.change_event(self.progress, self.status, self.event_num, self.x)

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
            print('walk left')
        elif event_num in self.walk_right_num:
            self.status = 3
            frames = self.walk_right_images
            print('walk right')
        elif event_num in self.upcoming3_num:
            self.status = 4
            frames = self.upcoming3_images
            print('upcoming3')
        elif event_num in self.upcoming4_num:
            self.status = 5
            frames = self.upcoming4_images
            print('upcoming4')

        self.progress = self.gif_work(progress, frames)
        self.image = frames[self.progress]  # Assign the current image reference
        self.label.config(image=self.image)
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
        status_board = StatusBoard()

        # Position the status board above the cat
        cat_position = self.cat_label.winfo_rootx(), self.cat_label.winfo_rooty()
        status_board.geometry(f"+{cat_position[0]}+{cat_position[1] - status_board.winfo_height()}")

    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def drag(self, event):
        self.geometry(f"+{event.x_root - self.x}+{event.y_root - self.y}")

    def resize(self, event):
        width = event.width
        height = event.height
        self.geometry(f"{width}x{height}")


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    window = VirtualRagdollCatcafe()
    window.bind("<ButtonPress-1>", window.start_drag)
    window.bind("<B1-Motion>", window.drag)
    window.bind("<Configure>", window.resize)
    root.mainloop()   


#VirtualRagdollCatcafe()
