import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from userstatusboard import UserStatusBoard
from petexperience import PetExperience

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

class BackLoginPage(tk.Tk):
    def __init__(self, pet_experience):
        super().__init__()
        self.title("Login Page")
        self.geometry("1000x700")
        
        #pet experience
        self.pet_experience = pet_experience

        self.create_login_page()
        
    
    def create_login_page(self):
        #set up background
        self.loginF_photo = ImageTk.PhotoImage(Image.open(self.file_path("loginF.png")).resize((1000, 700)))
        tk.Label(self, image=self.loginF_photo).pack()

        #username entry
        self.usernameE = tk.Entry(self,
                                  width=17,
                                  font=('Microsoft Yeahei UI Light',30),
                                  bd=0,
                                  fg=BROWN)
        self.usernameE.place(x=440,y=270)
        self.usernameE.insert(0,'Username')
        self.usernameE.bind('<FocusIn>',self.user_enter)

        #username frame
        self.usernameF = tk.Frame(self,
                                  width=330,
                                  height=2,
                                  bg=BROWN)
        self.usernameF.place(x=440,y=315)

        #password entry
        self.passwordE = tk.Entry(self,
                                  width=17,
                                  font=('Microsoft Yeahei UI Light',30),
                                  bd=0,
                                  fg=BROWN)
        self.passwordE.place(x=440,y=340)
        self.passwordE.insert(0,'Password')
        self.passwordE.bind('<FocusIn>',self.password_enter)
  

        #password frame
        self.passwordF = tk.Frame(self,
                                  width=330,
                                  height=2,
                                  bg=BROWN)
        self.passwordF.place(x=440,y=385)

        #forget password button
        self.forgetB = tk.Button(self,
                                 text='Forgot Password?',
                                 bd=0,
                                 bg='white',
                                 activebackground='white',
                                 cursor='hand2',
                                 font=('Microsoft Yeahei UI Light',20,'bold'),
                                 fg=PURPLE,
                                 activeforeground=PURPLE)
        self.forgetB.place(x=600,y=390)

        #login button
        login_image = Image.open(self.file_path("login.png"))

        login_image = login_image.resize((240, 80))
        self.login_photo = ImageTk.PhotoImage(login_image)

        login_button = tk.Button(self,
                                 image=self.login_photo,
                                 command=self.login_user).place(x=490, y=440)  

    
    def user_enter(self, event):
        if self.usernameE.get()=='Username':
            self.usernameE.delete(0, tk.END)
        
    def password_enter(self, event):
        if self.passwordE.get()=='Password':
            self.passwordE.delete(0, tk.END)

    def login_user(self):
        if self.usernameE.get()=='' or self.passwordE.get()=='':
            messagebox.showerror('Error', 'All Fields are Required!')
        else:
            cf = {
                'user': 'sql6630612',
                'password': 'VptXF7SRQz',
                'host': 'sql6.freesqldatabase.com',
                'database': 'sql6630612',
                'raise_on_warnings': True
            }
            self.con = mysql.connector.connect(**cf)
            self.cur = self.con.cursor()
            username_query = 'SELECT username FROM users WHERE username=%s'
            self.cur.execute(username_query, (self.usernameE.get(),))
            username = self.cur.fetchone()
            password_query = 'SELECT password FROM users WHERE password=%s'
            self.cur.execute(password_query, (self.passwordE.get(),))
            password=self.cur.fetchone()
            
            if username == None or password == None:
                messagebox.showerror('Error', 'Invalid Username or Password')
            else:
                messagebox.showinfo('Success', 'You are Logged in')
                self.destroy()
                UserStatusBoard(self.pet_experience, username, password)
                #VirtualRagdollCatcafe()
                

    def file_path(self, filename):
        assets_folder = os.path.join("assets")
        path = os.path.join(assets_folder, filename)
        return path



#BackLoginPage(PetExperience())






