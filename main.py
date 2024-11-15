#file setup
import time, tkinter
from tkinter import *
#define functions
def send():
    lendB.config(text = "Submitting..")
    idvalue = identry.get()
    credvalue = credentry.get()
    credentry.delete(0, END)
    #put send packet command here
def receive():
    receiveB.config(text = "Submitting..")
    credvalue = credentry.get()
    credentry.delete(0, END)
    #put get data command here
    # identry.config(text = "pulled id value")
    #send data "not lent" to database
def credClicked(event):
    credentry.config(show="*")
    credentry.delete(0, END)
def idClicked(event):
    identry.delete(0, END)
#define variables
win = Tk()
icon = PhotoImage(file="./assets/cmsiconr2.png")
window_width = round(win.winfo_screenwidth() * 0.60)
window_height = round(win.winfo_screenheight() * 0.60)
window_resolution = str(window_width)+"x"+str(window_height)
win.geometry(window_resolution)
win.title("Chromebook Management System")
win.iconphoto(True, icon)
title = Label(win, text="BMCCHS Chromebook Management System", font=("Arial", 16, "bold"), fg="black")
buttonF = Frame(win)
lendB = Button(buttonF, text="Lend", font=("Arial", 16), fg="white", bg="black", command=send)
receiveB = Button(buttonF, text="Receive", font=("Arial", 16), fg="white", bg="black", command=receive)
identry = Entry(win, font=("Arial", 16), fg="black")
identry.insert(0, "Chromebook ID") 
credentry = Entry(win, font=("Arial", 16), fg="black")
credentry.insert(0, "Admin password")
# Pack the label into the window
title.pack(pady=20)  # Add some padding to the top
buttonF.pack()
lendB.pack(side="left", padx=10)
receiveB.pack(side="right", padx=10)
identry.pack(pady=20)
credentry.pack()
#button binds
credentry.bind("<1>", credClicked)
identry.bind("<1>", idClicked)
#start the Tk mainloop
win.mainloop()
