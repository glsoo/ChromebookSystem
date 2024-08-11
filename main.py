#file setup
import time, tkinter
from tkinter import *

#define variables
win = Tk()
icon = PhotoImage(file="./assets/cmsiconr2.png")
window_width = round(win.winfo_screenwidth() * 0.60)
window_height = round(win.winfo_screenheight() * 0.60)
window_resolution = str(window_width)+"x"+str(window_height)
win.geometry(window_resolution)
win.title("Chromebook Management System")
win.iconphoto(True, icon)
label = Label(win, text="BMCCHS Chromebook Management System", font=("Arial", 16, "bold"), fg="black")

# Pack the label into the window
label.pack(pady=20)  # Add some padding to the top

#start the Tk mainloop
win.mainloop()

