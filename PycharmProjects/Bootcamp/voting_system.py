import tkinter

import mysql.connector as mc
import customtkinter as ct
import datetime as dt
import pyttsx3 as tts
import speech_recognition as sr


def connect_db():
    serverName = "localhost"
    dbUsername = "root"
    dbPassword = ""
    dbName = "voting_system"
    userInfo = mc.connect(host=serverName, user=dbUsername, password=dbPassword, database=dbName)
    return userInfo


def destroy_contents(*args):
    for widget in args:
        widget.destroy()


class LoginScreen:
    def __init__(self):
        self.conn = connect_db()
        self.screen = ct.CTk()
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("blue")
        self.screen.title("VOTING SYSTEM")
        self.screen.geometry("700x500")
        #self.screen.resizable(width=False, height=False)
        self.frame = ct.CTkFrame(self.screen, corner_radius=10, border_width=3)
        self.frame.pack(pady=100)
        self.label = ct.CTkLabel(self.frame, text="Login To Your Account", text_color="white",
                                 font=("Aptos", 20))
        self.label.pack(pady=30)
        self.indexNumber = ct.CTkEntry(self.frame, placeholder_text="Index Number", bg_color="transparent",
                                       height=32, width=250, corner_radius=7)
        self.indexNumber.pack(padx=20)
        self.password = ct.CTkEntry(self.frame, placeholder_text="Password", bg_color="transparent", show="*",
                                    height=32, width=250, corner_radius=7)
        self.password.pack(pady=15, padx=20)
        self.errorLabel = ct.CTkLabel(self.frame, text="")
        self.loginButton = ct.CTkButton(self.frame, text="Login", command=self.login_validation,
                                        font=("Aptos", 15),
                                        text_color="white", corner_radius=7, height=28, width=250)
        self.loginButton.pack(pady=7, padx=20)
        self.forgotPassword = ct.CTkButton(self.frame, text="Forgot Password", command=self.forgot_password,
                                           font=("Aptos", 15), text_color="white", height=28, width=250,
                                           corner_radius=7)
        self.forgotPassword.pack(pady=10, padx=20)
        self.errorLabel.pack(padx=20, pady=10)
        self.screen.mainloop()

    def login_validation(self):
        username = self.indexNumber.get()
        password = self.password.get()
        if username == "" and password == "":
            self.errorLabel.configure(self.frame, text="Please fill in the fields", font=("Aptos", 15),
                                      text_color="red", bg_color="transparent")
            self.errorLabel.pack(padx=20, pady=8)
            return
        conn = self.conn.cursor(prepared=True)
        sql = "SELECT ID FROM users WHERE Username = ?"
        conn.execute(sql, (username,))
        identifier = conn.fetchone()
        sql = "SELECT Password FROM users WHERE ID = ?"
        conn.execute(sql, identifier)
        dbPass = conn.fetchone()
        if password != dbPass[0]:
            self.errorLabel.configure(self.frame, text="Incorrect Credentials", font=("Aptos", 15),
                                      text_color="red", bg_color="transparent")
            self.errorLabel.pack(padx=20, pady=8)
        else:
            if username == dbPass[0]:
                self.change_password(identifier[0])
            else:
                self.voting_interface()

    def change_password(self, *args):
        destroy_contents(self.frame)
        self.frame = ct.CTkFrame(self.screen, border_width=3, corner_radius=10)
        self.frame.pack(pady=20)
        label = ct.CTkLabel(self.frame, text="Change the default password", text_color="white",
                            font=("Aptos", 20))
        label.pack(pady=20)
        oldPass = ct.CTkEntry(self.frame, placeholder_text="Old Password", width=300, height=32, show="*")
        oldPass.pack(pady=20)
        newPass = ct.CTkEntry(self.frame, placeholder_text="New Password", width=300, height=32,show="*")
        newPass.pack(pady=20)
        confirmPass = ct.CTkEntry(self.frame, placeholder_text="Confirm Password", height=32, width=300, show="*")
        confirmPass.pack(pady=20)
        done = ct.CTkButton(self.frame, text="Done", font=("Aptos", 15), text_color="white", width=300, height=28,
                            command=lambda: self.update_password(userId=args[0], newPass=newPass, confirmPass=confirmPass,
                                                                 oldPass=oldPass))
        done.pack(pady=20)

    def update_password(self, userId, oldPass, newPass, confirmPass):
        oldPass = oldPass.get()
        newPass = newPass.get()
        identifier = userId
        confirmPass = confirmPass.get()
        conn = self.conn.cursor()
        sql = "SELECT Password FROM users WHERE ID = %s"
        print("after second sql")
        conn.execute(sql, (identifier,))
        print("after first execute")
        dbPass = conn.fetchone()
        if oldPass == dbPass[0]:
            if newPass == confirmPass:
                stmt = "UPDATE users SET Password = %s WHERE ID = %s"
                conn.execute(stmt, (newPass, identifier))
                self.conn.commit()
                self.voting_interface()
            else:
                error = ct.CTkLabel(self.frame, text="Passwords do not match", text_color="red",
                                    font=("Aptos", 15))

    def forgot_password(self):
        pass

    def voting_interface(self):
        destroy_contents(self.frame)
        label = ct.CTkLabel(self.screen, text="Select A Category And Cast Your Vote", font=("Aptos", 16, "normal"))
        label.pack(pady=10)
        tab = ct.CTkTabview(self.screen, corner_radius=10, height=500)
        tab.pack(pady=10)
        tab.add("SRC President")
        tab.add("Treasurer")
        tab.set("SRC President")



screen = LoginScreen()

