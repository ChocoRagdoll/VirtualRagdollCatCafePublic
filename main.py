import random
import tkinter as tk
import pyautogui
from PIL import Image, ImageTk

#set up variables
x = 1400
y = 500
status = 1
progress = 0
tail_num = [1, 2]
blink_num = [3, 4]
upcoming1_num = [5, 6]
upcoming2_num = [7, 8]
upcoming3_num = [9, 10]
upcoming4_num = [11, 12]
event_num = random.randrange(1,3,1)
path = "C:/Chrome Downloads/"

#set up window
window = tk.Tk()
window.title("Virtual Ragdoll Catcafe") 
window.geometry('1024x1024+' + str(x) + "+" + str(y))

#create a list of frames
def create_images(str, frames):
    gif_path = path + str
    gif = Image.open(gif_path)
    
    for frame in range(gif.n_frames):
        gif.seek(frame)
        image = gif.convert("RGBA")  # Convert to RGBA to preserve transparency, if any
        image.save(f"frame_{frame}.png", "PNG")

    gif_images = []
    
    for frame in range(frames):
        image_file = f"frame_{frame}.png"
        image = ImageTk.PhotoImage(file=image_file)
        gif_images.append(image)

    return gif_images

#set up frames for each action
tail_images = create_images("tail40.gif", 40)
blink_images = create_images("blink50.gif", 50)
upcoming1_images = create_images("tail40.gif", 40)
upcoming2_images = create_images("blink50.gif", 50)
upcoming3_images = create_images("tail40.gif", 40)
upcoming4_images = create_images("blink50.gif", 50)

#track the initial position for dragging the pet
def start_drag(event):
    global x, y
    x = event.x
    y = event.y

#update the window position while dragging
def drag(event):
    global x, y
    window.geometry(f"+{event.x_root - x}+{event.y_root - y}")

# Bind the mouse events to the window
window.bind("<ButtonPress-1>", start_drag)
window.bind("<B1-Motion>", drag)

#make gif work
def gif_work(progress, frames, event_num):
    if progress < len(frames) -1:
        progress += 1
    else:
        progress = 0
        event_num = random.randrange(1, 13, 1)
    return progress, event_num

#change event
def change_event(progress, status, event_num, x):
    #default
    if status == 0:
        frame = tail_images[progress]
        progress, event_num = gif_work(progress, tail_images, event_num)

    #blink
    elif status == 1:
        frame = blink_images[progress]
        progress, event_num = gif_work(progress, blink_images, event_num)
        
    #upcoming1
    elif status == 2:
        frame = upcoming1_images[progress]
        progress, event_num = gif_work(progress, upcoming1_images, event_num)

    #upcoming2
    elif status == 3:
        frame = upcoming2_images[progress]
        progress, event_num = gif_work(progress, upcoming2_images, event_num)

    #upcoming3
    elif status == 4:
        frame = upcoming3_images[progress]
        progress, event_num = gif_work(progress, upcoming3_images, event_num)
        
    #upcoming4
    else:
        frame = upcoming4_images[progress]
        progress, event_num = gif_work(progress, upcoming4_images, event_num)
    
    label.configure(image = frame)
    window.after(1, create_event, progress, status, event_num, x)

#create event
def create_event(progress, status, event_num, x):
    if event_num in tail_num:
        status = 0
        print('tail')

    elif event_num in blink_num:
        status = 1
        print('blink')

    elif event_num in upcoming1_num:
        status = 2
        print('upcoming1')

    elif event_num in upcoming2_num:
        status = 3
        print('upcoming2')
    
    elif event_num in upcoming3_num:
        status = 4
        print('upcoming3')

    elif event_num in upcoming4_num:
        status = 5
        print('upcoming4')
    
    window.after(100, change_event, progress, status, event_num, x)
    
#create a label;
label = tk.Label(window, bd = 0, bg = 'black')
label.pack()  

window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

#loop and end program
window.after(1, change_event, progress, status, event_num, x)
window.mainloop() 
