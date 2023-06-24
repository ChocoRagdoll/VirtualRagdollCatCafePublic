import os
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk, messagebox
import textblob as tb
import googletrans as gt



BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
GREY = "#968b8a"
#path = "C:/Chrome Downloads/assets/"

class TranslatePage:
    def __init__(self, root):
        self.root = root


        self.create_translate_frame()


    def create_translate_frame(self):
        self.translate_frame = tk.Frame(self.root, bg=WHITE_PINK)
        self.translate_frame.pack(side=tk.BOTTOM)
        self.translate_frame.propagate(False)
        self.translate_frame.configure(width=1000, height=640)

        self.translateF_photo = ImageTk.PhotoImage(Image.open(self.file_path("translateF.png")).resize((1000, 640)))
        #path + "translateF.png"
        tk.Label(self.translate_frame, image=self.translateF_photo).pack()

        

        self.languages = gt.LANGUAGES
        self.lan_list = list(self.languages.values())

        #originial text
        self.original_text = tk.Text(self.translate_frame,
                             font=("Calibri", 20),
                             height=9,
                             width=27)

        self.original_text.place(x=60, y=165)
              
        #translated text
        self.translated_text = tk.Text(self.translate_frame,
                                       font=("Calibri", 20),
                                       height=9,
                                       width=27)

        self.translated_text.place(x=560, y=165)

        #original combobox
        self.original_combo = ttk.Combobox(self.translate_frame,
                                       width=30,
                                       value=self.lan_list)

        self.original_combo.current(1)
        self.original_combo.place(x=80, y=460)

        #translated combobox
        self.translated_combo = ttk.Combobox(self.translate_frame,
                                         width=30,
                                         value=self.lan_list)

        self.translated_combo.current(1)
        self.translated_combo.place(x=580, y=460)

        #clear button
        clear_image = Image.open(self.file_path("clear.png"))
        #path + "clear.png"
        clear_image = clear_image.resize((150, 50))
        self.clear_photo = ImageTk.PhotoImage(clear_image)
        
        clear_button = tk.Button(self.translate_frame,
                                   image=self.clear_photo,
                                   command=lambda: self.clear()).place(x=430, y=570)


        #translate button
        trans_image = Image.open(self.file_path("trans.png"))
        #path + "trans.png"
        trans_image = trans_image.resize((240, 60))
        self.trans_photo = ImageTk.PhotoImage(trans_image)

        
        trans_button = tk.Button(self.translate_frame,
                                   image=self.trans_photo,
                                   command=lambda: self.translate()).place(x=380, y=500)

    #translate function
    def translate(self):
        self.translated_text.delete(1.0, tk.END)
        try:
            for key, value in self.languages.items():
                if (value == self.original_combo.get()):
                    from_language = key

            for key, value in self.languages.items():
                if (value == self.translated_combo.get()):
                    to_language = key

            text = tb.TextBlob(self.original_text.get(1.0, tk.END))
            text = text.translate(from_lang=from_language, to=to_language)
            self.translated_text.insert(1.0, text)
        except Exception as e:
            messagebox.showerror("Translator", e)

    #clear function
    def clear(self):
        self.original_text.delete(1.0, tk.END)
        self.translated_text.delete(1.0, tk.END)

    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path
        
    

#TranslatePage(tk.Tk())
