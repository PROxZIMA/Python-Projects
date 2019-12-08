from tkinter import *

def donothing():
   x = 0

win = Tk()

menubar = Menu(win)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Past", command=donothing)
editmenu.add_command(label="Duplicate Line", command=donothing)
editmenu.add_command(label="Toggle Case", command=donothing)
menubar.add_cascade(label="Edit",menu=editmenu)

win.config(menu=menubar)
win.mainloop()