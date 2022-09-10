
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



def light_dark_mode():
    # theme = ""
    # Set light mode
    global theme
    if theme == 1:
        global fore
        fore = "#000000"
        global back
        back = "#FFFFFF"

        theme = theme - 1

    # Set dark mode
    else:

        fore = "#FFFFFF"

        back = "#000000"

        theme = theme + 1


# Signup interface
def signup(background, foreground):
    light_dark_mode()
    # Clears the main window to print the results page
    for widget in root.winfo_children():
        widget.grid_forget()

    # Title
    title = Label(root, text="BANK", font=("Palatino Linotype", 30, "bold"), bg=background, fg=foreground)
    title.grid(row=0, column=0, columnspan=2, pady=3)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    signup_label = Label(root, text="Sign up for free", font=("Palatino Linotype", 18, "bold"), bg=background,
                         fg=foreground)
    signup_label.grid(row=1, column=0, columnspan=2, pady=20)
    username_label = Label(root, text="Username: ", font=("Palatino Linotype", 17, "bold"), bg=background,
                           fg=foreground)
    username_label.grid(row=2, column=0, sticky=E)
    password_label = Label(root, text="Password: ", font=("Palatino Linotype", 17, "bold"), bg=background,
                           fg=foreground)
    password_label.grid(row=3, column=0, sticky=E, pady=10)
    password_repeat_label = Label(root, text="Repeat password: ", font=("Palatino Linotype", 17, "bold"),
                                  bg=background, fg="#FFFFFF")
    password_repeat_label.grid(row=4, column=0, sticky=E)
    username_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg=background, fg=foreground)
    username_entrybar.grid(row=2, column=1, sticky=W)
    password_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg=background, fg=foreground)
    password_entrybar.grid(row=3, column=1, sticky=W)
    password_repeat_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15), bg=background,
                                     fg=foreground)
    password_repeat_entrybar.grid(row=4, column=1, columnspan=2, sticky=W)
    signup_button = Button(root, text="Sign up", font=("Palatino Linotype", 16, "bold"), borderwidth=3,
                           bg=background, fg=foreground)
    signup_button.grid(row=5, column=0, columnspan=2, ipadx=8, pady=20)
    divider = Label(root, bg=background)
    divider.grid(row=6, column=0, columnspan=2, pady=30)
    login_label = Label(root, text="Already have an account?", font=("Palatino Linotype", 16, "bold"),
                        borderwidth=3, bg=background, fg=foreground)
    login_label.grid(row=7, column=0, columnspan=2)
    login_button = Button(root, text="Login", font=("Palatino Linotype", 16, "bold"), borderwidth=3, command=login,
                          bg=background, fg=foreground)
    login_button.grid(row=8, column=0, columnspan=2)

    # Dark mode button
    dark_button = Button(root, image=lamp_off, command="signup(back, fore)")
    dark_button.grid(row=0, column=1, sticky=E, padx=5)


# Login interface
def login():
    # Clears the main window
    for widget in root.winfo_children():
        widget.grid_forget()

    # Title
    title = Label(root, text="BANK", font=("Palatino Linotype", 30, "bold"))
    title.grid(row=0, column=0, columnspan=2, pady=3)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    login_label = Label(root, text="Log in to your account", font=("Palatino Linotype", 18, "bold"))
    login_label.grid(row=1, column=0, columnspan=2, pady=20)
    username_label = Label(root, text="Username: ", font=("Palatino Linotype", 17, "bold"))
    username_label.grid(row=2, column=0, sticky=E)
    password_label = Label(root, text="Password: ", font=("Palatino Linotype", 17, "bold"))
    password_label.grid(row=3, column=0, sticky=E, pady=10)
    username_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15))
    username_entrybar.grid(row=2, column=1, sticky=W)
    password_entrybar = Entry(root, borderwidth=3, font=("Palatino Linotype", 15))
    password_entrybar.grid(row=3, column=1, sticky=W)
    login_button = Button(root, text="Login", font=("Palatino Linotype", 16, "bold"), borderwidth=3)
    login_button.grid(row=4, column=0, columnspan=2, ipadx=8, pady=15)
    divider = Label(root)
    divider.grid(row=5, column=0, columnspan=2, pady=53)
    signup_label = Label(root, text="Dont have an account?", font=("Palatino Linotype", 16, "bold"), borderwidth=3)
    signup_label.grid(row=6, column=0, columnspan=2)
    signup_button = Button(root, text="Sign up", font=("Palatino Linotype", 16, "bold"), borderwidth=3,
                           command=signup(back, fore))
    signup_button.grid(row=7, column=0, columnspan=2)

    # Dark mode button
    dark_button = Button(root, image=lamp_off)
    dark_button.grid(row=0, column=1, sticky=E, padx=5)


# Runs the program
login()


root.mainloop()

# Comments:
# Add dark mode button
