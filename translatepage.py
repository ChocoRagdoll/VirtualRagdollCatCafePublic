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
path = "/Users/chengege/Downloads/"

class TranslatePage:
    def __init__(self, root):
        self.root = root


        self.create_translate_frame()


    def create_translate_frame(self):
        self.translate_frame = tk.Frame(self.root, bg=WHITE_PINK)
        self.translate_frame.pack(side=tk.BOTTOM)
        self.translate_frame.propagate(False)
        self.translate_frame.configure(width=1000, height=640)

        self.translateF_photo = ImageTk.PhotoImage(Image.open(path + "translateF.png").resize((1000, 640)))
        tk.Label(self.translate_frame, image=self.translateF_photo).pack()

        

        languages = gt.LANGUAGES
        lan_list = list(languages.values())

        #originial text
        original_text = tk.Text(self.translate_frame,
                             font=("Calibri", 20),
                             height=9,
                             width=27)

        original_text.place(x=60, y=165)
              
        #translated text
        translated_text = tk.Text(self.translate_frame,
                                       font=("Calibri", 20),
                                       height=9,
                                       width=27)

        translated_text.place(x=560, y=165)

        #original combobox
        original_combo = ttk.Combobox(self.translate_frame,
                                       width=30,
                                       value=lan_list)

        original_combo.current(1)
        original_combo.place(x=80, y=460)

        #translated combobox
        translated_combo = ttk.Combobox(self.translate_frame,
                                         width=30,
                                         value=lan_list)

        translated_combo.current(1)
        translated_combo.place(x=580, y=460)

        #clear button
        clear_image = Image.open(path + "clear.png")
        clear_image = clear_image.resize((150, 50))
        self.clear_photo = ImageTk.PhotoImage(clear_image)
        
        clear_button = tk.Button(self.translate_frame,
                                   image=self.clear_photo,
                                   command=lambda: self.clear()).place(x=430, y=570)


        #translate button
        trans_image = Image.open(path + "trans.png")
        trans_image = trans_image.resize((240, 60))
        self.trans_photo = ImageTk.PhotoImage(trans_image)

        
        trans_button = tk.Button(self.translate_frame,
                                   image=self.trans_photo,
                                   command=lambda: self.translate()).place(x=380, y=500)

    #translate function
    def translate(self):
        translated_text.delete(1.0, tk.END)
        try:
            for key, value in languages.items():
                if (value == original_combo.get()):
                    from_language = key

            for key, value in languages.items():
                if (value == translated_combo.get()):
                    to_language = key

            text = tb.TextBlob(self.original_text.get(1.0, tk.END))
            text = text.translate(from_lang=from_language, to=to_language)
            translated_text.insert(1.0, text)
        except Exception as e:
            messagebox.showerror("Translator", e)

    #clear function
    def clear(self):
        original_text.delete(1.0, tk.END)
        translated_text.delete(1.0, tk.END)

#TranslatePage(tk.Tk())
