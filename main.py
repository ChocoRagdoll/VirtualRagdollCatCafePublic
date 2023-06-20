import os
import random
import tkinter as tk
from PIL import Image, ImageTk

class VirtualRagdollCatcafe(tk.Toplevel):
    def __init__(self):
        super().__init__()
        
        
        
        self.x = 1400
        self.y = 500
        self.status = 1
        self.progress = 0
        self.tail_num = [1, 2]
        self.blink_num = [3, 4]
        self.upcoming1_num = [5, 6]
        self.upcoming2_num = [7, 8]
        self.upcoming3_num = [9, 10]
        self.upcoming4_num = [11, 12]
        self.event_num = random.randrange(1, 3, 1)
        self.assets_folder = os.path.join("assets")

        self.title("Virtual Ragdoll Catcafe")
        self.geometry(f'1024x1024+{self.x}+{self.y}')

        self.tail_images = self.create_images("tail40.gif")
        self.blink_images = self.create_images("blink50.gif")
        self.upcoming1_images = self.create_images("tail40.gif")
        self.upcoming2_images = self.create_images("blink50.gif")
        self.upcoming3_images = self.create_images("tail40.gif")
        self.upcoming4_images = self.create_images("blink50.gif")

        self.label = tk.Label(self, bd=0, bg='black')
        self.label.pack()  

        self.config(highlightbackground='black')
        self.overrideredirect(True)

        self.bind("<ButtonPress-1>", self.start_drag)
        self.bind("<B1-Motion>", self.drag)
        self.bind("<Configure>", self.resize)

        self.image = self.tail_images[0]  # Assign the initial image reference
        self.label.config(image=self.image)
        self.change_event(self.progress, self.status, self.event_num, self.x)

        self.mainloop()

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
        elif event_num in self.upcoming1_num:
            self.status = 2
            frames = self.upcoming1_images
            print('upcoming1')
        elif event_num in self.upcoming2_num:
            self.status = 3
            frames = self.upcoming2_images
            print('upcoming2')
        elif event_num in self.upcoming3_num:
            self.status = 4
            frames = self.upcoming3_images
            print('upcoming3')
        elif event_num in self.upcoming4_num:
            self.status = 5
            frames = self.upcoming4_images

        self.progress = self.gif_work(progress, frames)
        self.image = frames[self.progress]  # Assign the current image reference
        self.label.config(image=self.image)
        self.after(100, self.change_event, self.progress, self.status, self.event_num, self.x)


    def get_random_event_num(self):
        return random.randrange(1, 13, 1)

    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def drag(self, event):
        self.geometry(f"+{event.x_root - self.x}+{event.y_root - self.y}")

    def resize(self, event):
        width = event.width
        height = event.height
        self.geometry(f"{width}x{height}")



