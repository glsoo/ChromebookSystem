#file setup
import time, tkinter
from tkinter import *

#define variables
icon = PhotoImage(file="/assets/cmsicon.png")
win = Tk()
window_width = round(win.winfo_screenwidth() * 0.60)
window_height = round(win.winfo_screenheight() * 0.60)
window_resolution = str(window_width)+"x"+str(window_height)
win.geometry(window_resolution)
win.title("Chromebook Management System")
win.iconphoto(False, icon)

#start the Tk mainloop
win.mainloop()

