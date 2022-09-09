
# LOGIN INTERFACE

from tkinter import *

root = Tk()
root.title("Login interface")
root.geometry("900x550")
root.configure(bg="#000000")
root.resizable(False, False)


# Signup interface
def signup():
    # Clears the main window to print the results page
    for widget in root.winfo_children():
        widget.grid_forget()

    # Title
    title = Label(root, text="BANK", font=("Palatino Linotype", 30, "bold"), bg="#000000", fg="#FFFFFF")
    title.grid(row=1, column=0, columnspan=2)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    login_label = Label(root, text="Sign up for free", font=("Palatino Linotype", 18, "bold"), bg="#000000",
                        fg="#FFFFFF")
    login_label.grid(row=3, column=0, columnspan=2, pady=20)
    username_label = Label(root, text="Username: ", font=("Palatino Linotype", 17, "bold"), bg="#000000", fg="#FFFFFF")
    username_label.grid(row=4, column=0, sticky=E)
    password_label = Label(root, text="Password: ", font=("Palatino Linotype", 17, "bold"), bg="#000000", fg="#FFFFFF")
    password_label.grid(row=5, column=0, sticky=E, pady=10)
    password_repeat_label = Label(root, text="Repeat password: ", font=("Palatino Linotype", 17, "bold"), bg="#000000",
                                  fg="#FFFFFF")
    password_repeat_label.grid(row=6, column=0, sticky=E)
    username_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg="#000000", fg="#FFFFFF")
    username_entrybar.grid(row=4, column=1, sticky=W)
    password_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg="#000000", fg="#FFFFFF")
    password_entrybar.grid(row=5, column=1, sticky=W)
    password_repeat_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg="#000000", fg="#FFFFFF")
    password_repeat_entrybar.grid(row=6, column=1, columnspan=2, sticky=W)
    signup_button = Button(root, text="Sign up", font=("Palatino Linotype", 16, "bold"), borderwidth=3, bg="#000000",
                           fg="#FFFFFF")
    signup_button.grid(row=7, column=0, columnspan=2, ipadx=8, pady=20)
    divider = Label(root, bg="#000000")
    divider.grid(row=8, column=0, columnspan=2, pady=30)
    login_label = Label(root, text="Already have an account?", font=("Palatino Linotype", 16, "bold"), borderwidth=3,
                         bg="#000000", fg="#FFFFFF")
    login_label.grid(row=9, column=0, columnspan=2)
    login_button = Button(root, text="Login", font=("Palatino Linotype", 16, "bold"), borderwidth=3, bg="#000000",
                          fg="#FFFFFF", command=login)
    login_button.grid(row=10, column=0, columnspan=2)


# Login interface
def login():
    # Clears the main window
    for widget in root.winfo_children():
        widget.grid_forget()

    # Title
    title = Label(root, text="BANK", font=("Palatino Linotype", 30, "bold"), bg="#000000", fg="#FFFFFF")
    title.grid(row=1, column=0, columnspan=2)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    login_label = Label(root, text="Log in to your account", font=("Palatino Linotype", 18, "bold"), bg="#000000",
                        fg="#FFFFFF")
    login_label.grid(row=3, column=0, columnspan=2, pady=20)
    username_label = Label(root, text="Username: ", font=("Palatino Linotype", 17, "bold"), bg="#000000", fg="#FFFFFF")
    username_label.grid(row=4, column=0, sticky=E)
    password_label = Label(root, text="Password: ", font=("Palatino Linotype", 17, "bold"), bg="#000000", fg="#FFFFFF")
    password_label.grid(row=5, column=0, sticky=E, pady=10)
    username_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg="#000000", fg="#FFFFFF")
    username_entrybar.grid(row=4, column=1, sticky=W)
    password_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg="#000000", fg="#FFFFFF")
    password_entrybar.grid(row=5, column=1, sticky=W)
    login_button = Button(root, text="Login", font=("Palatino Linotype", 16, "bold"), borderwidth=3, bg="#000000",
                          fg="#FFFFFF")
    login_button.grid(row=6, column=0, columnspan=2, ipadx=8, pady=15)
    divider = Label(root, bg="#000000")
    divider.grid(row=7, column=0, columnspan=2, pady=53)
    signup_label = Label(root, text="Dont have an account?", font=("Palatino Linotype", 16, "bold"), borderwidth=3,
                         bg="#000000", fg="#FFFFFF")
    signup_label.grid(row=8, column=0, columnspan=2)
    signup_button = Button(root, text="Sign up", font=("Palatino Linotype", 16, "bold"), borderwidth=3, bg="#000000",
                           fg="#FFFFFF", command=signup)
    signup_button.grid(row=9, column=0, columnspan=2)


login()


root.mainloop()

# Comments:
# Add dark mode button
