import random
import tkinter as tk
import pyautogui

x = 1400
progress = 0
status = 1
norm_num = [1, 2]
norm_to_rest_num = [3]
rest_num = [4, 5]
rest_to_norm = [6]
walk_left_num = [7, 8]
walk_right_num = [9, 10]
event_num = random.randrange(1,3,1)
impath = https://github.com/gege0430/VirtualRagdollCatcafe.git

window = tk.Tk()
window.config(highlightbackground = 'black')
label = tk.Label(window, bd = 0, bg = 'black')
window.overrideredirect(True)
window.wm_attributes('-transparent', True)

label.pack()
window.mainloop()

norm_images = []
for a in range(5):
    image = tk.PhotoImage(file = impath + 'norm.gif', format = 'gif -index %a')
    norm_imagines.append(image)

rest_images = []
for b in range(5):
    image = tk.PhotoImage(file = impath + 'rest.gif', format = 'gif -index %b')
    rest_images.append(image)

norm_to_rest_images = []
for c in range(5):
    image = tk.PhotoImage(file = impath + 'norm_to_rest.gif', format = 'gif -index %c')
    norm_to_rest_images.append(image)

rest_to_norm_images = []
for d in range(5):
    image = tk.PhotoImage(file = impath + 'rest_to_norm.gif', format = 'gif -index %d')
    rest_to_norm_images.append(image)

walk_left_images = []
for e in range(5):
    image = tk.PhotoImage(file = impath + 'walk_left.gif', format = 'gif -index %e')
    walk_left_images.append(image)

walk_right_images = []
for f in range(5):
    image = tk.PhotoImage(file = impath + 'walk_right.gif', format = 'gif -index %f')
    walk_right_images.append(image)


def gif_work(progress, frames, event_num, first_num, last_num):
    if progress < len(frames) -1:
        progress += 1
    else:
        progress = 0
        event_num = random.randrange(first_num, last_num, 1)
    return progress, event_num

#change event
def change_event(progress, status, event_num, x):
    #norm
    if status == 0:
        frame = norm_images[progress]
        progress ,event_num = gif_work(progress, norm_images, event_num, 1, 11)

    #norm to rest
    elif status == 1:
        frame = norm_to_rest_images[progress]
        progress ,event_num = gif_work(progress, norm_to_rest_images, event_num, 4, 6)
        
    #rest
    elif status == 2:
        frame = rest_images[progress]
        progress ,event_num = gif_work(progress, rest_images, event_num, 4, 6)

    #rest to norm
    elif status == 3:
        frame = rest_to_norm_images[progress]
        progress ,event_num = gif_work(progress, est_to_norm_images, event_num, 1, 3)

    #walk left
    elif status == 4:
        frame = walk_left_num[progress]
        progress, event_num = gif_work(progress, walk_left_num, event_num, 1, 11)
        x -= 3

    #walk right
    elif status == 5:
        frame = walk_right_num[progress]
        progress, event_num = gif_work(progress, walk_right_num, event_num, 1, 11)
        x -= -3
        window.geometry('100x100+' + str(x) + '+1050')
        label.configure(image = frame)
        window.after(1, event, progress, status, event_num, x)

#create event
def event(progress, status, event_num, x):
    if event_num in norm_num:
        status = 0
        print('norm')
        window.after(400, update, progress, event, event_num, x) 

    elif event_num in norm_to_rest_num:
        status = 1
        print('from norm to rest')
        window.after(100, update, progress, event, event_num, x) 

    elif event_num in rest_num:
        status = 2
        print('rest')
        window.after(1000, update, progress, event, event_num, x)

    elif event_num in rest_to_norm_num:
        status = 3
        print('from rest to norm')
        window.after(100, update, progress, event, event_num,x)
    
    elif event_num in walk_left_num:
        status = 4
        print('walking towards left')
        window.after(100, update, progress, event, event_num, x)

    elif event_num in walk_right_num:
        status = 5
        print('walking towards right')
        window.after(100, change_event, progress, event, event_num, x)
    

 
