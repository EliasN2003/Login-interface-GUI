
# LOGIN INTERFACE

from tkinter import *

root = Tk()
root.title("Login interface")
root.geometry("900x550")
root.resizable(False, False)

lamp_on = PhotoImage(file="images/lamp_on.png")
lamp_off = PhotoImage(file="images/lamp_off.png")

# Dark or light mode
# 1 for light, 0 for dark
theme = 1
back = "#FFFFFF"
fore = "#000000"
lamp = lamp_on
cur_color = fore


def signup_themechange():
    light_dark_mode()
    signup()


def login_themechange():
    light_dark_mode()
    login()


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
        global cur_color
        cur_color = "#000000"


    # Sets light mode
    else:
        fore = "#000000"
        back = "#FFFFFF"
        theme = theme + 1
        root.configure(bg="#FFFFFF")
        lamp = lamp_on
        cur_color = "#000000"


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
    username_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg=back, fg=fore)
    username_entrybar.grid(row=2, column=1, sticky=W)
    password_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg=back, fg=fore)
    password_entrybar.grid(row=3, column=1, sticky=W)
    password_repeat_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg=back,
                                     fg=fore)
    password_repeat_entrybar.grid(row=4, column=1, columnspan=2, sticky=W)
    signup_button = Button(root, text="Sign up", font=("Palatino Linotype", 16, "bold"), borderwidth=3,
                           bg=back, fg=fore)
    signup_button.grid(row=5, column=0, columnspan=2, ipadx=8, pady=20)
    divider = Label(root, bg=back)
    divider.grid(row=6, column=0, columnspan=2, pady=30)
    login_label = Label(root, text="Already have an account?", font=("Palatino Linotype", 16, "bold"),
                        borderwidth=3, bg=back, fg=fore)
    login_label.grid(row=7, column=0, columnspan=2)
    login_button = Button(root, text="Login", font=("Palatino Linotype", 16, "bold"), borderwidth=3, command=login,
                          bg=back, fg=fore)
    login_button.grid(row=8, column=0, columnspan=2)

    # Dark mode button
    dark_button = Button(root, image=lamp, command=signup_themechange, bg=back)
    dark_button.grid(row=0, column=1, sticky=E, padx=5)


# Login interface
def login():
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
    login_button = Button(root, text="Login", font=("Palatino Linotype", 16, "bold"), borderwidth=3, bg=back, fg=fore)
    login_button.grid(row=4, column=0, columnspan=2, ipadx=8, pady=15)
    divider = Label(root, bg=back, fg=fore)
    divider.grid(row=5, column=0, columnspan=2, pady=53)
    signup_label = Label(root, text="Dont have an account?", font=("Palatino Linotype", 16, "bold"),
                         borderwidth=3, bg=back, fg=fore)
    signup_label.grid(row=6, column=0, columnspan=2)
    signup_button = Button(root, text="Sign up", font=("Palatino Linotype", 16, "bold"), borderwidth=3,
                           command=signup, bg=back, fg=fore)
    signup_button.grid(row=7, column=0, columnspan=2)

    # Dark mode button
    dark_button = Button(root, image=lamp, command=login_themechange, bg=back)
    dark_button.grid(row=0, column=1, sticky=E, padx=5)


# Runs the program
login()


root.mainloop()
