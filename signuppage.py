import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from statusboard import StatusBoard
from main import VirtualRagdollCatcafe
from backloginpage import BackLoginPage

BABY_PINK = "#f8c6c7"
WHITE_PINK = "#faedf5"
LIGHT_PINK = "#fef3f4"
WHITE = "#fcfafb"
HOT_PINK = "#f37af5"
BROWN = "#9d6e6f"
GREY = "#968b8a"
PURPLE = "#aea1ba"
LIGHT_BROWN = "#cfb49f"
YELLOW = "#ffc331"


class SignupPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Signup Page")
        self.geometry("1000x700")

        self.create_signup_page()
    
    def create_signup_page(self):
         #set up background
        self.signupF_photo = ImageTk.PhotoImage(Image.open(self.file_path("SignupF.png")).resize((1000, 700)))
        tk.Label(self, image=self.signupF_photo).pack()

        #email label
        self.emailL = tk.Label(self,
                               text='Email',
                               font=('Microsoft Yeahei UI Light',20, 'bold'),
                               bg='white',
                               fg=BROWN)
        self.emailL.place(x=440,y=260)

        #email entry
        self.emailE = tk.Entry(self,
                               width=26,
                               font=('Microsoft Yeahei UI Light',22),
                               bd=0,
                               fg=PURPLE,
                               bg=LIGHT_PINK)
        self.emailE.place(x=440,y=290)

         #username label
        self.usernameL = tk.Label(self,
                                  text='Username',
                                  font=('Microsoft Yeahei UI Light',20, 'bold'),
                                  bg='white',
                                  fg=BROWN)
        self.usernameL.place(x=440,y=330)

        #username entry
        self.usernameE = tk.Entry(self,
                                  width=26,
                                  font=('Microsoft Yeahei UI Light',22),
                                  bd=0,
                                  fg=PURPLE,
                                  bg=LIGHT_PINK)
        self.usernameE.place(x=440,y=360)

        #password label
        self.passwordL = tk.Label(self,
                                  text='Password',
                                  font=('Microsoft Yeahei UI Light',20, 'bold'),
                                  bg='white',
                                  fg=BROWN)
        self.passwordL.place(x=440,y=400)

        #password entry
        self.passwordE = tk.Entry(self,
                                  width=26,
                                  font=('Microsoft Yeahei UI Light',22),
                                  bd=0,
                                  fg=PURPLE,
                                  bg=LIGHT_PINK)
        self.passwordE.place(x=440,y=430)

        #confirm password label
        self.confirmL = tk.Label(self,
                                 text='Confirm Password',
                                 font=('Microsoft Yeahei UI Light',20, 'bold'),
                                 bg='white',
                                 fg=BROWN)
        self.confirmL.place(x=440,y=470)

        #confirm password entry
        self.confirmE = tk.Entry(self,
                                 width=26,
                                 font=('Microsoft Yeahei UI Light',22),
                                 bd=0,
                                 fg=PURPLE,
                                 bg=LIGHT_PINK)
        self.confirmE.place(x=440,y=500)

        #sign up button
        signup_image = Image.open(self.file_path("signup.png"))

        signup_image = signup_image.resize((240, 80))
        self.signup_photo = ImageTk.PhotoImage(signup_image)

        signup_button = tk.Button(self,
                                  image=self.signup_photo,
                                  command=self.connect_database).place(x=520, y=540)

    
    def connect_database(self):
        if self.emailE.get()=='' or self.usernameE.get()=='' or self.passwordE.get()=='' or self.confirmE.get()=='':
            messagebox.showerror('Error', 'All Fields are Required!')
        elif self.passwordE.get() != self.confirmE.get():
            messagebox.showerror('Error', 'Passwords are not the Same!')
        else:
            try:
                self.config = {
                    'user': 'sql6630612',
                    'password': 'VptXF7SRQz',
                    'host': 'sql6.freesqldatabase.com',
                    'database': 'sql6630612',
                    'raise_on_warnings': True
                }
                self.connection = mysql.connector.connect(**self.config)
                self.cursor = self.connection.cursor()
            except:
                messagebox.showerror('Error', 'Cannot Connect to Database')

            add_query='INSERT INTO users(email, username, password) values (%s,%s,%s)'
            self.cursor.execute(add_query,(self.emailE.get(), self.usernameE.get(), self.passwordE.get()))
            self.connection.commit()
            self.connection.close()
            messagebox.showinfo('Success', 'New Account is Created!')
            self.clear()
            self.destroy()
            BackLoginPage()
            
    
    def clear(self):
        self.emailE.delete(0,tk.END)
        self.usernameE.delete(0,tk.END)
        self.passwordE.delete(0,tk.END)
        self.confirmE.delete(0,tk.END)


    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path

