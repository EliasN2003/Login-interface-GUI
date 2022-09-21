
# Application for the login interface

from tkinter import *


app = Tk()
app.title("Application")
width = 900
height = 550
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
app.geometry("%dx%d+%d+%d" % (width, height, x, y))
app.resizable(False, False)



label = Label(app, text="HELLO")
label.pack()
button = Button(app)
button.pack()



app.mainloop()
