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
window.config(highlightbackground = 'black')
window.overrideredirect(True)
window.wm_attributes('-transparent', True)

#set up label
label = tk.Label(window, bd = 0, bg = 'black')
label.pack()


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
    #norm
    if status == 0:
        frame = default_images[progress]
        progress ,event_num = gif_work(progress, default_images, event_num)

    #norm to rest
    elif status == 1:
        frame = blink_images[progress]
        progress ,event_num = gif_work(progress, blink_images, event_num)
        
    #rest
    elif status == 2:
        frame = upcoming1_images[progress]
        progress ,event_num = gif_work(progress, upcoming1_images, event_num)

    #rest to norm
    elif status == 3:
        frame = upcoming2_images[progress]
        progress ,event_num = gif_work(progress, upcoming2_images, event_num)

    #walk left
    elif status == 4:
        frame = upcoming3_images[progress]
        progress, event_num = gif_work(progress, upcoming3_images, event_num)
        x -= 3

    #walk right
    elif status == 5:
        frame = upcoming4_images[progress]
        progress, event_num = gif_work(progress, upcoming4_images, event_num)
        x -= -3
    
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
        print('from norm to rest')
        window.after(400, change_event, progress, event, event_num, x) 

    elif event_num in upcoming1_num:
        status = 2
        print('rest')
        window.after(400, change_event, progress, event, event_num, x)

    elif event_num in upcoming2_num:
        status = 3
        print('from rest to norm')
        window.after(400, change_event, progress, event, event_num,x)
    
    elif event_num in upcoming3_num:
        status = 4
        print('walking towards left')
        window.after(400, change_event, progress, event, event_num, x)

    elif event_num in upcoming4_num:
        status = 5
        print('walking towards right')
        window.after(400, change_event, progress, event, event_num, x)
    
# end program
window.mainloop()
