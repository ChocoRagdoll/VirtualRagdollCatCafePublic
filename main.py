import random
import tkinter as tk
import pyautogui

#set up variables
x = 1400
progress = 0
status = 1
default_num = [1, 2]
blink_num = [3, 4]
upcoming1_num = [5, 6]
upcoming2_num = [7, 8]
upcoming3_num = [9, 10]
upcoming4_num = [11, 12]
event_num = random.randrange(1,3,1)
path = "/Users/chengege/Downloads/"

#set up window
window = tk.Tk()
window.title("Virtual Ragdoll Catcafe") 

default_images = []
for a in range(15):
    image = tk.PhotoImage(file = path + "default.gif", format = f'gif -index {a}')
    default_images.append(image)

blink_images = []
for b in range(5):
    image = tk.PhotoImage(file = path + "blink.gif", format = f'gif -index {b}')
    blink_images.append(image)

upcoming1_images = []
for c in range(15):
    image = tk.PhotoImage(file = path + "default.gif", format = f'gif -index {c}')
    upcoming1_images.append(image)

upcoming2_images = []
for d in range(5):
    image = tk.PhotoImage(file = path + "blink.gif", format = f'gif -index {d}')
    upcoming2_images.append(image)

upcoming3_images = []
for e in range(15):
    image = tk.PhotoImage(file = path + "default.gif", format = f'gif -index {e}')
    upcoming3_images.append(image)

upcoming4_images = []
for f in range(5):
    image = tk.PhotoImage(file = path + "blink.gif", format = f'gif -index {f}')
    upcoming4_images.append(image)

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
        frame = default_images[progress]
        progress ,event_num = gif_work(progress, default_images, event_num)

    #blink
    elif status == 1:
        frame = blink_images[progress]
        progress ,event_num = gif_work(progress, blink_images, event_num)
        
    #upcoming1
    elif status == 2:
        frame = upcoming1_images[progress]
        progress ,event_num = gif_work(progress, upcoming1_images, event_num)

    #upcoming2
    elif status == 3:
        frame = upcoming2_images[progress]
        progress ,event_num = gif_work(progress, upcoming2_images, event_num)

    #upcoming3
    elif status == 4:
        frame = upcoming3_images[progress]
        progress, event_num = gif_work(progress, upcoming3_images, event_num)
        
    #upcoming4
    else:
        frame = upcoming4_images[progress]
        progress, event_num = gif_work(progress, upcoming4_images, event_num)
    
    window.geometry('100x100+' + str(x) + '+1050')
    label.configure(image = frame)
    window.after(1, event, progress, status, event_num, x)

#create event
def event(progress, status, event_num, x):
    if event_num in default_num:
        status = 0
        print('default')
        window.after(400, change_event, progress, event, event_num, x) 

    elif event_num in blink_num:
        status = 1
        print('blink')
        window.after(400, change_event, progress, event, event_num, x) 

    elif event_num in upcoming1_num:
        status = 2
        print('upcoming1')
        window.after(400, change_event, progress, event, event_num, x)

    elif event_num in upcoming2_num:
        status = 3
        print('upcoming2')
        window.after(400, change_event, progress, event, event_num, x)
    
    elif event_num in upcoming3_num:
        status = 4
        print('upcoming3')
        window.after(400, change_event, progress, event, event_num, x)

    elif event_num in upcoming4_num:
        status = 5
        print('upcoming4')
        window.after(400, change_event, progress, event, event_num, x)
    
#create a labe;
label = tk.Label(window, bd = 0, bg = 'black')
label.pack()  

#loop and end program
window.after(1, change_event, progress, status, event_num, x)
window.mainloop() 
