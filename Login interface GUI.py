
# LOGIN INTERFACE

from tkinter import *
import sqlite3


root = Tk()
root.title("Login interface")
width = 900
height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, False)

lamp_on = PhotoImage(file="images/lamp_on.png")
lamp_off = PhotoImage(file="images/lamp_off.png")

# Dark or light mode
# 1 for light, 0 for dark
theme = 1
back = "#FFFFFF"
fore = "#000000"
lamp = lamp_on

# Variables used for creating users and logging in
username = StringVar()
password = StringVar()
password_confirm = StringVar()


def database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                   "username TEXT, password TEXT, firstname TEXT)")


# Dark/light mode for the signup page
def signup_themechange():
    light_dark_mode()
    signup()


# Dark/light mode for the login page
def login_themechange():
    light_dark_mode()
    login_interface()


# Sets light and dark mode
def light_dark_mode():
    # Sets dark mode
    global theme
    if theme == 1:
        global fore
        fore = "#FFFFFF"
        global back
        back = "#000000"
        theme = theme - 1
        root.configure(bg="#000000")
        global lamp
        lamp = lamp_off


    # Sets light mode
    else:
        fore = "#000000"
        back = "#FFFFFF"
        theme = theme + 1
        root.configure(bg="#FFFFFF")
        lamp = lamp_on


def run():
    print("Made it!")


def login():
    database()
    if username.get() == "" or password.get() == "":
        result_holder.config(text="Please fill all the required fields!", bg=back, fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?",
                       (username.get(), password.get()))
        if cursor.fetchone() is not None:
            run()
        else:
            result_holder.config(text="Invalid username or password", bg=back, fg="red")


def create_user():
    database()
    if username.get() == "" or password.get() == "" or password_confirm.get() == "":
        result_holder.config(text="Please fill all the required fields!", bg=back, fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (username.get(),))
        if cursor.fetchone() is not None:
            result_holder.config(text="Username is already taken", bg=back, fg="red")
        else:
            cursor.execute("INSERT INTO `member` (username, password, firstname) VALUES(?, ?, ?)",
                           (str(username.get()), str(password.get()), str(password_confirm.get())))
            conn.commit()
            username.set("")
            password.set("")
            password_confirm.set("")
            result_holder.config(text="Successfully Created!", bg=back, fg="black")
        cursor.close()
        conn.close()


# Signup interface
def signup():
    # Clears the main window to print the results page
    for widget in root.winfo_children():
        widget.grid_forget()

    # Title
    title = Label(root, text="BANK", font=("Palatino Linotype", 30, "bold"), bg=back, fg=fore)
    title.grid(row=0, column=0, columnspan=2, pady=3)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    signup_label = Label(root, text="Sign up for free", font=("Palatino Linotype", 18, "bold"), bg=back,
                         fg=fore)
    signup_label.grid(row=1, column=0, columnspan=2, pady=20)
    username_label = Label(root, text="Username: ", font=("Palatino Linotype", 17, "bold"), bg=back,
                           fg=fore)
    username_label.grid(row=2, column=0, sticky=E)
    password_label = Label(root, text="Password: ", font=("Palatino Linotype", 17, "bold"), bg=back,
                           fg=fore)
    password_label.grid(row=3, column=0, sticky=E, pady=10)
    password_repeat_label = Label(root, text="Repeat password: ", font=("Palatino Linotype", 17, "bold"),
                                  bg=back, fg=fore)
    password_repeat_label.grid(row=4, column=0, sticky=E)
    username_entrybar = Entry(root, textvariable=username, borderwidth=3, font=("Palatino Linotype", 15), bg=back,
                              fg=fore)
    username_entrybar.grid(row=2, column=1, sticky=W)
    password_entrybar = Entry(root, textvariable=password, borderwidth=3, font=("Palatino Linotype", 15), bg=back,
                              fg=fore)
    password_entrybar.grid(row=3, column=1, sticky=W)
    password_repeat_entrybar = Entry(root, textvariable=password_confirm, borderwidth=3, font=("Palatino Linotype", 15),
                                     bg=back, fg=fore)
    password_repeat_entrybar.grid(row=4, column=1, columnspan=2, sticky=W)
    signup_button = Button(root, text="Sign up", font=("Palatino Linotype", 16, "bold"), cursor='hand2', borderwidth=3,
                           bg=back, fg=fore, command=create_user)
    signup_button.grid(row=5, column=0, columnspan=2, ipadx=8, pady=20)
    global result_holder
    result_holder = Label(root, text="", font=("Palatino Linotype", 16, "bold"), bg=back)
    result_holder.grid(row=6, column=0, columnspan=2, ipady=10, ipadx=15)
    login_label = Label(root, text="Already have an account?", font=("Palatino Linotype", 16, "bold"),
                        borderwidth=3, bg=back, fg=fore)
    login_label.grid(row=7, column=0, columnspan=2, pady=(27, 0), sticky=N)
    login_button = Button(root, text="Login", font=("Palatino Linotype", 16, "bold"), cursor='hand2', borderwidth=3,
                          command=login_interface, bg=back, fg=fore)
    login_button.grid(row=8, column=0, columnspan=2)

    # Dark mode button
    dark_button = Button(root, image=lamp, command=signup_themechange, cursor='hand2', bg=back)
    dark_button.grid(row=0, column=1, sticky=E, padx=5)


# Login interface
def login_interface():
    # Clears the main window
    for widget in root.winfo_children():
        widget.grid_forget()

    # Title
    title = Label(root, text="BANK", font=("Palatino Linotype", 30, "bold"), bg=back, fg=fore)
    title.grid(row=0, column=0, columnspan=2, pady=3)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    login_label = Label(root, text="Log in to your account", font=("Palatino Linotype", 18, "bold"), bg=back, fg=fore)
    login_label.grid(row=1, column=0, columnspan=2, pady=20)
    username_label = Label(root, text="Username: ", font=("Palatino Linotype", 17, "bold"), bg=back, fg=fore)
    username_label.grid(row=2, column=0, sticky=E)
    password_label = Label(root, text="Password: ", font=("Palatino Linotype", 17, "bold"), bg=back, fg=fore)
    password_label.grid(row=3, column=0, sticky=E, pady=10)
    username_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg=back, fg=fore)
    username_entrybar.grid(row=2, column=1, sticky=W)
    password_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg=back, fg=fore)
    password_entrybar.grid(row=3, column=1, sticky=W)
    login_button = Button(root, text="Login", font=("Palatino Linotype", 16, "bold"), cursor='hand2', borderwidth=3,
                          bg=back, fg=fore, command=login)
    login_button.grid(row=4, column=0, columnspan=2, ipadx=8, pady=15)
    divider = Label(root, bg=back, fg=fore)
    divider.grid(row=5, column=0, columnspan=2, pady=53)
    signup_label = Label(root, text="Don't have an account?", font=("Palatino Linotype", 16, "bold"),
                         borderwidth=3, bg=back, fg=fore)
    signup_label.grid(row=6, column=0, columnspan=2)
    signup_button = Button(root, text="Sign up", font=("Palatino Linotype", 16, "bold"), cursor='hand2', borderwidth=3,
                           command=signup, bg=back, fg=fore)
    signup_button.grid(row=7, column=0, columnspan=2)

    # Dark mode button
    dark_button = Button(root, image=lamp, command=login_themechange, cursor='hand2', bg=back)
    dark_button.grid(row=0, column=1, sticky=E, padx=5)


# Runs the program
login_interface()


root.mainloop()
