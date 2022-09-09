
# LOGIN INTERFACE

from tkinter import *

root = Tk()
root.title("Login interface")
root.geometry("800x460")

# Title
title = Label(root, text="COMPANY NAME", font=("Times New Roman", 30, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=5)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
divider = Label(root)
divider.grid(row=1, column=0, columnspan=2, pady=7)

# Login interface
username_label = Label(root, text="Username: ", font=("Arial", 17, "bold"))
username_label.grid(row=2, column=0, sticky=E)
password_label = Label(root, text="Password: ", font=("Arial", 17, "bold"))
password_label.grid(row=3, column=0, sticky=E, pady=10)
username_entrybar = Entry(root, borderwidth=3, font=("Arial", 15))
username_entrybar.grid(row=2, column=1, sticky=W)
password_entrybar = Entry(root, borderwidth=3, font=("Arial", 15))
password_entrybar.grid(row=3, column=1, sticky=W)
login_button = Button(root, text="Login", font=("Times New Roman", 16, "bold"), borderwidth=3)
login_button.grid(row=4, column=0, columnspan=2, ipadx=8, pady=15)

root.mainloop()
