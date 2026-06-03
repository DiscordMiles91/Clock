import tkinter as tk
import os
import sys
from time import strftime
import ctypes

win = tk.Tk()
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#Quartz crystal
def clockcrystal():
    clock = strftime("%H:%M:%S")
    clockclock.config(text=clock)

    win.after(100, clockcrystal)



#Black magic that makes the window dragable
offset_x = 0
offset_y = 0

def start_move(event):
    global offset_x, offset_y

    offset_x = event.x_root - win.winfo_x()
    offset_y = event.y_root - win.winfo_y()

def do_move(event):
    x = event.x_root - offset_x
    y = event.y_root - offset_y

    win.geometry(f"+{x}+{y}")



#You can't be invisible forever!
def set_appwindow():

    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080

    hwnd = ctypes.windll.user32.GetParent(win.winfo_id())

    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

    style &= ~WS_EX_TOOLWINDOW
    style |= WS_EX_APPWINDOW

    ctypes.windll.user32.SetWindowLongW(
        hwnd,
        GWL_EXSTYLE,
        style
    )



#Binding
def bind_dragging():

    widgets = [win, clockclock]

    for widget in widgets:
        widget.bind("<Button-1>", start_move)
        widget.bind("<B1-Motion>", do_move)



#The microcondrea is the powerhouse of the cell


w = 200 
h = 70

# Hides window during startup
win.withdraw()

#yadah yadah
win.iconbitmap(resource_path("clock.ico"))
win.resizable(False, False)
win.title("Clock")

# startup posistion
ws = win.winfo_screenwidth() # width of the screen
hs = win.winfo_screenheight() # height of the screen

# math owo
ex = (ws/2) - (w/2)
why = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
win.geometry('%dx%d+%d+%d' % (w, h, ex, why))


# borderless
win.overrideredirect(True)

# clock, appear!
clockclock = tk.Label(win,font=("Arial", 30),fg="white",bg="blue")

clockclock.pack(fill="both", expand=True)

set_appwindow()
bind_dragging()
clockcrystal()

win.deiconify()

# bring window to front
win.lift()
win.attributes("-topmost", True)
#win.after(100, lambda: win.attributes("-topmost", False))
win.focus_force()

#context menu
def Die(isthissupposedtobeavariable):
    view_menu .tk_popup(isthissupposedtobeavariable.x_root, isthissupposedtobeavariable.y_root)

  
view_menu = tk.Menu(win, tearoff=0)

what = tk.IntVar()
what.set(1)

def tu():
    win.attributes("-topmost", bool(what.get()))

view_menu.add_checkbutton(label="Always stay on top", onvalue=1, offvalue=0, variable=what, command=tu)
view_menu.add_separator()
view_menu.add_command(label="Exit", command =win.destroy)

win.bind("<Button-3>", Die)
win.mainloop()

win.mainloop()