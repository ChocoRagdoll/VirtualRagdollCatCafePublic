import os
import random
import tkinter as tk
from PIL import Image, ImageTk
import openai

BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
GREY = "#968b8a"
#path = "/Users/chengege/Downloads/"
openai.api_key = "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"


class ChatPage:
    def __init__(self, root):
        self.root = root

        self.create_chat_frame()
        
               
    def create_chat_frame(self):
        #background
        self.chat_frame = tk.Frame(self.root, bg=WHITE_PINK)
        self.chat_frame.pack(side=tk.BOTTOM)
        self.chat_frame.propagate(False)
        self.chat_frame.configure(width=1000, height=640)
        self.chatF_photo = ImageTk.PhotoImage(Image.open(self.file_path("chatF.png")).resize((1000, 640)))
        #path + "chatF.png"
        tk.Label(self.chat_frame, image=self.chatF_photo).pack()

        #chatbox
        self.chat_box = tk.Text(self.chat_frame,
                                font=("Calibri", 20),
                                bd=0,
                                height=16,
                                width=34)
        
        self.chat_box.place(x=45, y=190)
        self.chat_box.configure(state='disabled')
        self.chat_box.tag_configure(BROWN, foreground=BROWN)
        self.chat_box.tag_configure(GREY, foreground=GREY)
        
        #user entry
        self.user_input = tk.Entry(self.chat_frame,
                                   font=("Calibri", 16),
                                   bd=0,
                                   width=34)

        self.user_input.place(x=570, y=370)
        self.user_input.focus()
        self.user_input.bind('<Return>', self.on_enter)

        #chat button
        chat_image = Image.open(self.file_path("send.png"))
        #path + "send.png"
        chat_image = chat_image.resize((210, 70))
        self.chat_photo = ImageTk.PhotoImage(chat_image)
        
        self.submit_button = tk.Button(self.chat_frame,
                                       image=self.chat_photo,
                                       command=self.get_chat_response)

        self.submit_button.place(x=640, y=420)
    
    def get_chat_response(self):
        input_text = self.user_input.get()
        self.update_chat_box("YOU: " + input_text, BROWN)
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            max_tokens=40,
            n=1,
            stop=None,
            temperature=0.7
        )
        
        chat_response = response.choices[0].text.strip()
        self.update_chat_box("PET: " + chat_response, GREY)
        
        self.user_input.delete(0, tk.END)
    
    def on_enter(self, event):
        self.get_chat_response()
    
    def update_chat_box(self, message, color):
        self.chat_box.configure(state='normal')
        self.chat_box.insert(tk.END, message + "\n", color)
        self.chat_box.configure(state='disabled')
    
    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path

#ChatPage(tk.Tk())

    

    

    








